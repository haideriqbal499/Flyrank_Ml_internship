# FL — No-code workflow: mentor update (draft → critique → revise)

**Pipeline type:** draft, critique, revise (from the FL-01 weekly choke point: “summarize model results for mentor”)  
**Tooling:** Claude Project only (free) — no paid custom GPT, no n8n required  
**Optional later:** NotebookLM if the input is a multi-source reading pack; this chore is metrics-packet → status note, so Claude Project is enough  

**Related:** `work/fl01_prompt_iteration_log.md` (prompt ladder that fed Step 2–4)

---

## Why this pipeline

Single prompts save minutes. This chain saves the hour I used to burn rewriting overclaims. The handoff is fixed: **only pasted numbers enter → draft → attack the draft → ship a short mentor note**.

---

## Flow sketch (before build)

```text
[Human] Gather metrics packet
    │  (paste ONLY figures from notebook/JSON; no vibes)
    ▼
[Step 1 · DRAFT] Claude Project — Prompt A
    │  handoff: draft markdown block
    ▼
[Step 2 · CRITIQUE] same Project — Prompt B
    │  handoff: bullet list of overclaims / missing limits / bad asks
    ▼
[Step 3 · REVISE] same Project — Prompt C
    │  handoff: revised mentor note ≤180 words
    ▼
[Step 4 · HUMAN CHECK] me
    │  verify every number against packet; kill any new claims
    ▼
[Step 5 · FORMAT / SEND] paste into email or track thread
```

Three+ distinct steps with defined handoffs: **Gather → Draft → Critique → Revise → Human check**.

---

## Claude Project configuration

**Name:** `Mentor update — draft critique revise`

**Custom instructions (paste once):**

```
You are a careful ML intern tutor helping me write mentor updates.

Proof habit: decision-support only. Never claim refreshes recover traffic or that we predicted Google's algorithm unless an experiment is described in the packet.

Rules:
- Use ONLY numbers I paste in the current message.
- Never invent metrics, clients, charts, or URLs.
- Prefer observed / directional / decision-support language.
- Short sentences. No buzzwords.

When I say DRAFT, CRITIQUE, or REVISE, follow the matching prompt exactly.
After REVISE, remind me: "Human must re-check every number against the packet before send."
```

---

## Prompts (every configuration used)

### Prompt A — DRAFT

```
DRAFT

Audience: track mentor.
Task: turn the metrics packet below into a first mentor update.

Packet (only these numbers exist):
<<<
{PASTE_PACKET}
>>>

Write:
## Result in one sentence
## Numbers (bullets, only packet figures)
## What this does NOT mean (two lines)
## Ask for mentor (one line)

Max 180 words total. Do not invent anything outside the packet.
```

### Prompt B — CRITIQUE

```
CRITIQUE

Here is the draft:
<<<
{PASTE_DRAFT}
>>>

Here is the original packet again:
<<<
{PASTE_PACKET}
>>>

Do NOT rewrite the note.
List only:
1) Overclaims (claim → why the packet does not support it)
2) Missing limits
3) Numbers that do not appear in the packet (if any)
4) Ask-section scope drift (if any)
5) One highest-priority fix

Be specific, not encouraging.
```

### Prompt C — REVISE

```
REVISE

Packet:
<<<
{PASTE_PACKET}
>>>

Draft:
<<<
{PASTE_DRAFT}
>>>

Critique:
<<<
{PASTE_CRITIQUE}
>>>

Rewrite the mentor update to fix the critique. Same four headings. Max 180 words.
Still use only packet numbers. End with the human-check reminder line.
```

### Human check (Step 4 — required)

- [ ] Every figure appears in the packet  
- [ ] No causal traffic / Google-algorithm claim  
- [ ] Ask is one clarifying question, not a new project  
- [ ] Under ~180 words  

---

## Five real runs

Packets are real committed metrics (public-safe). Outputs below are the **revised** mentor notes after draft → critique → revise. Critique highlights are summarized per run.

### Run 1 — Starter mentor summary (FL-01 choke point)

**Input packet**

```
rows: 30000
declining_label_rate: 0.542
model: random_forest
precision@50: 0.74
baseline_rules precision@50: 0.24
RF ROC AUC: 0.750
split: client_holdout
top_features: days_with_impressions, log_impressions_90d, avg_position, content_age_days
product_rule: decision support only
```

**Critique caught:** draft said “ready for editors” without naming the proxy-label limit; ask drifted toward a traffic A/B test.

**Revised output**

