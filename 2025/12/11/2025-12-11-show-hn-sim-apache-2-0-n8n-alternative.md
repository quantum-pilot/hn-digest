# Show HN: Sim – Apache-2.0 n8n alternative

- Score: 235 | [HN](https://news.ycombinator.com/item?id=46234186) | Link: https://github.com/simstudioai/sim

### TL;DR
Sim is an Apache-2.0, self-hostable alternative to n8n focused on AI agent workflows. It provides a visual canvas with many built-in blocks (agents, tools, memory, knowledge base, code, API), plus a custom orchestration engine that supports human-in-the-loop, concurrent block execution, and streaming. Workflows can be deployed as APIs and soon as MCP servers, making it a potential drop‑in replacement or companion to LangGraph. HN discussion centers on vendor lock-in, practical workflow use cases, and the appeal of unlimited local Docker deployment.

---

### Comment pulse
- Sim vs LangGraph → Sim built its own orchestration for control and fewer dependencies; workflows deploy as streaming APIs, potentially replacing LangGraph—counterpoint: some still like LangGraph’s abstractions and ecosystem.
- Stateful workflows (dedupe, change detection) → Sim’s memory, CSV/sheets, Supabase, or knowledge base blocks cover “have I seen this before?” without custom infra; n8n, windmill, autokitteh also suggested.
- Local-first appeal → Being able to run Sim fully via Docker with no execution limits is seen as a major differentiator from increasingly monetized SaaS stacks.

---

### LLM perspective
- View: Sim is positioning as the “agent-native” automation layer, not just generic no-code flows with an LLM node bolted on.
- Impact: Most useful for teams wanting reproducible, inspectable agent workflows without committing to LangSmith-style hosted control planes.
- Watch next: Quality of MCP integration, stability of SDKs, and whether business models preserve the current openness of self-hosting.
