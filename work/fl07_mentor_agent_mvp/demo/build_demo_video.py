"""Build a short captioned demo MP4 from the real E2E agent run (no YouTube)."""
from __future__ import annotations

import textwrap
from pathlib import Path

import imageio.v2 as imageio
from PIL import Image, ImageDraw, ImageFont

out_dir = Path(__file__).resolve().parent
W, H = 1280, 720
BG = (244, 241, 234)
INK = (20, 32, 26)
ACCENT = (11, 95, 69)

try:
    font_title = ImageFont.truetype("arialbd.ttf", 40)
    font_body = ImageFont.truetype("arial.ttf", 28)
    font_small = ImageFont.truetype("consola.ttf", 22)
except OSError:
    font_title = ImageFont.load_default()
    font_body = font_title
    font_small = font_title

# (seconds, title, body, narration caption)
slides = [
    (
        18,
        "Honest Mentor Update Agent",
        "One job: metrics packet -> honest mentor note.\n"
        "For: Haider (ML intern). Then human sends.",
        "This agent drafts mentor updates from metrics only.",
    ),
    (
        22,
        "Design decision: no send tool",
        "Overclaims are the failure mode.\n"
        "Draft + critique + revise, then STOP.\n"
        "I copy-paste after I re-check numbers.",
        "Design decision: no email connector. Draft only.",
    ),
    (
        20,
        "Live input: UPDATE + packet",
        "File: work/outputs/w05_model_vs_baseline.json\n"
        "Slim packet: live_w05_packet.json\n"
        "Trigger: UPDATE",
        "I attach the live holdout metrics JSON and say UPDATE.",
    ),
    (
        28,
        "Packet numbers (ground truth)",
        "split: client_holdout\n"
        "test_rows: 2325 | test_clients: 6\n"
        "RF precision@50: 0.9\n"
        "baseline precision@50: 0.3\n"
        "RF ROC AUC: 0.7641",
        "These are the only numbers the note may use.",
    ),
    (
        35,
        "Agent loop: DRAFT then CRITIQUE",
        "DRAFT wrote a usable review-order signal.\n"
        "CRITIQUE: name the 6-client holdout\n"
        "so transfer is not implied.",
        "It drafts, then attacks its own draft for overclaims.",
    ),
    (
        40,
        "REVISED mentor note (live result)",
        "On a 6-client holdout, RF beat CTR-gap\n"
        "on Precision@50 — ranking signal, not\n"
        "traffic promise.\n"
        "P@50: 0.9 vs 0.3 | AUC 0.7641\n"
        "Ask: P@50 + top-20 hand review gate?",
        "Revised note cites 0.9 vs 0.3 and six clients.",
    ),
    (
        25,
        "Human gate line",
        "Human must re-check every number\nagainst the packet before send.",
        "I still verify every figure before I send.",
    ),
    (
        28,
        "Limitation: thin packet refuse",
        'UPDATE + {"model":"random_forest"}\n'
        "Agent asks for missing metrics.\n"
        "No invented P@50 or AUC.",
        "Limitation: without a real packet it refuses — no invented metrics.",
    ),
    (
        20,
        "Eval v2: 5/5 pass",
        "1 happy path | 2 holdout | 3 thin refuse\n"
        "4 overclaim bait | 5 dual-file ask\n"
        "See eval_results_v2.md",
        "Pre-build evals all pass after the critique step.",
    ),
    (
        18,
        "Done",
        "README: work/fl07_mentor_agent_mvp/README.md\n"
        "Repo: haideriqbal499/Flyrank_Ml_internship",
        "That is the end-to-end loop: request to result.",
    ),
]


def draw_slide(title: str, body: str, caption: str) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 8], fill=ACCENT)
    d.text((48, 36), title, font=font_title, fill=INK)
    y = 110
    for para in body.split("\n"):
        for line in textwrap.wrap(para, width=56) or [""]:
            d.text((48, y), line, font=font_body, fill=INK)
            y += 36
    d.rectangle([0, H - 110, W, H], fill=INK)
    cap_y = H - 90
    for line in textwrap.wrap("Narration: " + caption, width=70):
        d.text((48, cap_y), line, font=font_small, fill=BG)
        cap_y += 28
    return img


def main() -> None:
    fps = 2
    frames: list[Image.Image] = []
    total_secs = 0
    for secs, title, body, caption in slides:
        frame = draw_slide(title, body, caption)
        for _ in range(max(1, int(secs * fps))):
            frames.append(frame)
        total_secs += secs

    out_path = out_dir / "honest_mentor_update_agent_demo.mp4"
    imageio.mimsave(out_path, frames, fps=fps, codec="libx264", quality=7)
    print(
        f"wrote {out_path} seconds~{total_secs} frames={len(frames)} "
        f"bytes={out_path.stat().st_size}"
    )


if __name__ == "__main__":
    main()
