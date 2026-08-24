# Show HN: Sim – Apache-2.0 n8n alternative

- Score: 235 | [HN](https://news.ycombinator.com/item?id=46234186) | Link: https://github.com/simstudioai/sim

### TL;DR

Sim is an Apache-licensed visual platform for composing and deploying AI agent workflows from connected agents, tools, and blocks. Its team built the orchestration engine rather than adopting LangGraph, citing control over execution, human approval, concurrent block runs, streaming APIs, and nested workflows. Missing integrations can be reached through code or API blocks, and the project can run locally in Docker without execution limits. HN interest centered on durable state for mostly deterministic automations, package extensibility, interoperability with existing agents, and deployment portability.

### Comment pulse

- The authors positioned their engine as a LangGraph replacement, while retaining interoperability through generic API calls and deployed workflow endpoints.
- Users wanted durable change detection for feeds, files, and issues; suggested storage included memory blocks, tables, spreadsheets, Supabase, and knowledge bases.
- Self-hosting without execution caps won praise, but unanswered questions remained around parity with n8n and importing npm or Python packages.

### LLM perspective

- View: Visual orchestration is useful when deterministic steps stay explicit and model calls remain small, inspectable components.
- Impact: Teams can prototype agent workflows locally, expose them as streaming APIs, and avoid maintaining a separate orchestration service.
- Watch next: MCP deployment, state durability, package installation, n8n parity, LangGraph integration tests, upgrade stability, and production observability.
