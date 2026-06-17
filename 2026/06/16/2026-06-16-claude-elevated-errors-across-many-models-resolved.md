# Claude: Elevated errors across many models [resolved]

- Score: 179 | [HN](https://news.ycombinator.com/item?id=48558766) | Link: https://status.claude.com/incidents/xmhsglsz3h3w

## TL;DR
Anthropic reported a service incident causing elevated error rates across several Claude models (notably Sonnet, Opus 4.8, and Haiku 4.5), affecting claude.ai, the Claude API, Claude Code, and Claude Cowork. The main outage window began around 17:23 UTC, with error rates peaking at roughly 10% for Sonnet and Opus, then persisting mainly on Opus 4.8 until about 19:20 UTC. Anthropic implemented fixes, transitioned to monitoring, and has marked the incident as resolved.

---

## LLM perspective
- View: This shows Anthropic treating LLM access like classic SaaS infra, with structured incident response and public status transparency.  
- Impact: Teams depending on Claude for production workflows need robust fallbacks, retries, and perhaps model-level redundancy.  
- Watch next: Look for post-incident retrospectives, clarified SLAs, and any architectural changes to isolate failures between individual models.
