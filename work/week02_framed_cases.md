# Framed cases — Week 2

**Voice card (standing instruction):** direct, plain, careful, specific, no buzzwords.

Paste into your Claude Project custom instructions:

> Voice: direct, plain, careful, specific, no buzzwords. Short sentences. No “passionate,” “results-driven,” “leveraged,” or “dynamic.” Prefer observed / directional / decision-support language. Use my words. If a line sounds like a generic AI bio, rewrite it the way I would say it to a friend.

---

## Proof statement (from this track)

I build ranking systems on messy search data and say what they can and cannot claim. I am proving this to a hiring manager who needs a useful decision-support prototype, not a flashy demo. The one action: email me to talk about an ML intern or junior role.

**Why this needs to exist:** a CV lists tools. This site shows a real triage problem, the decisions I made before training, and an honest result — including limits.

---

## Sitemap this document covers

| Page | Job |
|---|---|
| Home | Claim + one proof line + CTA |
| Work → Content refresh queue | Main internship case |
| Work → Frame before you model | Case: lane + ML task framing |
| About | Two-sentence bio |
| Contact | One-line CTA |

---

## Case 1 — Content refresh opportunity queue

*(Internship build · Lane 2 · starter dataset + ranked queue)*

### The problem

Editors cannot eyeball 30,000 pages a week. Flagging “everything trending down” dumps high-impression page-one URLs next to low-demand noise. Someone still has to decide what to refresh, expand, protect, prune, or monitor — and wrong tops waste hours or miss a visible page that is sliding.

### What I did (and decided)

I locked Lane 2: refresh / content opportunity scoring. Unit of analysis: one page. Output: a ranked review queue with a suggested action and short reason codes — not a black-box “score” alone.

I treated this as ranking / scoring, not classification for its own sake. Success metric: precision@K (K = 20 and 50), because editors only open the top of the list. I kept a transparent rule baseline first, then compared simple models. On the starter run, a random forest beat the rule baseline on precision@50 (0.74 vs 0.24). Top features that mattered in that run were things like days with impressions, log impressions, average position, and content age — signals an editor can argue with.

I also decided what I will not claim: a refresh will recover traffic, or that I am predicting Google’s algorithm. The queue is decision support. A human still verifies the page.

### What came of it

A ranked action mix on 30k pages (high / medium / low confidence bands, plus actions like refresh, monitor, refresh-and-review CTR). The top of the queue surfaces high-demand pages that look like triage candidates, with reasons attached. Next time I would replace the starter proxy label with an observed next-window decline from the warehouse, and log a hand review of the top 20 so the “does this make sense?” check is written down, not just felt.

**Repo:** https://github.com/haideriqbal499/Flyrank_Ml_internship

---

## Case 2 — Frame the question before the model

*(ML-02 / ML-03 · `w01_research_question.ipynb`, `w02_ml_task_framing.ipynb`)*

### The problem

It is easy to “train a model” and still not help the person who has to pick this week’s pages. Without a decision, an action, and a cost of being wrong, the notebook is homework, not a prototype.

### What I did (and decided)

I wrote the research question first: which pages should an SEO/content editor review first? Actor: the editor. Action: refresh, expand, protect, prune, or monitor. Cost of a wrong call: wasted editor time, or a high-visibility page that keeps sliding.

I backed the lane with numbers from the starter CSV — not vibes. In that snapshot, over half of pages trend down on impressions; among pages with ≥500 impressions / 90d, most still trend down; page-one URLs decline often too. That is a triage problem, not a niche edge case.

Then I mapped the lane onto the ML loop before training: ranking / scoring, a proxy target for the starter (`needs_refresh_review` from high demand + down trend), and an explicit note that `trend_direction` must not leak back in as a feature. Preferred later target: observed decline in a future window.

### What came of it

A filled framing notebook pair that a stranger can read and know what I am building, who acts on it, and what “good” means (precision@K + a human sense-check of the top 20). Next time I would lock the warehouse label path earlier so the proxy does not stick around longer than it should.

---

## Home copy (one screen)

**Headline:** I rank which pages to refresh when the inventory is too big to eyeball.

**Proof line:** Lane 2 on real FlyRank search data — ranked queue, reason codes, honest limits.

**CTA:** Email me if you want someone who starts with the decision, not the model.

---

## Bio (pick one)

**A.** I build ranking queues on messy search data for SEO and content teams. I care more about a useful top-20 than a pretty ROC curve.

**B.** I turn large content inventories into ranked review lists with reasons a human can check. Right now that work lives in my FlyRank ML internship.

**C.** I am an ML intern working on content-refresh prioritization. I write the decision and the failure cost before I train anything.

*(Recommended: A.)*

---

## Contact / CTA

Email me to talk about an ML intern or junior role — I can walk you through the queue and what I would not claim.

---

## Before / after (generic AI vs edited)

| Before (generic AI) | After (edited, my voice) |
|---|---|
| “Passionate, results-driven ML enthusiast leveraging cutting-edge models to deliver impactful, data-driven SEO insights.” | “I rank which pages an editor should refresh first when 30k URLs is too many to eyeball — and I say what the model cannot prove.” |

---

## Claude Project — paste this whole block as standing instructions

```
Voice card: direct, plain, careful, specific, no buzzwords.
Short sentences. No “passionate,” “results-driven,” “leveraged,” or “dynamic.”
Prefer: observed / directional / decision-support. Never invent metrics I did not give you.
Proof statement: I build ranking systems on messy search data and say what they can and cannot claim. Audience: a hiring manager who needs a useful prototype, not a demo. One action: email me to talk about an ML intern or junior role.
When you draft portfolio copy, use my words, keep the three beats (problem / what I did and decided / what came of it), and flag any guess so I can fix it.
```

---

## Self-check against pass criteria

- [x] Framed case for each sitemap work piece (refresh queue + framing before modeling), plus home / about / contact copy
- [x] Each case has the three beats and could only describe this Lane 2 project
- [x] Sounds specific; before/after shows the cut from generic AI sludge
- [x] One audience, one action; no filler adjectives
