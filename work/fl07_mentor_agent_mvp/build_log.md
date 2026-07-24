# Build log — Honest Mentor Update Agent (FL-07 Checkpoint 1)

**Spec:** `work/agent_design_mentor_update.md` (FL-06)  
**MVP folder:** `work/fl07_mentor_agent_mvp/`  
**Goal:** one end-to-end core job + one live data connection + honest iteration notes

---

## Timeline (what actually happened)

### 1. Started from the FL-06 spec, then cut

**Kept**
- One job: metrics → honest mentor note → human send gate
- Draft → critique → revise → stop
- Packet-only numbers; no send tool
- Eval 2 (capstone holdout) as the primary E2E
- Eval 3 (thin packet) as a smoke refuse test

**Cut from v1 (and why)**
| Cut | Why |
|---|---|
| Full Eval 1/4/5 battery in the MVP capture | Spec said get **one** full loop working first; extra evals are next checkpoint |
| Claude Cowork / n8n / Custom GPT | Already rejected in FL-06; still out of budget |
| Auto-email / portal post | Guardrail: irreversible |
| GitHub connector | Spec v2 optional; paste + file read is enough for Checkpoint 1 |
| Uploading entire `fl_workflow_mentor_update.md` into the first run | Too long; replaced with short `knowledge/voice_and_limits.md` excerpt |

### 2. What broke / what we changed

1. **Broken assumption:** “Claude Project alone” would show a *tool call* in the repo evidence. Project file-upload is a live data connection for day-to-day use, but reviewers cannot see that from GitHub.  
   **Change:** Run the same instructions against a **live filesystem read** of `work/outputs/w05_model_vs_baseline.json`, log the tool-backed packet in `packets/live_w05_packet.json`, and keep the Claude Project pack for Haider’s daily use. Documented as a platform **deviation**, not a silent swap.

2. **Broken assumption:** Dumping the full comparison JSON into the note would stay under 180 words.  
   **Change:** Extract a slim packet (split, rows, clients, three P@50s, AUC, top-4 features, claim) before UPDATE.

3. **Critique pass found a real miss:** first draft implied “usable” without stressing **6 clients**.  
   **Change:** Revised note names holdout size in the result / limits lines (matches Eval 2 must-clause).

### 3. Live tool / data connection used

| Connection | How |
|---|---|
| **Primary for MVP proof** | Read `work/outputs/w05_model_vs_baseline.json` (committed internship metrics) → agent packet |
| **Declared platform (FL-06)** | Claude Project: paste `PROJECT_INSTRUCTIONS.md` + upload `knowledge/voice_and_limits.md` + attach JSON |

No mid-run hand-editing of the revised note numbers.

### 4. Deviation summary (vs FL-06)

| Spec said | MVP did | Reason |
|---|---|---|
| Claude Project as the run surface | Project pack shipped **and** one Cursor/filesystem E2E logged | Need visible tool/file proof in the repo; Project still the daily home |
| Optional GitHub/MCP later | Not built | Out of Checkpoint 1 scope |
| Five evals before tuning | Eval 2 full + Eval 3 smoke | Narrowest path to one working loop |

### 5. Still not done (intentionally)

- Haider’s **raw ~2 min screen capture** of the Claude Project run (must be recorded on his machine — see `capture_checklist.md`)
- Eval 1, 4, 5 formal scoring table
- MCP filesystem server on Claude Desktop

---

## Files shipped this checkpoint

```
work/fl07_mentor_agent_mvp/
  PROJECT_INSTRUCTIONS.md
  knowledge/voice_and_limits.md
  packets/eval1_starter.json
  packets/live_w05_packet.json
  run_e2e_transcript.md
  build_log.md              ← this file
  capture_checklist.md
```

---

## Portal paste (after you attach the screen capture)

```
FL-07 Checkpoint 1 — Honest Mentor Update Agent MVP.
Core job: UPDATE on live work/outputs/w05_model_vs_baseline.json → draft/critique/revise mentor note → human gate.
Live data: filesystem read of committed metrics JSON (packet in work/fl07_mentor_agent_mvp/packets/).
Platform: Claude Project instructions pack + documented Cursor file-read E2E (deviation logged).
Build log: work/fl07_mentor_agent_mvp/build_log.md
E2E transcript: work/fl07_mentor_agent_mvp/run_e2e_transcript.md
Screen capture: [attach raw ~2 min recording of Project run — see capture_checklist.md]
```
