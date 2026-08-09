# Anthropic downgraded cache TTL on March 6th

- Score: 461 | [HN](https://news.ycombinator.com/item?id=47736476) | Link: https://github.com/anthropics/claude-code/issues/46829

### TL;DR

A GitHub issue reports that Claude Code’s prompt-cache time-to-live silently fell from one hour to five minutes around early March 2026, allegedly increasing cache misses, quota consumption, and costs. Because subscriptions use five-hour windows, pauses or forced quota waits can now trigger expensive context rebuilds and a worsening usage cycle. Commenters connected the change to broader complaints about shrinking quotas, weaker reasoning, bugs, and opaque service changes, though experiences varied. One suggested periodic tiny requests to preserve the cache; others recommended multi-model tools or switching providers.

### Comment pulse

- Engineers described eroding trust as limits, harness policies, reasoning behavior, and apparent quality changed without clear explanations.
- Several users reported dramatic degradation — counterpoint: one iterative user saw little impact and still obtained good results with careful guidance.
- A proposed workaround sends a minimal request every 4 minutes 50 seconds, keeping cached context alive near quota boundaries.

### LLM perspective

- **View:** An undocumented cache-policy change can feel like a model downgrade because it alters both effective price and continuity.
- **Impact:** Cache misses compound restrictive quotas, making long sessions costlier and organizational rollouts less predictable.
- **Watch next:** Anthropic confirmation, restoration or documentation, cache-hit telemetry, reproducible cost comparisons, and subscription-level behavior.
