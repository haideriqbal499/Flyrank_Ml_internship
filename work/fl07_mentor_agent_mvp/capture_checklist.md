# Screen capture checklist (you record this)

The portal wants a **raw, unedited ~2 minute** capture of a successful end-to-end run. AI cannot fake that for you. Do this once the Project is set up.

## Setup (once, ~10 min)

1. Open [claude.ai](https://claude.ai) → Projects → New project.  
   Name: `Honest Mentor Update Agent`.
2. Paste everything inside the code fence from `PROJECT_INSTRUCTIONS.md` into Project instructions.
3. Upload `knowledge/voice_and_limits.md` as Project knowledge.
4. Start a new Project chat.

## What to record (~2 min, one take, no edits)

1. Start screen recording (Windows: Win+G, or phone filming the laptop).
2. In the Project chat, attach `packets/live_w05_packet.json` **or** paste its contents.
3. Type exactly: `UPDATE`
4. Wait until the agent finishes DRAFT → CRITIQUE → REVISED note and prints:  
   `Human must re-check every number against the packet before send.`
5. Scroll so the revised note is visible.
6. Stop recording. Do **not** cut, speed up, or overlay text.

## Upload

- Portal **Files:** the raw video / screen recording  
- Portal **Deliverable links:**  
  `https://github.com/haideriqbal499/Flyrank_Ml_internship/blob/main/work/fl07_mentor_agent_mvp/run_e2e_transcript.md`  
  `https://github.com/haideriqbal499/Flyrank_Ml_internship/blob/main/work/fl07_mentor_agent_mvp/build_log.md`

## Sanity check before you hit Save

- [ ] Capture shows request → result with no mid-run paste of a finished note by you
- [ ] JSON / packet visible as the data source
- [ ] Revised note cites 0.9 / 0.3 (or whatever is in the packet you attached)
- [ ] Stop-for-human line visible
