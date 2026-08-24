# Anthropic Outage for Opus 4.5 and Sonnet 4/4.5 across all services

- Score: 172 | [HN](https://news.ycombinator.com/item?id=46267385) | Link: https://status.claude.com/incidents/9g6qpr72ttbr

### TL;DR

Anthropic reported degraded availability for Opus 4.5 and Sonnet 4 and 4.5 across Claude’s website, API, platform, and Claude Code on December 14. The incident lasted from 13:25 to 14:43 Pacific time. A network-routing misconfiguration dropped traffic to inference backends; reverting it restored service. An engineer said overlapping route advertisements blackholed some backends, detection took roughly 75 minutes, and usual mitigations failed. Anthropic plans better synthetic monitoring and visibility around high-impact infrastructure changes.

### Comment pulse

- Users appreciated the unusually candid live status updates and follow-up engineering detail.
- Some clients misreported the outage as exhausted message quotas or an upgrade prompt, compounding confusion with incorrect recovery guidance.
- Developers described abrupt productivity loss, underscoring dependence on centralized inference services.

### LLM perspective

- View: The incident exposed observability and error-mapping gaps beyond the routing mistake itself.
- Impact: Partial routing failures can masquerade as account limits and leave standard mitigation paths ineffective.
- Watch next: Synthetic probes by model, route-change guardrails, and client-side error classification.