```
## Result in one sentence
On this starter run, random forest beat the rule baseline at top-of-queue precision, so it is usable as a review aid with clear limits.

## Numbers
- 30,000 pages; declining-label rate 0.542
- precision@50: 0.74 (RF) vs 0.24 (baseline_rules)
- RF ROC AUC 0.750; client_holdout
- Top features: days_with_impressions, log_impressions_90d, avg_position, content_age_days

## What this does NOT mean
Does not mean refreshes recover clicks. Does not mean we modeled Google’s algorithm.

## Ask for mentor
Approve precision@50 + a top-20 hand review as the gate before warehouse labels?

Human must re-check every number against the packet before send.
```

**Timed:** ~9 min pipeline · manual estimate ~30 min  

---

### Run 2 — Capstone / client-holdout model vs baseline

**Input packet** (from `work/outputs/w05_model_vs_baseline.json` + capstone metrics)

```
split: client_holdout
test_rows: 2325
test_clients: 6
base_rate_test: 0.391
CTR-gap baseline precision@50: 0.30
logistic_regression precision@50: 0.54
random_forest precision@50: 0.90
RF ROC AUC: 0.7641
top_rf_features: avg_position, log_impressions_90d, content_age_days, days_with_impressions
claim: decision-support on snapshot decline proxy; not causal traffic recovery
```

**Critique caught:** draft compared only RF vs baseline and buried LR; almost claimed “strong transfer” from 6 clients without the sensitivity caveat.

**Revised output**

```
## Result in one sentence
Under client_holdout, random forest leads the CTR-gap rule on Precision@50; this is a ranking signal for review order, not a traffic promise.

## Numbers
- test n=2,325; 6 unseen clients; base rate 0.391
- Precision@50: RF 0.90 · LR 0.54 · CTR-gap rule 0.30
- RF ROC AUC 0.7641
- Top RF features: avg_position, log_impressions_90d, content_age_days, days_with_impressions

## What this does NOT mean
Not causal evidence a refresh recovers traffic. Not a Google-algorithm claim. Six-client holdout is evidence of transfer under this split, not a finished sensitivity study.

## Ask for mentor
Want the next note to be the random-vs-client gap from the validation audit?

Human must re-check every number against the packet before send.
```

**Timed:** ~10 min pipeline · manual ~35 min  

---

### Run 3 — Rule baseline only (before the learned ranker)

**Input packet** (from `work/outputs/baseline_action_score_metrics.json`)

```
rule: impressions_90d >= 500 AND 0 < avg_position <= 20 AND ctr < 0.5
reason_code: low_ctr_visible_page
action: refresh_and_review_ctr
rows: 30000
rows_firing_rule: 9759
base_rate_declining: 0.5421
precision_at_10_vs_declining_label: 0.6
precision_at_50_vs_declining_label: 0.42
signal_verdicts: staleness=OPPOSITE, ctr_vs_position=CONFIRMED
excluded_from_inputs: trend_direction, trend_pct, is_declining_label
```

**Critique caught:** draft treated 0.42 P@50 as “good enough to ship to editors” without saying this is the transparent baseline, not the final model.

**Revised output**

```
## Result in one sentence
The transparent CTR-gap style rule is a readable baseline: it fires on visible low-CTR pages and beats chance on the declining proxy at P@50, but it is not the final ranker.

## Numbers
- 30,000 rows; rule fires on 9,759
- base rate declining 0.5421
- precision@10 = 0.6; precision@50 = 0.42 vs declining label
- verdicts: ctr_vs_position CONFIRMED; staleness OPPOSITE
- trend fields excluded from rule inputs

## What this does NOT mean
Not a learned model result. Not proof the action recovers clicks.

## Ask for mentor
OK to keep this rule as the always-on baseline while we compare RF on Precision@50?

Human must re-check every number against the packet before send.
```

**Timed:** ~8 min pipeline · manual ~25 min  

---

### Run 4 — Validation / leakage audit

**Input packet** (from `work/outputs/w06_validation_audit.json`)

```
random_row_split: n_test=6000, base_rate=0.542, precision@50=0.96, roc_auc=0.7714
client_holdout: n_test=2325, base_rate=0.391, precision@50=0.90, roc_auc=0.7641
gap_random_minus_client precision@50: 0.06
leakage_attack honest: precision@50=0.90, top_feature=avg_position
leakage_attack with trend_pct: precision@50=1.0, roc_auc=1.0, top_feature=trend_pct (importance 0.889)
```

**Critique caught:** draft led with “model is validated” — wrong story. The packet’s point is the leakage trap and the small split gap.

**Revised output**

