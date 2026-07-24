# Week 5 — Ship the ugly version

**Track card:** [Ship Ugly, Ship Live](https://www.aifluency.flyrank.ai/week-05.html)  
**Live URL:** https://haideriqbal499.github.io/Flyrank_Ml_internship/

---

## How the site is built (no mystery code)

| Piece | What it is |
|---|---|
| Files | Plain HTML pages + one shared `docs/styles.css` |
| Host | GitHub Pages: `main` branch → `/docs` folder |
| Look | Fraunces (headings) + Source Sans 3 (body); cream `#f4f1ea`, text `#14201a`, accent `#0b5f45` from the Week 3 identity kit |
| Cases | Real copy + chart SVGs from the internship notebooks — not placeholders |
| Update loop | Edit a file under `docs/` → commit → push `main` → wait ~1–2 min → hard-refresh the live URL |

Each page is the same shape: header (brand + Work + About + Email me) → main content → footer. Relative links (`../styles.css`, `work/refresh-queue.html`) keep Pages happy. No React, no backend, no build step.

---

## Sitemap reachability (verified 2026-07-24)

Core map from Week 1: Home · Work · About · Contact. Paper + two cases hang off Work.

| Page | Live URL | HTTP |
|---|---|---|
| Home | https://haideriqbal499.github.io/Flyrank_Ml_internship/ | 200 |
| About | …/about.html | 200 |
| Contact | …/contact.html | 200 |
| Work: refresh queue | …/work/refresh-queue.html | 200 |
| Work: frame before model | …/work/frame-before-model.html | 200 |
| Research paper | …/paper/ | 200 |

Nav: Work → `#work` / `index.html#work`; Email me → `contact.html`; every case opens from the Work cards.

**Assembly note this week:** hero primary CTA is now **Email me** (solid), paper is secondary (ghost) — matches the Week 1 pressure-test change. Not a redesign; finishes the sitemap intent.

---

## One real person’s reaction

**Status:** needs you — AI cannot send your link for you.

**Do this today (5 minutes):**

1. Text or email someone in SEO / content / applied ML (or a peer who hires / reviews portfolios).
2. Paste only:

```
Could you open this and tell me in 2–3 lines what you think I do, what confused you, and whether you’d email me from it?
https://haideriqbal499.github.io/Flyrank_Ml_internship/
```

3. Paste their reply into the blanks below (or into portal Notes). Honest confusion counts as success.

| Field | Fill in after they reply |
|---|---|
| Who (role / relation — no need for full name on a public paste) | |
| Channel (text / email / DM) | |
| What they saw / said I do | |
| What confused them | |
| Did the work land? (yes / partial / no + one line) | |

---

## Still ugly (honest list)

Things I already know are rough — not a fail list, a fix list for later weeks:

1. **Hero still reads dense** — claim + FlyRank + audience in one block; a stranger may skim past the one action.
2. **Frame-before-model card has no chart thumb** on Home (paper and refresh queue do).
3. **Three Work cards compete** — paper + two cases; Week 1 wanted one proof path; depth pages are good, equal weight on Home is noisy.
4. **Paper page nav adds “Paper”** as a top-level item; core map was Home / Work / About / Contact.
5. **About mentions “Lane” internship framing** in spirit via ML jargon (“precision@K”, “ROC”) that a non-ML hiring manager might bounce on.
6. **No dedicated phone polish pass this week** — cream/green is fine; spacing and card cutoffs on small screens are untested beyond “it loads.”
7. **Footer “Week 7 fix log”** is internship-insider; a stranger may not care.
8. **Identity-kit page exists** but is not in the hiring path (fine) — easy to confuse with a public page if linked accidentally.

Ship now. Polish against this list later.

---

## Portal paste

### Deliverable links (one per line)

```
https://haideriqbal499.github.io/Flyrank_Ml_internship/
https://haideriqbal499.github.io/Flyrank_Ml_internship/about.html
https://haideriqbal499.github.io/Flyrank_Ml_internship/contact.html
https://haideriqbal499.github.io/Flyrank_Ml_internship/work/refresh-queue.html
https://haideriqbal499.github.io/Flyrank_Ml_internship/work/frame-before-model.html
https://haideriqbal499.github.io/Flyrank_Ml_internship/paper/
```

### Notes (fill reaction, then paste)

```
Week 5 — ship ugly.
Live: https://haideriqbal499.github.io/Flyrank_Ml_internship/
Stack: plain HTML/CSS in docs/ → GitHub Pages.
All sitemap pages return 200; cases + paper open from Work; real charts/copy (no placeholders).
Hero CTA fixed to Email me primary (Week 1 sitemap intent).
Real person: [name/role] via [channel] — saw: […] · confused by: […] · landed: [yes/partial/no].
Still ugly: dense hero; frame case missing thumb; three Work cards compete; paper nav extra; About a bit jargon-y; phone spacing untested; Week 7 footer insider; identity-kit off-path.
Doc: work/week05_ship_ugly.md
```

---

## Pass check

| Criterion | Status |
|---|---|
| Live URL, every sitemap page reachable | Done — table above |
| Real work / cases / look / images in | Done — no placeholders |
| Real person opened it; reaction captured | **You — send link, fill table** |
| Can explain how it is built | Done — section above |
| Honest still-ugly list | Done — eight items |
