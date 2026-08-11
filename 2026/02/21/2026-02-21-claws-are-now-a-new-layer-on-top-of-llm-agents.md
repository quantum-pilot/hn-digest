# Claws are now a new layer on top of LLM agents

- Score: 161 | [HN](https://news.ycombinator.com/item?id=47096253) | Link: https://twitter.com/karpathy/status/2024987174077432126

### TL;DR

Karpathy argues that Claws form a persistent layer above LLM agents, handling orchestration, schedules, context, tools, and local integrations. He distrusts OpenClaw’s roughly 400,000-line, actively attacked codebase and favors smaller containerized alternatives such as NanoClaw, whose skills modify a compact, forkable repository instead of accumulating configuration. HN discussion centered on security and ownership: locally controlled agents may represent users better than product-embedded AI, but powerful actions need least-privilege accounts, approval gates, and clear separation between the initiating user and everyone affected.

### Comment pulse

- Treat the agent like staff → separate email, restricted payment methods, and scoped credentials limit damage — counterpoint: real assistants often receive sensitive access.
- Human approval should guard irreversible actions → OTPs, trusted messaging channels, or explicit activity links can authorize risky tool calls.
- Agent-first APIs could reduce GUI dependence → incumbent services may resist because easier switching weakens lock-in.

### LLM perspective

- **View:** Locality improves control, not safety; permissions must be enforced outside the model.
- **Impact:** Personal agents could reorganize services around users while expanding attack surfaces into homes and accounts.
- **Watch next:** Sandboxing, credential brokers, approval UX, supply-chain controls, and auditable skill installation.
