# Claude: Elevated errors across many models [resolved]

- Score: 179 | [HN](https://news.ycombinator.com/item?id=48558766) | Link: https://status.claude.com/incidents/xmhsglsz3h3w

### TL;DR

Anthropic reported a resolved incident affecting claude.ai, its API, Claude Code, and Cowork. From 17:23–18:00 UTC, all Sonnet and Opus models reached roughly 10 percent errors; Opus 4.8 then averaged 10 percent until 19:20 UTC. HN readers treated it less as an isolated outage than a reliability concern, citing recurrent failures, sluggish clients, undocumented enterprise-routing limitations, and brittle agent recovery after server errors. Others emphasized the difficulty of rapid GPU-constrained scaling, reported few problems, or argued Anthropic still excels in models and product-market fit despite operational roughness.

### Comment pulse

- Agent failures cascade → one subagent’s 500 error left the parent uncertain about shared state and triggered a repository checkout.

- Infrastructure quality is strategic → distributed systems punish misunderstood generated code, and a reliable competitor could erode today’s strong product-market fit.

- Vendor comparisons remain polarized → some switched to Codex for reliability and long tasks — counterpoint: Claude retains richer integrations and frontend strengths.

### LLM perspective

- **View:** A 10 percent error rate is operationally severe for autonomous workflows because retryable requests can leave non-retryable side effects.

- **Impact:** Developers need checkpoints, idempotent tools, bounded retries, and human approval around destructive recovery while model providers improve availability.

- **Watch next:** Anthropic should publish root cause, regional scope, mitigation details, recurrence metrics, and client behavior during partial outages.
