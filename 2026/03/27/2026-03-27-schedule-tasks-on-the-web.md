# Schedule tasks on the web

- Score: 281 | [HN](https://news.ycombinator.com/item?id=47539188) | Link: https://code.claude.com/docs/en/web-scheduled-tasks

- TL;DR  
Anthropic’s Claude Code now supports cloud “scheduled tasks”: recurring, autonomous runs of a prompt against fresh GitHub clones and MCP-connected services, using configurable environments, schedules, and models. Tasks live on Anthropic’s infra, persist across restarts, and can open PRs, send notifications, or sync data without a user online. HN discussion ranges from excitement about end‑to‑end agentic dev workflows, through concerns about error compounding and inference costs, to skepticism that many use cases really need AI rather than simple deterministic automations.

- Comment pulse  
  - Launch welcomed, but contrasted with opaque usage limits and Twitter rumors; some note FUD about “rugpulls,” others say variable pricing and cloud control are normal.  
  - Some envision end‑to‑end agentic SDLC, but others report cascading errors, messy AI code, and humans losing understanding — counterpoint: promising in narrow, tool-rich workflows.  
  - Many say cron-like rules handle alerts or web checks cheaper and reliably; AI mainly helps non-coders specify “then” actions or fuzzy notions like “good deal”.

- LLM perspective  
  - View: This is essentially managed cron plus an LLM agent wired into GitHub and connectors, exposed via UI and CLI.  
  - Impact: Most valuable for small teams lacking DevOps: recurring PR grooming, audits, and syncing without standing up CI or custom scripts.  
  - Watch next: Key to adoption: reliable evals, guardrails on repo mutations, clearer pricing/quotas, and better UIs for defining conditions beyond time-based triggers.
