# AI stack mastery — day-to-day

Written proof of how this internship is run on a free stack. Not a product pitch.

## Daily loop

1. Open this repo in **Cursor** (or VS Code). One assignment = one fresh chat.
2. Tell the assistant: read `skills/README.md`, then load the **one** skill for this card.
3. Search the repo before writing code. Interview before multi-step plans.
4. Do the work in `work/` (notebooks under `work/notebooks/`). Leave `scripts/` alone unless you are copying a pattern.
5. Run the notebook **top to bottom**. Read the output. Commit when a section is done.
6. Cross-check hard claims with a second free model when it matters (Claude Free / ChatGPT Free / Gemini).

## Where each piece lives

| Need | Tool | In this repo |
|---|---|---|
| Editor + agent | Cursor Hobby / VS Code | `.cursor/rules/ai-stack.mdc` always on |
| Task instructions | Skills | `skills/README.md` → one `SKILL.md` |
| Notebooks | Local Jupyter or Colab | Badges in `README.md` / case pages |
| Version control | GitHub Free | This public repo is the portfolio |
| Public site | GitHub Pages (`/docs`) | https://haideriqbal499.github.io/Flyrank_Ml_internship/ |
| Brand / employer copy | Personal agent skill | `skills/personal-agent/SKILL.md` |
| Free tool map | Intern guide | `docs/intern-free-tooling-guide.md` |

## What “done” looks like for stack mastery

- [x] Always-on Cursor rule points at the skills router and data safety
- [x] Personal agent skill exists for portfolio voice work
- [x] Live site is the public brand surface (GitHub Pages from `docs/`)
- [ ] Each new assignment: one chat, one skill, notebook Run all, then commit

## Safety (non-negotiable)

- Approved / anonymized internship data only in external AI tools
- No client names, raw queries, or private warehouse details in chats or on the site
- Never commit CSVs under `data/` — CI fails the PR if you do
