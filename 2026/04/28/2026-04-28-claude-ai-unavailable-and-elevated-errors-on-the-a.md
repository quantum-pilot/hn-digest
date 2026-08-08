# Claude.ai unavailable and elevated errors on the API

- Score: 259 | [HN](https://news.ycombinator.com/item?id=47938097) | Link: https://status.claude.com/incidents/9l93x2ht4s5w

### TL;DR

Anthropic reported a 78-minute incident on April 28, from 17:34 to 18:52 UTC, that made Claude.ai inaccessible and raised authentication errors across its API and Claude Code. The disruption also affected Console, Cowork, and Claude for Government. Success rates returned to normal before the incident was marked resolved at 19:15 UTC; no root cause was provided. HN users focused on recent reliability, especially for expensive enterprise deployments, and argued that low switching costs make multi-model tooling or alternative Claude API hosts practical resilience measures.

### Comment pulse

- One organization reported spending over $200,000 monthly while executives grew frustrated with outages and support.
- Some disputed “one nine” rhetoric based on usage patterns — counterpoint: enterprise workflows still need explicit availability commitments.
- Developers favored Anthropic, Codex, and Gemini fallbacks because changing LLM providers may cost less than traditional multicloud.

### LLM perspective

- Isolate authentication so account failures do not simultaneously impair web, CLI, and API entry points.
- Buyers need service objectives, support escalation, and tested failover before making assistants production dependencies.
- Watch for a root-cause report covering capacity, regional isolation, and recovery controls.
