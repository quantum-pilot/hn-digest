# Anthropic says OpenClaw-style Claude CLI usage is allowed again

- Score: 472 | [HN](https://news.ycombinator.com/item?id=47844269) | Link: https://docs.openclaw.ai/providers/anthropic

### TL;DR

OpenClaw’s Anthropic integration again treats subscription-backed `claude -p` and Claude CLI reuse as permitted, while warning that Anthropic can change billing or access rules independently. The documented path reuses a same-host Claude Code login and draws from subscription limits; direct API keys remain the recommended option for shared automation and predictable production costs. OpenClaw also distinguishes CLI execution from copying OAuth credentials into a custom client, and says its runtime disables token-heavy features where possible.

### Comment pulse

- Users mainly objected to contradictory, informal policy announcements and feared workflows could become unsupported without warning.
- Some distinguished running inside official Claude Code from extracting OAuth credentials; others argued the billing status remains unresolved.
- Critics called limits a bait-and-switch — counterpoint: subscription economics may require human-scale usage limits and API billing for automation.

### LLM perspective

- Build against API keys when continuity and cost accounting matter more than subscription savings.
- Treat CLI compatibility as revocable operational policy, not a stable platform contract.
- Expose authentication mode and billing surface clearly so operators understand which limits apply.
