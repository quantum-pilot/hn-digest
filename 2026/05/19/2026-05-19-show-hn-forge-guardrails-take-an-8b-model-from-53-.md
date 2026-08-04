# Show HN: Forge – Guardrails take an 8B model from 53% to 99% on agentic tasks

- Score: 275 | [HN](https://news.ycombinator.com/item?id=48192383) | Link: https://github.com/antoinezambelli/forge

### TL;DR

Forge is an MIT-licensed Python reliability layer for self-hosted LLM agents, wrapping tool calls with malformed-response recovery, retry nudges, required-step enforcement, and VRAM-aware context compaction. It can run workflows directly, embed as middleware, or proxy OpenAI-compatible clients across local and Anthropic backends. Although the Show HN title advertises a 53%→99% jump, the current repository reports its best 8B configuration at 86.5% over 26 scenarios and 76% on the hardest tier. HN agreed harnesses unlock small models but flagged retry cost and long-session attention decay.

### Comment pulse

- Guardrails can substitute for raw model scale → constrained retries prevent invalid actions while preserving acceptable reasoning from smaller local models.

- Stepwise validation offers cleaner histories → checking each argument and rewinding failures improves reliability — counterpoint: many-argument tools may require excessive round trips.

- Long horizons expose a different ceiling → small models degrade before advertised context limits, while large frontier models sustain attention across longer sessions.

### LLM perspective

- **View:** Forge improves execution reliability, not underlying judgment; benchmark gains depend on tasks where detectable protocol errors dominate.

- **Impact:** Teams can reserve frontier APIs for ambiguous planning while routing structured, recoverable workflows to cheaper local models.

- **Watch next:** Compare fixed-attempt budgets, latency, token use, unseen tools, 50-plus-step tasks, and success without benchmark-specific nudges.
