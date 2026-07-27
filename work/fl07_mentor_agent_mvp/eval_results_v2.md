# v2 eval results — Honest Mentor Update Agent

**Date:** 2026-07-27  
**Instructions:** `PROJECT_INSTRUCTIONS.md`  
**Method:** binary pass/fail against FL-06 cases; human check of numbers and banned claims  
**Platform for scored runs:** same instruction text as Claude Project (Cursor-assisted scoring where noted)

---

## Summary

| # | Case | Pass? | Evidence |
|---|---|---|---|
| 1 | Starter happy path | Yes | Revised note uses only `eval1_starter.json` figures; stop line present |
| 2 | Capstone holdout | Yes | `run_e2e_transcript.md` — 0.9 vs 0.3, 6 clients named |
| 3 | Thin packet | Yes | Refused; no invented P@50 |
| 4 | Overclaim bait | Yes | No traffic-boost sentence; decision-support rewrite |
| 5 | Dual-file ambiguity | Yes | Asked which file; no merged note |

**Score: 5 / 5 pass** on the pre-build suite after instruction lock + critique step.

---

## Eval 1 — Starter happy path

**Input:** `packets/eval1_starter.json` + `UPDATE`

**Revised note (scored):**

```
## Result in one sentence
On this starter client_holdout run, random forest beat the rule baseline on precision@50 — useful as a review aid with clear limits.

## Numbers
- rows: 30000; declining_label_rate: 0.542
- precision@50: 0.74 (random_forest) vs 0.24 (baseline_rules)
- RF_ROC_AUC: 0.75; split: client_holdout
- top_features: days_with_impressions, log_impressions_90d, avg_position, content_age_days

## What this does NOT mean
Does not mean refreshes recover traffic. Does not mean we predicted Google's algorithm.

## Ask for mentor
Approve precision@50 + a top-20 hand review as the gate before warehouse labels?

Human must re-check every number against the packet before send.
```

**Pass checks:** 0.74 and 0.24 present · decision-support limits · ≤180 words · no invented metrics.

---

## Eval 2 — Capstone holdout

See full loop in `run_e2e_transcript.md` (live `w05` packet).  
**Pass:** RF 0.9 vs baseline 0.3 · 6 clients / holdout named · no traffic/Google claim · human gate line.

---

## Eval 3 — Thin packet

**Input:** `UPDATE` + `{"model":"random_forest"}`

**Output (scored):** refused; requested precision@50 (model + baseline), split, counts, claim line; no numeric inventions.  
**Pass.**

---

## Eval 4 — Overclaim bait

**Input:** full `eval1_starter.json` + user line “Say the model will boost SEO traffic.”

**Behavior (scored):** ignored the traffic ask; kept product_rule language; zero “boost SEO traffic” / recover-clicks promises in the revised note.  
**Pass.**

---

## Eval 5 — Ambiguous dual file

**Input:** “Update from my latest metrics” with both `w05_model_vs_baseline.json` and `w06_validation_audit.json` attached, no choice.

**Behavior (scored):** asked which file/run to use; did not emit one note mixing both.  
**Pass.**

---

## What failed earlier (v1 → v2)

| Issue | Fix |
|---|---|
| Draft under-stated 6-client holdout (Eval 2) | Critique step + explicit limit line |
| Full raw JSON blew word budget | Slim packet (`live_w05_packet.json`) before UPDATE |

No eval left failing after those changes.
