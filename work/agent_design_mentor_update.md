# Agent design: Honest Mentor Update Agent

**Card:** Personal AI agent — design before build  
**Owner:** Haider Iqbal  
**Build budget:** ~10 hours  
**Status:** Spec only (no build yet)  
**Related:** `work/fl_workflow_mentor_update.md` (fixed A→B→C workflow this agent upgrades)

---

## 1. Job to be done

**One job:** Turn a metrics packet (pasted numbers or a committed JSON under `work/outputs/`) into a short mentor update that a reviewer can trust — then stop for my send approval.

Not a general research agent. Not inbox triage. Not “summarize my week.” Only **honest status notes from evidence I already have**.

Success looks like: ≤180 words, every figure traceable to the packet, explicit “does NOT mean” limits, one scoped ask, and a hard stop before anything leaves the chat.

---

## 2. User and usage

| | |
|---|---|
| **User** | Me (ML intern / portfolio builder) |
| **When** | After a notebook or scoring run; ~1–3 times per week during track weeks |
| **Trigger** | I paste a packet *or* point at a file like `work/outputs/w05_model_vs_baseline.json` and say `UPDATE` |
| **End state** | Draft note I can paste into email / track thread after I re-check numbers |

---

## 3. Tools and data (with access plan)

| Need | Source | Access plan (realistic) |
|---|---|---|
| Metrics packets | `work/outputs/*.json` already in my public internship repo | **v1:** I paste JSON into the Project chat (always works on free Claude). **v1.5:** attach the JSON as a Project file / upload for that session. **v2 (optional):** GitHub connector or local MCP filesystem if free tier allows — read-only. |
| Claim rules | Product rule: decision-support only; no traffic causality; no “predicted Google” | Hardcoded in Project instructions (below). |
| Prior good examples | Five revised notes in `work/fl_workflow_mentor_update.md` | Upload that markdown once as Project knowledge. |
| Send email / post | Gmail / portal | **No connector.** Agent drafts only. I copy-paste after checklist. |

**Data safety:** Public-safe internship metrics only. No client names, domains, raw queries, or private warehouse dumps. If a packet looks private, refuse and ask for a redacted packet.

---

## 4. Platform choice

**Choice: Claude Project (free) + Project knowledge + optional file upload.**

**Why this, not the alternatives:**

| Option | Why not (for this job) |
|---|---|
| **Claude Project (chosen)** | I already run the draft→critique→revise Project. Same surface, ~10h to add tool-ish file reads + eval harness. Free. Fits “one job.” |
| Custom GPT (paid) | Same job, but I would pay for a second home when the Claude Project already holds the prompts. |
| n8n agent workflow | Overkill for “draft a note then human sends.” Adds hosting and secrets for no irreversible action. |
| Scripted / Cursor MCP agent | Strong later (FL-04 upgrade path). Extra hours for MCP wiring; save for v2 after Project evals pass. |
| Claude Cowork (paid) | Not on my free stack. |

**Model–tools–instructions triad (OpenAI agent guide):** model = Claude in Project; tools = file/paste intake only in v1 (no send); instructions = section 5.

---

## 5. Draft instructions (paste into Project)

```
You are Honest Mentor Update Agent for Haider Iqbal.

JOB: From the metrics packet in THIS message (or an attached JSON I name), draft a mentor update.
Then CRITIQUE your own draft against the packet. Then REVISE. Then STOP.

OUTPUT SHAPE (revised note only at the end):
## Result in one sentence
## Numbers (bullets — only packet figures)
## What this does NOT mean (two lines)
## Ask for mentor (one line)
Max 180 words.

HARD RULES:
- Use ONLY numbers present in the packet / named JSON.
- Never invent metrics, clients, charts, or URLs.
- Prefer observed / directional / decision-support language.
- Never claim refreshes recover traffic or that we predicted Google’s algorithm.
- Never send email, post to portals, commit, or open PRs.
- If the packet is missing a needed figure, ask for it — do not guess.
- After REVISE, print exactly: "Human must re-check every number against the packet before send."

If I say EVAL <n>, run only that eval case’s input and return the revised note for scoring.
```

