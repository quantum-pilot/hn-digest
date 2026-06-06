# Claude.ai unavailable and elevated errors on the API

- Score: 259 | [HN](https://news.ycombinator.com/item?id=47938097) | Link: https://status.claude.com/incidents/9l93x2ht4s5w

### TL;DR
Anthropic’s status page reports a widespread Claude outage on April 28, 2026, affecting claude.ai, the API, Claude Code, Cowork, Console, and government tenants for about 80 minutes before recovery and monitoring. Hacker News commenters focus less on this single incident and more on Anthropic’s reliability trend: enterprises spending six figures monthly complain of “one‑nine” uptime and weak support, others note the hard engineering of GPU-backed LLM services, and many advocate multi-provider, multi-model strategies to reduce vendor lock-in and outage impact.

### Comment pulse
- Enterprise buyers losing patience → Six‑figure monthly spend sees frequent outages, “one‑nine” availability, and poor support; some route Anthropic models via AWS/Google for better uptime.  
- Uptime metrics debated → Status shows ~98–99% over 90 days; some empathize with LLM infra complexity, others say auth issues shouldn’t cripple the core service.  
- Resilience via diversity → Some teams use multiple LLM vendors to ride out outages. — counterpoint: Others see multi‑provider setups as needless complexity.  

### LLM perspective
- View: LLM platforms must be treated like core cloud infra, with published SLOs, credits, and clear postmortems for major incidents.  
- Impact: Enterprise users will pressure vendors toward higher availability or shift spend to hyperscaler-hosted or open-weight alternatives they can control.  
- Watch next: Standardized LLM APIs, better automatic failover tooling, and realistic “two‑nine” style SLAs instead of marketing-driven uptime claims.
