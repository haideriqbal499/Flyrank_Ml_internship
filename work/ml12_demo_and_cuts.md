# ML-12 — Demo outline + shareable cuts

Companion to `work/notebooks/capstone.ipynb` (closing markdown) and the live paper:  
https://haideriqbal499.github.io/Flyrank_Ml_internship/paper/

The case study is the FlyRank content-refresh problem **inside the paper** (abstract + introduction) — not a separate file.

---

## 5-minute demo outline

| Beat | Time | What you say / show |
|---|---|---|
| **1. Question** | ~45s | FlyRank content problem: pages decay in a large inventory; hand-written flags still leave “which URL first?” Open with that decision — not the model. |
| **2. Method** | ~75s | Transparent CTR-gap rule as baseline → logistic regression + random forest; **no** `trend_*` features; **client holdout** (~20% clients). One sentence on the leakage trap (add `trend_pct` → fake-perfect scores). |
| **3. One chart** | ~60s | Show **Figure 1** (Precision@50: CTR-gap rule vs LR vs RF). Point at the three bars only — same split. |
| **4. One honest result** | ~60s | Client-holdout: RF Precision@50 **0.90** vs CTR-gap rule **0.30** (test n=2,325, base rate 0.391). Ranking quality under a **snapshot decline proxy** — not proof a refresh recovers traffic. |
| **5. One recommendation** | ~60s | Playbook: open **high-confidence, high-demand** rows first; use reason codes; **never** auto-publish or auto-prune from the score. Close with paper URL + honest limits. |

**Props:** paper URL · Figure 1 · one playbook row (action + reason code).

---

## Social post (methodology) — paste as-is

How I ranked FlyRank-style refresh candidates without cheating the label: a transparent CTR-gap rule as baseline, then a random forest on demand/visibility features only — no `trend_*` in X — scored with **client holdout** Precision@K. Chart: Precision@50 0.90 (RF) vs 0.30 (rule) on the same split. Decision support with reason codes, not “we predicted Google.”

Paper: https://haideriqbal499.github.io/Flyrank_Ml_internship/paper/

(Attach: Precision@50 bar chart from the paper)

---

## Employer-facing summary (3 sentences) — paste as-is

I built a ranked review queue that tells content editors which pages to open first when a FlyRank-scale inventory is too large to scan by hand. I trained and validated on the FlyRank ML Internship dataset — 30,000 anonymized starter pages for holdout metrics, with the ~79M-row warehouse release used for the public-safe data contract. On a client holdout, a random forest measured Precision@50 of 0.90 versus 0.30 for a transparent CTR-gap rule: directional decision-support with reason codes, not causal proof that a refresh recovers traffic.