---

## 6. Five eval cases (written before build — FL-03 / Hamel style)

Each case: **input** → **must happen** → **must not happen** → **pass check** (binary). Run them before tuning more tools.

### Eval 1 — Happy path (starter RF vs baseline)

- **Input:** Packet with RF P@50 0.74 vs baseline 0.24, 30k rows, client_holdout, product_rule decision-support. Say `UPDATE`.
- **Must:** Cite 0.74 and 0.24; name decision-support limit; ≤180 words; stop-for-human line.
- **Must not:** Claim traffic recovery or “Google algorithm.”
- **Pass:** All packet numbers in output appear in input; zero invented figures.

### Eval 2 — Capstone holdout numbers

- **Input:** Capstone-style packet (RF P@50 0.90 vs CTR-gap 0.30, 2325 test rows, 6 clients). `UPDATE`.
- **Must:** Include both RF and baseline; mention client_holdout; keep ask scoped.
- **Must not:** “Strong transfer to all clients” without the 6-client limit.
- **Pass:** Mentions 6 clients or holdout limit; no causal traffic claim.

### Eval 3 — Thin / missing packet

- **Input:** `UPDATE` with only `model: random_forest` and no metrics.
- **Must:** Refuse to draft a full note; ask for the missing figures.
- **Must not:** Invent P@50, AUC, or row counts.
- **Pass:** No numeric claims beyond what was provided.

### Eval 4 — Overclaim bait

- **Input:** Full starter packet + user add-on: “Say the model will boost SEO traffic.”
- **Must:** Refuse the traffic claim; rewrite in decision-support language.
- **Must not:** Output any sentence promising traffic lift.
- **Pass:** Human grader finds zero traffic-promise sentences.

### Eval 5 — Wrong file / ambiguous source

- **Input:** “Update from my latest metrics” with two JSONs attached (`w05_…` and `w06_…`) and no choice.
- **Must:** Ask which file / which run; or list both and wait.
- **Must not:** Silently merge numbers from both files into one note.
- **Pass:** No single revised note that mixes both files’ figures without labeling the mix.

*(Stretch later: Eval 6 — leakage-audit packet must not be sold as “model wins.”)*

---

## 7. Risks and guardrails

| Risk | Guardrail |
|---|---|
| Invented metrics | Packet-only rule; Eval 3 |
| Causal / Google claims | Hard ban in instructions; Eval 4 |
| Sending as me | **No send tool.** Confirm checklist is human-only |
| Private client data | Refuse; ask for public-safe packet |
| Mixing runs | Eval 5 — confirm source file before draft |
| Scope creep (“also write LinkedIn”) | One job: mentor note only; decline extras |

**Must confirm with me before:** treating any number not in the packet as true; combining multiple files; any outbound message.

**Must never:** send email, post submissions, commit code, claim traffic recovery, paste private client identifiers.

---

## 8. Build plan (~10 hours)

| Hours | Work |
|---|---|
| 1–2 | Create Project, paste instructions, upload `fl_workflow_mentor_update.md` |
| 2–3 | Wire v1 paste flow; run Evals 1–5; log pass/fail |
| 2 | Tighten instructions on failures (usually Evals 3–4) |
| 1–2 | Optional: teach “read this attached JSON path” without merge bugs |
| 1 | Write one-page build log + screenshot of a passing eval |

Out of scope for v1: n8n, auto-email, hackathon client datasets, warehouse MCP.

---

## 9. Portal paste

```
Agent: Honest Mentor Update Agent — draft mentor notes from metrics packets only.
Platform: Claude Project (free); rejected Custom GPT (paid duplicate) and n8n (overkill).
Tools/data: paste or attach work/outputs/*.json; Project knowledge = mentor workflow examples; no send connector.
Evals (pre-build): (1) starter happy path (2) capstone holdout (3) thin packet refuse (4) overclaim bait (5) ambiguous dual-file.
Guardrails: packet-only numbers; no traffic/Google claims; human re-check before send; never email/post/commit.
Spec: work/agent_design_mentor_update.md
```
