"""Run Lane 2 baseline score logic and stamp outputs into w04_baseline_score.ipynb."""
from __future__ import annotations

import io
import json
import os
from contextlib import redirect_stdout
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
os.chdir(ROOT)

CSV = Path("data/raw/content_refresh_anonymized.csv")
OUT_DIR = Path("work/outputs")
OUT_DIR.mkdir(parents=True, exist_ok=True)
QUEUE_PATH = OUT_DIR / "baseline_action_score.csv"
METRICS_PATH = OUT_DIR / "baseline_action_score_metrics.json"
NB_PATH = Path("work/notebooks/w04_baseline_score.ipynb")


def main() -> None:
    df = pd.read_csv(CSV)
    df["is_declining_label"] = (df["trend_direction"].astype(str).str.lower() == "down").astype(int)

    bufs: dict[str, str] = {}

    def cap(key: str, fn) -> None:
        buf = io.StringIO()
        with redirect_stdout(buf):
            fn()
        bufs[key] = buf.getvalue()
        print(bufs[key], end="")

    def setup() -> None:
        print("Working dir:", os.getcwd())
        print(f"Loaded {len(df):,} rows")
        print("Lane: 2 — Refresh / Content Opportunity Scoring")
        print(f"Declining-label rate: {df['is_declining_label'].mean():.3f}")

    cap("setup", setup)

    def signal_a() -> str:
        staleness = df.copy()
        staleness["stale_bucket"] = pd.cut(
            staleness["days_since_last_update"],
            bins=[-np.inf, 90, 180, 365, np.inf],
            labels=["0-90d", "91-180d", "181-365d", "365d+"],
        )
        sig_a = (
            staleness.groupby("stale_bucket", observed=True)
            .agg(
                n=("is_declining_label", "size"),
                declining_rate=("is_declining_label", "mean"),
                median_impressions=("impressions_90d", "median"),
            )
            .reset_index()
        )
        sig_a["declining_rate"] = sig_a["declining_rate"].round(3)
        print("Signal A — days_since_last_update vs declining-label rate")
        print(sig_a.to_string(index=False))
        print(f"\nOverall declining-label rate: {df['is_declining_label'].mean():.3f}")
        rate_fresh = float(sig_a.loc[sig_a["stale_bucket"] == "0-90d", "declining_rate"].iloc[0])
        rate_181 = float(sig_a.loc[sig_a["stale_bucket"] == "181-365d", "declining_rate"].iloc[0])
        n_181 = int(sig_a.loc[sig_a["stale_bucket"] == "181-365d", "n"].iloc[0])
        rate_mid = float(sig_a.loc[sig_a["stale_bucket"] == "91-180d", "declining_rate"].iloc[0])
        # Deep-stale (180d+) is the refresh-flag threshold; judge that bucket, not a tiny 365d+ tail.
        if n_181 < 50:
            verdict = "MIXED"
            why = (
                f"181-365d has only n={n_181}; mid bucket 91-180d rate={rate_mid:.3f}. "
                "Too little deep-stale mass to trust a staleness rule here."
            )
        elif rate_181 > rate_fresh + 0.03:
            verdict = "CONFIRMED"
            why = f"181-365d declining_rate={rate_181:.3f} > fresh {rate_fresh:.3f}"
        elif rate_181 < rate_fresh - 0.03:
            verdict = "OPPOSITE"
            why = (
                f"181-365d declining_rate={rate_181:.3f} < fresh {rate_fresh:.3f} "
                f"(n={n_181}). Staleness-behind-refresh does not hold cleanly on this snapshot — "
                f"saved us from building the baseline on it. Mid bucket 91-180d is hotter ({rate_mid:.3f})."
            )
        else:
            verdict = "FALSE"
            why = f"181-365d~=fresh ({rate_181:.3f} vs {rate_fresh:.3f})"
        print(f"\nVerdict A (staleness): {verdict}")
        print("Why:", why)
        return verdict

    verdict_a_holder: list[str] = []

    def signal_a_wrap() -> None:
        verdict_a_holder.append(signal_a())

    cap("signal_a", signal_a_wrap)
    verdict_a = verdict_a_holder[0]

    verdict_b_holder: list[str] = []

    def signal_b() -> None:
        visible = df[
            (df["impressions_90d"] >= 500) & (df["avg_position"] > 0) & (df["avg_position"] <= 20)
        ].copy()
        visible["ctr_bucket"] = pd.cut(
            visible["ctr"],
            bins=[-np.inf, 0.5, 1.0, 2.0, np.inf],
            labels=["<0.5", "0.5-1", "1-2", "2+"],
        )
        sig_b = (
            visible.groupby("ctr_bucket", observed=True)
            .agg(
                n=("is_declining_label", "size"),
                declining_rate=("is_declining_label", "mean"),
                median_position=("avg_position", "median"),
            )
            .reset_index()
        )
        sig_b["declining_rate"] = sig_b["declining_rate"].round(3)
        print("Signal B — CTR buckets among visible pages (imp>=500, pos 1-20)")
        print(sig_b.to_string(index=False))
        print(f"Visible slice n={len(visible):,}")
        rate_low_ctr = float(sig_b.loc[sig_b["ctr_bucket"] == "<0.5", "declining_rate"].iloc[0])
        rate_mid_ctr = float(sig_b.loc[sig_b["ctr_bucket"] == "0.5-1", "declining_rate"].iloc[0])
        n_low = int(sig_b.loc[sig_b["ctr_bucket"] == "<0.5", "n"].iloc[0])
        if rate_low_ctr > rate_mid_ctr + 0.03:
            verdict = "CONFIRMED"
        elif rate_low_ctr < rate_mid_ctr - 0.03:
            verdict = "OPPOSITE"
        else:
            verdict = "MIXED"
        verdict_b_holder.append(verdict)
        print(f"\nVerdict B (CTR vs position): {verdict}")
        print(
            f"Why: among visible pages, CTR<0.5 declining_rate={rate_low_ctr:.3f} "
            f"(n={n_low:,}) vs CTR 0.5-1 rate={rate_mid_ctr:.3f}. "
            "This is the signal the baseline will use."
        )

    cap("signal_b", signal_b)
    verdict_b = verdict_b_holder[0]

    queue = df.copy()
    queue["ctr_gap"] = (
        (queue["impressions_90d"] >= 500)
        & (queue["avg_position"] > 0)
        & (queue["avg_position"] <= 20)
        & (queue["ctr"] < 0.5)
    ).astype(int)
    queue["reason_code"] = np.where(queue["ctr_gap"] == 1, "low_ctr_visible_page", "monitor_not_ctr_gap")
    queue["action"] = np.where(queue["ctr_gap"] == 1, "refresh_and_review_ctr", "monitor")
    queue["score"] = np.log1p(queue["impressions_90d"]) * queue["ctr_gap"]
    queue = queue.sort_values(["score", "impressions_90d"], ascending=[False, False]).reset_index(drop=True)
    queue["rank"] = np.arange(1, len(queue) + 1)
    out_cols = [
        "rank",
        "content_id",
        "client_id",
        "score",
        "reason_code",
        "action",
        "impressions_90d",
        "avg_position",
        "ctr",
        "days_since_last_update",
        "is_declining_label",
    ]
    ranked = queue[out_cols].copy()
    ranked.to_csv(QUEUE_PATH, index=False)
    n_fire = int(queue["ctr_gap"].sum())
    base_rate = float(df["is_declining_label"].mean())
    top10 = ranked.head(10)
    top50 = ranked.head(50)
    p_at_10 = float(top10["is_declining_label"].mean())
    p_at_50 = float(top50["is_declining_label"].mean())
    metrics = {
        "lane": "Lane 2: Refresh / Content Opportunity Scoring",
        "rule": "impressions_90d >= 500 AND 0 < avg_position <= 20 AND ctr < 0.5",
        "reason_code": "low_ctr_visible_page",
        "action": "refresh_and_review_ctr",
        "rows": int(len(ranked)),
        "rows_firing_rule": n_fire,
        "base_rate_declining": round(base_rate, 4),
        "precision_at_10_vs_declining_label": round(p_at_10, 4),
        "precision_at_50_vs_declining_label": round(p_at_50, 4),
        "signal_verdicts": {"staleness": verdict_a, "ctr_vs_position": verdict_b},
        "inputs_used": ["impressions_90d", "avg_position", "ctr"],
        "inputs_excluded": ["trend_direction", "trend_pct", "is_declining_label", "product flags"],
        "queue_path": "work/outputs/baseline_action_score.csv",
    }
    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    def queue_out() -> None:
        print(f"Wrote {QUEUE_PATH} ({len(ranked):,} rows)")
        print(f"Wrote {METRICS_PATH}")
        print(f"Rule fired on {n_fire:,} / {len(ranked):,} pages")
        print(f"Base rate (declining label): {base_rate:.3f}")
        print(f"Precision@10 vs declining label: {p_at_10:.3f}")
        print(f"Precision@50 vs declining label: {p_at_50:.3f}")
        print("\nTop 10 preview:")
        print(
            top10[
                [
                    "rank",
                    "score",
                    "reason_code",
                    "action",
                    "impressions_90d",
                    "avg_position",
                    "ctr",
                    "is_declining_label",
                ]
            ].to_string(index=False)
        )

    cap("queue", queue_out)

    reviews = []
    for _, row in top10.iterrows():
        why = (
            f"low_ctr_visible_page: pos={row['avg_position']:.1f}, "
            f"ctr={row['ctr']:.3f} (x100 scale), "
            f"impressions_90d={int(row['impressions_90d']):,}, score={row['score']:.2f}"
        )
        wrong = (
            "Wrong if CTR is low because of a non-search landing intent, a soft SERP feature "
            "stealing clicks, a branded query with inevitable low CTR, or the title/meta was "
            "already fixed after this snapshot."
        )
        reviews.append(
            {
                "rank": int(row["rank"]),
                "content_id": row["content_id"],
                "action": row["action"],
                "why": why,
                "what_would_make_it_wrong": wrong,
                "declining_label": int(row["is_declining_label"]),
            }
        )
    review_df = pd.DataFrame(reviews)

    def review_out() -> None:
        print(review_df[["rank", "content_id", "action", "declining_label"]].to_string(index=False))
        print("\n--- Line-by-line skeptic notes ---")
        for r in reviews:
            print(f"#{r['rank']} {r['content_id']}")
            print(f"  action: {r['action']}")
            print(f"  why: {r['why']}")
            print(f"  wrong if: {r['what_would_make_it_wrong']}")

    cap("review", review_out)

    def weak_out() -> None:
        print("Score inputs:", ["impressions_90d", "avg_position", "ctr"])
        print("Excluded from score:", ["trend_direction", "trend_pct", "is_declining_label", "product flags"])
        print(
            "Max score among non-firing rows (must be 0):",
            float(queue.loc[queue["ctr_gap"] == 0, "score"].max()),
        )
        weak = top10.loc[top10["is_declining_label"] == 0]
        print("\nTop-10 with declining_label=0 (skeptic: still may be fair CTR reviews):")
        if len(weak):
            print(weak[["rank", "content_id", "impressions_90d", "avg_position", "ctr"]].to_string(index=False))
        else:
            print("(none in this run — look for branded/SERP-feature false friends in a later hand pass)")
        print("\nLane lock confirmation: Lane 2 stays.")
        print("Signal verdicts:", {"staleness": verdict_a, "ctr_vs_position": verdict_b})

    cap("weak", weak_out)

    nb = json.loads(NB_PATH.read_text(encoding="utf-8"))
    code_keys = ["setup", "signal_a", "signal_b", "queue", "review", "weak"]
    code_i = 0
    exec_count = 1
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        key = code_keys[code_i] if code_i < len(code_keys) else None
        cell["execution_count"] = exec_count
        text = bufs.get(key, "") if key else ""
        cell["outputs"] = (
            [{"output_type": "stream", "name": "stdout", "text": text.splitlines(keepends=True) or [""]}]
            if text
            else []
        )
        code_i += 1
        exec_count += 1
    NB_PATH.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Stamped outputs into {NB_PATH}")
    print("DONE")


if __name__ == "__main__":
    main()
