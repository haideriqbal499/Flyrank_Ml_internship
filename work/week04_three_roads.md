# Week 4 — Three roads: choose the stack

**Track card:** [Three Roads](https://aifluency.flyrank.ai/week-04.html#three-roads)  
**Related:** `work/week04_empty_but_live.md` (live URL on the stack I chose)

---

## Four constraints I gave (and kept)

| Constraint | My answer |
|---|---|
| Budget | Free only — no paid builder, no paid host |
| Skill level | Honest beginner at web shipping; comfortable editing HTML/CSS with AI help; already use GitHub for the ML internship |
| What the site must do | Four-page path from Week 1/3: Home (claim) → Work proof → About → Contact. One action: email me about an ML intern / junior role. Sitemap + content map: `work/week01_draw_the_path.md`, `work/week03_through_line.md` |
| How work must be shown | **Code repo** (public GitHub) + **embedded / one-click notebook** (Colab badges) + **long-form cases** (three beats) + **real chart SVGs** — not a photo gallery portfolio |
| Dynamic yet? | **No.** Mailto is enough. No contact-form backend, no auth, no database at launch |

---

## Three stack options (simplest → most powerful)

### Option A — No-code builder (Carrd / Framer free tier)

| | |
|---|---|
| Build | Drag-and-drop pages in the builder |
| Host | Builder’s free publish URL |
| Backend | Not yet (unless I add their form later) |
| Shows my work? | Fine for text; weak for “open the repo / Colab / paper HTML” as first-class proof |
| Trade-off | Fastest to a pretty page; the **repo is no longer the site**. Harder to prove I can ship code. Vendor lock-in if I outgrow the free tier |

### Option B — Plain HTML/CSS + free static host (front-runner)

| | |
|---|---|
| Build | Hand-edited (with AI) HTML/CSS in a folder |
| Host | **GitHub Pages** from this repo (`docs/`) — or Netlify/Cloudflare Pages if I dragged a folder |
| Backend | **Not yet** — static files only |
| Shows my work? | Best fit: same repo as the internship, Colab links, paper page, SVG charts, fix-log screenshots |
| Trade-off | I must touch files and push. No visual CMS. In return: free forever, fully mine, maintainable in Cursor |

### Option C — Framework (Next.js / React on Vercel)

| | |
|---|---|
| Build | Component app, build step, deploys on push |
| Host | Vercel Hobby (free) |
| Backend | Not required for a static portfolio — but the *tooling* acts like one |
| Shows my work? | Can show the same content, but the stack itself becomes the story |
| Trade-off | Most “powerful,” most to maintain: node, builds, routing. Easy to burn two weeks on tooling instead of the claim |

---

## Pressure-test the front-runner (Option B)

| Question | Answer |
|---|---|
| What breaks if I pick the simplest (A)? | Hiring manager sees a pretty Carrd and still has to hunt for GitHub. My ML proof (repo + Colab + paper) feels bolted on. |
| What do I maintain if I pick the most powerful (C)? | Dependencies, build failures, framework upgrades — for four static pages. I cannot honestly say I need that. |
| Can I finish in two weeks? | B is already live. A would mean rebuilding. C would risk the deadline. |
| Does it show my work the way it needs to be shown? | Yes: ranked-queue charts, paper, notebooks, and the repo are native to Pages-from-`docs/`. |

---

## Decision (my words)

**I chose Option B: plain HTML and CSS in `docs/`, hosted on GitHub Pages from this public repo. Backend: not yet.**

I did **not** choose Carrd/Framer. It would look finished faster, but my proof is not a mood board — it is a ranked queue with numbers, a paper, and a repo a stranger can open. A no-code site would hide the shipping evidence.

I did **not** choose a React/Next framework. It is more than I need. I would maintain a build pipeline instead of the claim. Finish beats fancy.

**Can I maintain this?** Yes. Edit an HTML file, push `main`, Pages updates. Same habit as the internship notebooks. No paid plan to renew.

**Does it show my work well?** Yes. Home leads with the claim; Work leads with the paper and queue charts; Colab and GitHub sit next to the cases; Contact is still just email.

**Live on this stack:** https://haideriqbal499.github.io/Flyrank_Ml_internship/

---

## Pass check

| Criterion | Hit |
|---|---|
| Three options with trade-offs | A / B / C above |
| Free + matched to needs | Pages + static HTML |
| Own-words rationale + maintain | Decision section |
| Backend honest | Not yet |

---

## Paste for track thread

I gave AI four constraints: free only; beginner at web shipping but fine editing HTML with help; a four-page map that ends in Email me; work shown as repo + Colab + long-form cases + real chart SVGs; nothing dynamic yet.

Three roads: (A) Carrd/Framer — fast, weak as code proof; (B) plain HTML/CSS on GitHub Pages — mine, free, shows notebooks/repo; (C) Next/Vercel — powerful, too much to maintain for four pages.

I chose B. I can maintain it by editing `docs/` and pushing. It shows my ranked-queue work the way a hiring manager needs to see it. Backend: not yet. Live: https://haideriqbal499.github.io/Flyrank_Ml_internship/
