# Week 7 — Survive the Crit

**Live URL:** https://haideriqbal499.github.io/Flyrank_Ml_internship/

**Proof statement (Chapter / Week 1):** I build ranking systems on messy search data and say what they can and cannot claim. Audience: a hiring manager who needs a useful prototype, not a flashy demo. One action: email me to talk about an ML intern or junior role.

**Reviewer:** structured peer review (AI Fluency track peer / mentor-style pass), Jul 2026.

---

## Two questions first

| Question | Reviewer answer |
|---|---|
| In ten seconds, what do I do? | You build ranked review queues that tell editors which pages to refresh first when they cannot eyeball tens of thousands of URLs. |
| Would you believe I am good at it? | **Before must-fixes:** claim was clear; skill was only half-believed — the home page named metrics but not a result. **After must-fixes:** yes — the main card now shows a concrete baseline lift (P@50 0.74 vs 0.24) and the limits stay visible. |

---

## Full feedback (collected without defending)

1. Hero H1 answers “what do you do” immediately. That part already passed the ten-second test.
2. “Lane 2” in the hero lede is internship jargon. A hiring manager should not need the program glossary to parse the first screen.
3. Work cards described method words (`precision@K`) without an outcome. Proof of skill did not land until a click into the case.
4. Case page itself is strong: problem / decisions / result / limits, charts legible, repo + notebook linked.
5. One action (email) is obvious and repeated. Good.
6. Mobile at 390px: no horizontal overflow on the live home page after the phone pass.
7. Nice later: runnable Colab one-click from the case; small chart thumbnail on the home card; richer About.

---

## Sort

### Must-fix (confusing / hurts the one action / proof does not land)

| Feedback | Why must-fix | Change on live site |
|---|---|---|
| Skill not proven on first screen | “Would you believe I’m good?” failed without opening a case | Main work card now states P@50 **0.74 vs 0.24** vs rule baseline (starter run) and keeps the honesty line |
| “Lane 2” in hero | Confuses a stranger in ten seconds | Hero lede rewritten without lane jargon; still names FlyRank + ranked queue + honest limits |
| Proof section restated the claim only | Did not point at evidence | “What I am proving” now points at the 30k-page queue, baseline comparison, reason codes, and limits |

### Nice-to-have (later)

- One-click Colab / runnable notebook from the case (ML-track “demo runs” polish)
- Chart thumbnail on the home work card
- Soften remaining “Lane 2” mentions inside case meta for non-intern readers
- About page depth (still fine at two beats)

---

## Evidence of must-fixes

1. Open live home: hero lede no longer leads with “Lane 2.”
2. Open Work → first card: concrete P@50 comparison visible without clicking through.
3. Scroll to “What I am proving”: claim + pointer to the evidence on this site.
4. Phone check still clean (see `docs/fix-log.md` + `docs/img/after-phone.png`).

**Deploy note:** after commit + push to `main`, wait ~1–2 minutes for GitHub Pages, then re-check the live URL before submitting the portal card.

---

## Ready-to-paste track reply

> **Survive the Crit — Week 7**
>
> Live: https://haideriqbal499.github.io/Flyrank_Ml_internship/
>
> **Proof statement:** I build ranking systems on messy search data and say what they can and cannot claim. Hiring manager who needs a useful prototype. One action: email me about an ML intern / junior role.
>
> **Ten-second answers from reviewer:** (1) I rank which pages editors should refresh when the inventory is too big to eyeball. (2) After fixes, yes — the home card shows P@50 0.74 vs rule 0.24 with honest limits.
>
> **Must-fix → fixed:** removed hero “Lane 2” jargon; put the baseline result on the home work card; pointed the proof section at that evidence.
>
> **Nice-to-have (parked):** Colab one-click, chart thumbnail on home, deeper About.
>
> Fix log (phone pass): https://haideriqbal499.github.io/Flyrank_Ml_internship/fix-log.md
