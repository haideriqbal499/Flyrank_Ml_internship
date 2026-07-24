# Workflows, agents, and MCP — what FL-04 actually is

**Sources:** Anthropic *Building Effective Agents*; MCP intro + server concepts  
**Pipeline reviewed:** mentor-update draft → critique → revise (`work/fl_workflow_mentor_update.md`)  
**MCP client:** Cursor (`cursor-ide-browser`, `cursor-app-control`)

---

Most AI products call themselves “agents.” That word is doing marketing work, not engineering work. Anthropic’s useful cut is simpler: a **workflow** is an LLM (and maybe tools) run along a path you already chose; an **agent** is an LLM that chooses the path itself — which tools to call, in what order, and when to stop — while it works.

A workflow is orchestration you design up front. Prompt chaining, routing, and evaluator–optimizer loops are workflows: you decide the stages, the handoffs, and the gates. The model does hard reasoning *inside* each stage, but it does not invent the stage list. An agent is different. You give it a goal and a toolbelt. It plans, acts, reads the environment (tool results, errors, files), and decides the next move. Autonomy is the point — and so are the costs: more latency, more spend, and errors that can compound if you skip guardrails.

That distinction matters when you evaluate a product. Same three prompts every time is a workflow — even if the UI says “Agent.” Searching, editing files, or asking a clarifying question because tools returned a conflict is closer to an agent. Start simple. Add autonomy only when a fixed path is not enough.

## My FL-04 pipeline is a workflow

My FL-04 build is the mentor-update chain: gather a metrics packet → DRAFT → CRITIQUE → REVISE → human check → send. The tooling is a Claude Project with fixed prompts A, B, and C. Every run follows the same sequence. The model never decides to skip critique, open a notebook, or query GitHub mid-flight. I paste only packet numbers; it cannot invent metrics; I still re-check every figure before send.

By Anthropic’s definition, that is a **workflow** — prompt chaining with a human gate, close to their evaluator–optimizer pattern. It is agentic in the loose sense that LLMs are doing the writing. It is **not** an agent: control of the process stays with me and the Project instructions, not with a model that dynamically directs tool use.

That is a feature, not a failure. Mentor notes fail by overclaiming. A fixed path plus a human gate is the right complexity for this chore. An agent that invents experiments or fetches private client context would be the wrong upgrade.

## What MCP is (and the three primitives)

Chat alone is stuck in the box: whatever you pasted, plus training data. The **Model Context Protocol (MCP)** is the open standard that lets an AI client plug into external systems the way USB-C plugs into devices. The host (Claude Desktop, Cursor, VS Code, and others) connects to an MCP server. The server exposes capabilities; the model can use them with permission.

MCP servers expose three core primitives:

1. **Tools** — actions the model can invoke: read a file, call an API, open a browser page. Model-controlled, usually with user approval.
2. **Resources** — read-only context the app can attach: schemas, docs, file contents. Application-driven context, not “do something.”
3. **Prompts** — reusable templates the user picks that structure how tools and resources should be used for a common job.

Tools change the world or query it. Resources fill the context window with ground truth. Prompts package good recipes. Together they turn “chat that guesses” into “chat that can check.”

I used Cursor as the MCP client with the built-in browser and app-control servers. Plain chat could not have done these three tasks without tool calls:

1. **Live portfolio** — `browser_navigate` + screenshot on the deployed GitHub Pages site; tool output returned the live title and H1.
2. **Live MCP docs** — same browser MCP on the official intro page, capturing the USB-C framing as rendered today.
3. **Local file + live GitHub** — `open_resource` opened `work/fl_workflow_mentor_update.md` in the editor; browser MCP plus a live API fetch confirmed the public repo state.

Screenshots and API JSON are in `work/fl04_agents_mcp/evidence/`; the evidence log lists the tool calls.

## What FL-04 would need to become an agent

Turning the mentor-update workflow into an agent is not “add more prompts.” It is hand the model a goal and a toolbelt, and let it choose steps.

**One concrete upgrade:** give the mentor-update agent tools to (1) read the latest metrics JSON under `work/outputs/` itself, (2) open the matching notebook or report section, and (3) draft only from those files — then stop for human approval before any send. The model would decide which output file matches the week’s ask, whether critique needs another pass after a tool re-read, and when the packet is too thin to write. The path would no longer be hardcoded A→B→C; the agent would loop on tool feedback until the note is packet-grounded or it asks me for a missing file.

That upgrade needs MCP (or equivalent tool APIs), clear tool docs, a hard stop before send, and the same proof habit: no number that did not come from a tool result. Until then, FL-04 stays a tight workflow with a human gate — and “agent” stays a word I only use when the model, not the checklist, is steering.
