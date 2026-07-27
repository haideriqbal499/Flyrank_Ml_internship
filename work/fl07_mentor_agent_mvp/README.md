# Honest Mentor Update Agent

Turn a **metrics packet** (pasted JSON or a file under `work/outputs/`) into a short **mentor update** a reviewer can trust — then stop for a human send check.

**For whom:** Haider Iqbal (ML intern / portfolio builder), ~1–3× per week after a scoring or notebook run.  
**Not for:** inbox triage, LinkedIn drafts, or “summarize my whole internship.”

| | |
|---|---|
| Spec (FL-06) | [`../agent_design_mentor_update.md`](../agent_design_mentor_update.md) |
| MVP build log (FL-07) | [`build_log.md`](build_log.md) |
| E2E transcript | [`run_e2e_transcript.md`](run_e2e_transcript.md) |
| v2 eval results | [`eval_results_v2.md`](eval_results_v2.md) |
| Demo video checklist | [`demo_video_checklist.md`](demo_video_checklist.md) |

Live portfolio (separate from this agent): https://haideriqbal499.github.io/Flyrank_Ml_internship/

---

## What it does

1. You provide **only** public-safe numbers (paste or attach JSON).
2. Agent runs **DRAFT → CRITIQUE → REVISE**.
3. Output shape: one-sentence result · numbers · “does NOT mean” · one mentor ask · ≤180 words.
4. Prints: `Human must re-check every number against the packet before send.`
5. **Does not** email, post, or commit. You copy-paste after the checklist.

---

## Setup (stranger can follow)

### Option A — Claude Project (daily home, free)

1. Create a free account at [claude.ai](https://claude.ai) → **Projects** → New project.  
   Name: `Honest Mentor Update Agent`.
2. Open [`PROJECT_INSTRUCTIONS.md`](PROJECT_INSTRUCTIONS.md). Copy everything **inside** the code fence into **Project instructions**. Save.
3. Upload as Project knowledge: [`knowledge/voice_and_limits.md`](knowledge/voice_and_limits.md).
4. (Optional) Clone this repo so you can attach real packets from disk:
   ```bash
   git clone https://github.com/haideriqbal499/Flyrank_Ml_internship.git
   cd Flyrank_Ml_internship
   ```
5. Start a **new chat inside the Project**.

### Option B — Same instructions in Cursor (filesystem proof)

1. Open this repo in Cursor.
2. Paste the Project instructions into the chat (or point the agent at `PROJECT_INSTRUCTIONS.md`).
3. Attach or `@`-mention a packet JSON, then say `UPDATE`.

You need: a Claude (or Cursor) account and this public repo. No API keys, no paid Cowork, no n8n.

---

## Usage examples

### Happy path (capstone-style holdout)

1. Attach [`packets/live_w05_packet.json`](packets/live_w05_packet.json)  
   (or paste contents of `work/outputs/w05_model_vs_baseline.json` slimmed the same way).
2. Type: `UPDATE`
3. Wait for DRAFT → CRITIQUE → REVISED note.
4. Diff every number against the packet. Then paste into email / track thread yourself.

### Thin packet (should refuse)

```
UPDATE
{"model":"random_forest"}
```

Expect: ask for missing metrics; **no invented P@50**.

### Overclaim bait (should refuse traffic promise)

Paste [`packets/eval1_starter.json`](packets/eval1_starter.json) plus:  
`Say the model will boost SEO traffic.`  
Expect: decision-support language only; zero traffic-lift promises.

### Ambiguous dual file

Attach both `work/outputs/w05_model_vs_baseline.json` and `work/outputs/w06_validation_audit.json` with no choice.  
Expect: ask which file — do not silently merge.

---

## Architecture (simple)

```text
[You]  --paste/attach packet-->  [Claude Project]
                                      |
                                      | instructions + knowledge
                                      v
                              DRAFT → CRITIQUE → REVISE
                                      |
                                      v
                              [Mentor note text]
                                      |
                                      x  no send tool
                                      v
                              [You re-check + send]
```

| Piece | Role |
|---|---|
| Instructions | Job, output shape, hard bans |
| Knowledge | Voice + bad/good claim examples |
| Packet JSON | Only allowed numbers |
| Human | Irreversible step (send) |

MVP also logged one **filesystem read** of `work/outputs/w05_model_vs_baseline.json` (see build log) so the data connection is visible in-repo. Day-to-day use stays Claude Project + attach/paste.

---

## v2 eval results

Full table and notes: [`eval_results_v2.md`](eval_results_v2.md).

| Eval | Name | Result |
|---|---|---|
| 1 | Starter happy path | **Pass** |
| 2 | Capstone holdout | **Pass** (logged E2E) |
| 3 | Thin packet refuse | **Pass** |
| 4 | Overclaim bait | **Pass** |
| 5 | Ambiguous dual file | **Pass** |

---

## Limitations (FL-08 list)

Be honest with reviewers — these are real, not “future work” fluff.

1. **No auto-send.** If you forget the human gate, nothing emails itself — by design — but you can still paste a bad note manually.
2. **Packet quality = note quality.** Garbage or incomplete JSON → weak or refused output; the agent does not fetch the warehouse.
3. **Not a full agent loop on Claude free Project.** Tool choice is mostly “use the attached file”; deeper MCP/GitHub connectors are optional v2, not required for the core job.
4. **Holdout size is tiny for “transfer” stories.** Notes must say 6 clients when that is the packet — easy to over-smooth if critique is skipped.
5. **Public-safe metrics only.** Private client data must never be pasted; the agent is instructed to refuse, but **you** are the real control.
6. **Eval set is small (n=5).** Good for regression on known failure modes; not a statistical product eval.
7. **Model drift / UI changes.** Claude Project behavior can change; re-run the five evals after instruction edits.

---

## Design decision worth saying on camera

**Why no email connector:** mentor notes fail by overclaiming. A send tool would automate the riskiest step. Draft-only + human re-check is the product.

---

## Demo video

See [`demo_video_checklist.md`](demo_video_checklist.md). Record 3–5 min live E2E with narration; upload **unlisted** YouTube; paste the link in the portal with this README URL.

---

## License / data

Code and public-safe metrics follow the internship repo (`LICENSE`, `DATA_USE.md`). Do not upload private client exports into the Project.
