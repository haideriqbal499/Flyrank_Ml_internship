# FL-04 MCP evidence log

**Client:** Cursor (MCP host)  
**Servers used:** `cursor-ide-browser`, `cursor-app-control`  
**Date:** 2026-07-24  
**Rule of thumb:** each task required a tool call; plain chat has no live DOM, no local editor open, and no live GitHub state.

## Setup

Cursor already exposes MCP servers to the agent. No separate Claude Desktop config was required for this card (“any MCP client counts”). Verified servers ready via MCP tool discovery (`GetMcpTools` catalog): both servers reported `serverStatus: ready`.

## Task 1 — Live portfolio page (browser MCP)

**Ask:** What is the live page title and H1 on the deployed site right now?  
**Why chat alone fails:** Training/memory can hallucinate old copy; only a live fetch/browse sees the current deploy.

| Step | MCP server | Tool | Result (public-safe) |
|---|---|---|---|
| 1 | `cursor-ide-browser` | `browser_navigate` → `https://haideriqbal499.github.io/Flyrank_Ml_internship/` | Loaded live site |
| 2 | `cursor-ide-browser` | `browser_take_screenshot` → `task1_live_portfolio.png` | Screenshot saved |

**Observed from tool output (not guessed):**
- Page title: `Haider Iqbal — ranking queues for content refresh`
- H1: `I rank which pages to refresh when the inventory is too big to eyeball.`

**Screenshot:** `evidence/task1_live_portfolio.png`

## Task 2 — Official MCP intro (browser MCP)

**Ask:** Open the live MCP introduction and capture the “USB-C” framing.  
**Why chat alone fails:** Need the live docs page as rendered today, with visual proof of tool use.

| Step | MCP server | Tool | Result |
|---|---|---|---|
| 1 | `cursor-ide-browser` | `browser_navigate` → `https://modelcontextprotocol.io/docs/getting-started/intro` | Page title: `What is the Model Context Protocol (MCP)?` |
| 2 | `cursor-ide-browser` | `browser_take_screenshot` → `task2_mcp_docs.png` | Screenshot saved |

**Screenshot:** `evidence/task2_mcp_docs.png`

## Task 3 — Local file + live GitHub (two MCP surfaces + live API)

**Ask:** Open the local FL mentor-workflow doc in the editor, and confirm the public repo’s live state.  
**Why chat alone fails:** Chat cannot open an IDE tab on disk or see current GitHub commit counts / metadata without tools.

| Step | MCP server / action | Tool / call | Result |
|---|---|---|---|
| 1 | `cursor-app-control` | `open_resource` → `file:///C:/Users/Windows%2011/Flyrank_Ml_internship/work/fl_workflow_mentor_update.md` | Editor opened the local markdown file |
| 2 | `cursor-ide-browser` | `browser_navigate` → `https://github.com/haideriqbal499/Flyrank_Ml_internship` | Live repo UI: `main`, **26 commits**, public |
| 3 | `cursor-ide-browser` | `browser_take_screenshot` → `task3_live_github_repo.png` | Screenshot saved |
| 4 | Host shell (REST) | `Invoke-RestMethod` → GitHub API | JSON written to evidence |

**API excerpt** (`evidence/task3_github_api.json`): public repo, `default_branch: main`, `language: Jupyter Notebook`, `pushed_at: 2026-07-23T15:23:49Z`.

**Screenshots / files:**
- `evidence/task3_live_github_repo.png`
- `evidence/task3_github_api.json`

## Pass check vs brief

| Criterion | Status |
|---|---|
| Explainer in own words, technically aligned with Anthropic + MCP docs | `explainer.md` |
| FL-04 classified as **workflow** (fixed A→B→C + human gate) | Yes |
| One concrete agent upgrade named | Metrics-file tools + model-directed loop before send |
| Connector demonstrably working (tool use, not plain chat) | Three MCP tool sequences above |
| Three tasks chat alone could not do | Live site, live docs, local file + live GitHub |

## Files in this folder

```
work/fl04_agents_mcp/
  explainer.md
  evidence_log.md          ← this file
  evidence/
    task1_live_portfolio.png
    task2_mcp_docs.png
    task3_live_github_repo.png
    task3_github_api.json
```
