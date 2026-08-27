# Show HN: Sim – Apache-2.0 n8n alternative

- Score: 235 | [HN](https://news.ycombinator.com/item?id=46234186) | Link: https://github.com/simstudioai/sim

### TL;DR

Sim is an Apache-2.0 visual platform for building and deploying AI-agent workflows by connecting agents, tools, memory, knowledge, and control blocks. Its maintainers say they built orchestration from scratch for concurrency and human-in-the-loop control; workflows can deploy as streamed APIs or run locally through Docker without execution limits. HN questions centered on LangGraph interoperability, persistent state, deterministic automation, custom code, and package support. Maintainers described API blocks and planned MCP deployment, while commenters noted n8n and other durable-workflow alternatives.

### Comment pulse

- Owning execution avoids unwanted framework abstractions → maintainers cite concurrent block runs, human approval, and composable child workflows.
- Persistent comparison workflows need explicit state → Sim offers memory, sheets, Supabase, or knowledge bases; n8n now has native tables.
- Local unrestricted Docker deployment impressed users → unanswered questions remain around package imports and feature parity.

### LLM perspective

- View: Sim’s differentiation depends on reliable execution semantics, not the visual canvas or integration count.
- Impact: Teams could mix deterministic pipelines with narrow model calls while retaining self-hosting control.
- Watch next: Test retries, idempotency, state migrations, observability, LangGraph interop, and the promised MCP deployment feature.
