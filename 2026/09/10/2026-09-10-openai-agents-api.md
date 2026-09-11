# OpenAI Agents API

- Score: 258 | [HN](https://news.ycombinator.com/item?id=49649213) | Link: https://developers.openai.com/api/docs/guides/agents-api/overview

### TL;DR

OpenAI’s Agents API exposes its managed Codex harness to applications. Developers select models, tools, MCP connections, and either hosted or self-hosted execution environments; OpenAI handles durable sessions, orchestration, compaction, recovery, streaming, steering, and optional subagents. Usage, tools, and hosted containers are billed separately. The API currently supports only U.S. data residency and not Zero Data Retention, including with self-hosted sandboxes. Discussion welcomed reduced harness engineering but worried about provider dependence, portability, trust, and hidden reasoning.

### Comment pulse

- Managed harnesses save work → State, recovery, context management, and sandbox reliability are difficult to build well.
- Self-hosting improves control → Developers can keep execution environments while consuming OpenAI’s external orchestration layer.
- Lock-in remains → Proprietary models and opaque reasoning may make migration harder than lightweight local agent tools.

### LLM perspective

- View: The product’s core abstraction is durable agent orchestration, not merely remote code execution.
- Impact: Application teams can ship agent workflows faster while accepting a consequential control-plane dependency.
- Watch next: Portability standards, non-U.S. residency, ZDR support, failure semantics, observability, and cross-model compatibility.
