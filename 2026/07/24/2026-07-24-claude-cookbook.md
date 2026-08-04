# Claude Cookbook

- Score: 284 | [HN](https://news.ycombinator.com/item?id=49031409) | Link: https://platform.claude.com/cookbook/

### TL;DR

Anthropic’s cookbook is a date-stamped catalog of practical Claude examples spanning basic API patterns through production agents. Entries cover tool use, RAG, multimodal work, evaluations, context and memory management, Skills, orchestration, security, observability, hosting, prompt rollback, and human approval loops; newer recipes include programmatic tool calling, automatic compaction, and managed multi-agent systems. Community contributions are invited. Hacker News questioned whether fast model and harness improvements make such techniques quickly obsolete, criticized the frontend-aesthetics examples as regressions, but found manually invoked, requirements-focused Skills useful.

### Comment pulse

- Technique churn undermines deep investment → commenters expect reasoning models and vendor harnesses to absorb today’s prompt, memory, MCP, and orchestration patterns.
- Aesthetic guidance failed its own visual test → many preferred the unprompted examples, calling the alternatives gradient-heavy and formulaic.
- User-triggered Skills offer a durable compromise → they consume context only when invoked and keep people focused on requirements and experiential decisions.

### LLM perspective

- **View:** Cookbooks are most valuable as runnable reference implementations, not doctrines; durability comes from exposing stable concepts beneath changing APIs.
- **Impact:** Teams can prototype faster, but copying recipes uncritically risks stale architecture, vendor coupling, and unmeasured quality regressions.
- **Watch next:** Track recipe update dates, executable tests, model-version compatibility, maintenance ownership, and before-versus-after task metrics.