```
## Result in one sentence
Validation check: client-holdout stays near random-split on Precision@50, and a deliberate trend_pct leak drives metrics to 1.0 — so keeping trend out of X is non-negotiable.

## Numbers
- random split P@50 0.96 (n=6,000, base 0.542) vs client_holdout P@50 0.90 (n=2,325, base 0.391)
- gap ≈ 0.06 on Precision@50
- honest top feature avg_position; with trend_pct leak → P@50 1.0 / AUC 1.0, trend_pct dominates (0.889)

## What this does NOT mean
A small gap is not proof of perfect transfer. A perfect score with trend_pct is a warning, not a win.

## Ask for mentor
Any other holdout membership checks you want before I treat client_holdout as the default scorecard?

Human must re-check every number against the packet before send.
```

**Timed:** ~11 min pipeline · manual ~40 min (easy to mis-tell)  

---

### Run 5 — Action playbook queue mix

**Input packet** (from `work/outputs/w07_action_playbook_metrics.json`)

```
rows_scored: 30000
holdout Precision@50: 0.90
holdout ROC AUC: 0.7641
score_formula: 100 * (0.70 * model_probability + 0.30 * normalized_baseline)
action_counts: refresh 11717, monitor 9725, refresh_and_review_ctr 6296, refresh_and_review_engagement 1879, protect 301, expand_and_refresh 82
safe_claim: directional decision-support with reason codes — not causal traffic recovery
```

**Critique caught:** draft listed every action count as if volume = priority; ask proposed auto-publishing refreshes.

**Revised output**

```
## Result in one sentence
Playbook scores 30k pages with a blended RF+baseline score; holdout Precision@50 is 0.90, and the queue is for human review with reason codes.

## Numbers
- 30,000 scored; holdout P@50 0.90; ROC AUC 0.7641
- blend: 70% model probability + 30% normalized baseline
- actions (counts): refresh 11,717 · monitor 9,725 · refresh_and_review_ctr 6,296 · others smaller

## What this does NOT mean
Counts are not a publish schedule. Not causal proof a refresh recovers traffic. Not auto-apply.

## Ask for mentor
Should the next mentor note be a hand review of the top 20 with reason codes attached?

Human must re-check every number against the packet before send.
```

**Timed:** ~9 min pipeline · manual ~30 min  

---

## Brand-new input check (end-to-end)

Paste any new packet into Prompt A → B → C without changing Project instructions. Runs 1–5 used five different packets; same Project config. **Workflow runs on a brand-new input** as long as the packet is pasted fresh.

---

## Time accounting (honest)

| Item | Time |
|---|---|
| Setup (Project + three prompts + one dry run) | ~50 min (one-time) |
| Manual mentor note (careful, no pipeline) | ~25–40 min each |
| Pipeline run (gather paste + A/B/C + human check) | ~8–12 min each |
| Five documented runs | ~47 min active + setup already sunk |

**Time saved on five notes:**  
5 × ~(32 − 10) ≈ **~110 minutes** of writing/checking, after setup.  
**Net after setup:** ~110 − 50 ≈ **~60 minutes saved on this batch**; next batches keep the ~20 min/run savings without re-setup.

Setup cost is included above — not hidden.

---

## Where it breaks / what a human must still check

| Failure point | What happens | Human must |
|---|---|---|
| Thin or wrong packet | Model invents or over-smooths | Only paste figures from JSON/notebook; refuse vibes |
| Helpfulness drift in Ask | Proposes experiments / auto-publish | Delete scope that was not requested |
| Critique too soft | Overclaims survive into revise | If critique has zero overclaims, re-run B with “be harsher” |
| Number transcription | 0.74 vs 0.90 mix-ups across runs | Diff every bullet against the packet |
| Wrong story for the packet | e.g. validation run sold as “model wins” | Read packet purpose first (baseline vs model vs leakage) |
| Private data | Client names / raw URLs | Keep public-safe metrics only |

**Non-negotiable human gate:** Step 4 checklist before send. The pipeline drafts; it does not approve.

---

## Pass check

| Criterion | Evidence |
|---|---|
| Runs end-to-end on new input | Same A→B→C on five distinct packets |
| Three+ steps with handoffs | Gather → Draft → Critique → Revise → Human check |
| Five real runs with outputs | Runs 1–5 above |
| Honest time + setup | Setup ~50 min; ~8–12 vs ~25–40 per note |
| Failure points + human review | Table above |

---

## Paste for track thread

```
Workflow: Mentor update — draft → critique → revise (Claude Project).
From FL-01 choke point: summarizing model results without overclaiming.
Five runs: starter P@50 0.74; capstone 0.90; rule baseline; leakage audit; action playbook.
~8–12 min/run vs ~25–40 manual; setup ~50 min once.
Human still checks every number and kills causal claims.
Doc: work/fl_workflow_mentor_update.md
```
