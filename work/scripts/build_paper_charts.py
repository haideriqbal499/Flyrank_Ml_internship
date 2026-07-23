"""Build paper comparison chart from committed metrics receipts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "paper" / "img"
WORK_FIG = ROOT / "work" / "figures"
OUT.mkdir(parents=True, exist_ok=True)
WORK_FIG.mkdir(parents=True, exist_ok=True)

W05 = json.loads((ROOT / "work" / "outputs" / "w05_model_vs_baseline.json").read_text(encoding="utf-8"))


def escape_xml(value: str) -> str:
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def vertical_bars(title: str, labels: list[str], values: list[float], path: Path, color: str = "#0b5f45") -> None:
    width, height = 960, 520
    margin_left, margin_right, margin_top, margin_bottom = 70, 40, 70, 90
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom
    max_v = max(values) if values else 1.0
    max_v = max(max_v, 0.01)
    n = max(len(values), 1)
    gap = 24
    bar_w = (plot_w - gap * (n - 1)) / n
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{width/2}" y="36" text-anchor="middle" font-family="Arial" font-size="22" fill="#14201a">{escape_xml(title)}</text>',
        f'<line x1="{margin_left}" y1="{margin_top + plot_h}" x2="{margin_left + plot_w}" y2="{margin_top + plot_h}" stroke="#c9c2b4"/>',
    ]
    for i, (lab, val) in enumerate(zip(labels, values)):
        x = margin_left + i * (bar_w + gap)
        h = (val / max_v) * plot_h
        y = margin_top + plot_h - h
        lines.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="{color}" rx="4"/>')
        lines.append(
            f'<text x="{x + bar_w/2:.1f}" y="{y - 10:.1f}" text-anchor="middle" font-family="Arial" font-size="16" fill="#14201a">{val:.2f}</text>'
        )
        lines.append(
            f'<text x="{x + bar_w/2:.1f}" y="{margin_top + plot_h + 28}" text-anchor="middle" font-family="Arial" font-size="14" fill="#3d4a42">{escape_xml(lab)}</text>'
        )
    lines.append(
        f'<text x="{margin_left}" y="{height - 18}" font-family="Arial" font-size="13" fill="#3d4a42">'
        "Client-holdout Precision@50 (same split). Base rate on test = 0.391.</text>"
    )
    lines.append("</svg>")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    by = {row["method"]: row for row in W05["comparison"]}
    labels = ["CTR-gap rule", "Logistic regression", "Random forest"]
    keys = ["week4_ctr_gap_baseline", "logistic_regression", "random_forest"]
    values = [float(by[k]["precision@50"]) for k in keys]
    for dest in (OUT / "model_vs_baseline.svg", WORK_FIG / "capstone_model_vs_baseline.svg"):
        vertical_bars("Precision@50 on client holdout", labels, values, dest)
        print(f"Wrote {dest}")


if __name__ == "__main__":
    main()
