# Week 3 — The through-line (claim + content map)

**Track card:** [The Through-Line](https://aifluency.flyrank.ai/week-03.html#the-through-line)  
**Week 1 one action:** email `haideriqbal499@gmail.com` about an ML intern / junior role  
**Live site:** https://haideriqbal499.github.io/Flyrank_Ml_internship/

---

## Ten one-line claim options (AI draft → I choose)

1. I build ranked content-refresh queues on messy search data.
2. I rank which pages to refresh when the inventory is too big to eyeball.
3. I turn 30k-page inventories into a short editor review list with reasons.
4. I score which pages deserve a human look first — and I say what the score does not prove.
5. I ship decision-support ranking for SEO content triage, not demo metrics.
6. I compare a learned ranker to a transparent rule baseline and keep the limits honest.
7. I help hiring managers see I can prioritize refresh work under real data mess.
8. I build prototypes that tell an editor where to start, not what Google will do next.
9. I prove I can rank messy search pages for refresh review with precision@K and claimed limits.
10. I make the top of a content queue useful when “everything is declining” is useless.

### Chosen (sharpened)

**I rank which pages to refresh when the inventory is too big to eyeball.**

**Why this one:** One breath, one verb (*rank*), one stuck person (editors / hiring manager who needs that skill). Options 1 and 9 were accurate but heavier; 5–7 sounded like pitch decks. This matches the live Home H1 and still implies the honest-limits habit without stuffing “and.”

---

## Content map

*Core path (Week 1): Home → Work proof → About → Contact. Paper and framing cases are proof depth, not equal top-level destinations.*

### Home — `index.html`

| Order | Section | What sits here | CTA (named) | Sends visitor to |
|---|---|---|---|---|
| 1 | Nav | Brand · Work · About · Email | **Email me** | Contact / mailto |
| 2 | Hero | One-line claim + one proof lede | **Email me** (primary) · See the proof (secondary → Work/paper) | mailto / `#work` or paper |
| 3 | Work | Case cards — **strongest first** (below) | Per-card: Open the paper / Read the case | Paper or case page |
| 4 | What I am proving | Claim restated + one action | **Email me** (in copy) | mailto / Contact |
| 5 | Footer | Email · Repo · Fix-log | Email / Repo | mailto / GitHub |

**Case order on Home (lead with strongest):**

1. **Research paper** — client-holdout Precision@50 0.90 vs 0.30 (strongest numbers) → `paper/`
2. **Content refresh queue** — 30k ranked list, starter P@50 0.74 vs 0.24 → `work/refresh-queue.html`
3. **Frame before you model** — decision/cost before training (supports the claim; does not lead) → `work/frame-before-model.html`

### Work · Paper — `paper/index.html`

| Order | Section | CTA |
|---|---|---|
| 1 | Abstract / claim | Continue reading |
| 2 | Method + figures (real SVGs) | — |
| 3 | Results + limits | — |
| 4 | Close | **Email me** · Repo |

### Work · Refresh queue — `work/refresh-queue.html`

| Order | Section | CTA |
|---|---|---|
| 1 | Problem | — |
| 2 | What I did (and decided) | — |
| 3 | Figures (action mix, features) | — |
| 4 | What came of it + limits | Colab / Repo |
| 5 | Footer | **Email me** · Contact |

### Work · Frame before model — `work/frame-before-model.html`

| Order | Section | CTA |
|---|---|---|
| 1–3 | Three beats | Repo / notebooks |
| Close | — | **Email me** · Contact |

### About — `about.html`

| Order | Section | CTA |
|---|---|---|
| 1 | Short bio (same claim) | — |
| 2 | What you can check on this site | — |
| 3 | — | **Email me about a role** → Contact |

### Contact — `contact.html`

| Order | Section | CTA |
|---|---|---|
| 1 | One ask | **Email me** (the Week 1 action — stop here) |

### CTA ladder (everything → Week 1 action)

```text
See the proof (paper/case)
        ↓
Believe the claim (numbers + limits)
        ↓
About (who emailed you)
        ↓
Email me  ←── one action
```

Secondary CTAs (Open paper, Read case, Repo, Colab) only exist to make **Email me** credible. None compete as a second “hire me for X.”

---

## Still need to gather (honest)

| Item | Status | Blocks build? |
|---|---|---|
| Live portfolio URL | Have — GitHub Pages | No |
| Public repo | Have | No |
| Colab / notebook links | Have on cases | No |
| Real chart SVGs (model vs baseline, features, action mix, reason codes) | Have | No |
| Phone before/after screenshots | Have (`docs/img/*-phone.png`) | No |
| Identity kit (fonts, hex, logo/favicon) | Have | No |
| Custom domain (if track requires later) | Not set | Only if Week 10 domain gate applies |
| Graduate / showcase badge in footer | Not installed | Capstone week, not this map |
| Warehouse next-window decline label + top-20 hand-review case | Named next piece — not shipped | Does not block this map; blocks “next case” only (`work/week10_next_case_habit.md`) |
| Written top-20 hand-review log | Not done | Same as above |
| Testimonial from a mentor/hiring manager | None | Nice-to-have; do not invent |
| Real headshot on About | Intentionally omitted | Only if we add a face later (real photo only) |
| Hero primary CTA swap (Email primary, paper secondary) | Map says yes; live hero still leads with paper | Small copy/HTML fix — not blocked on assets |

---

## Pass check

| Criterion | Hit |
|---|---|
| Single memorable claim | One sentence above — not a paragraph |
| Every page: ordered sections + named CTA | Tables above |
| Strongest work leads | Paper first on Home Work grid |
| CTAs ladder to Week 1 Email me | Ladder diagram |
| Gather-list honest | Unfinished warehouse case + badge + optional testimonial named |

---

## Paste for track thread

**One-line claim:** I rank which pages to refresh when the inventory is too big to eyeball.

**Map:** Home (claim → Work cards: paper, refresh queue, framing → proof line → Email) · Paper/cases (three beats + Email) · About (bio → Email) · Contact (Email only). Strongest lead = research paper.

**Still gather:** warehouse-label + top-20 hand-review case (next); showcase badge; optional testimonial; optional custom domain. Not blocking this map: repo, Colab, chart SVGs, phone shots already live.
