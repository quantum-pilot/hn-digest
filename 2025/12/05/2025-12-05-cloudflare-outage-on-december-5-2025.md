# Cloudflare outage on December 5, 2025

- Score: 516 | [HN](https://news.ycombinator.com/item?id=46162656) | Link: https://blog.cloudflare.com/5-december-2025-outage/

### TL;DR

Cloudflare says a 25-minute outage affected about 28% of its HTTP traffic when a global configuration change disabled an internal WAF test ruleset. On older FL1 proxies, skipping an `execute` action left a missing Lua object that later code dereferenced, returning HTTP 500s to customers using the managed ruleset. The change supported mitigation work for a React Server Components vulnerability and was not an attack. Cloudflare promises gradual configuration rollouts, stronger rollback paths, fail-open behavior, and a change freeze while those controls are completed.

### Comment pulse

- Critics blame centralized blast radius—counterpoint: many sites could not independently match Cloudflare’s long-term reliability.
- Readers question why alerts took two minutes and rollback about 21 minutes after a globally propagated change.
- Some praise the postmortem’s clarity; others say a second major incident makes apologies insufficient.

### LLM perspective

- View: The nil dereference was local; instant global configuration propagation made it systemic.
- Impact: Customers inherit correlated failure when a provider’s safety controls bypass staged deployment.
- Watch next: Automatic rollback thresholds, configuration canaries, FL1 retirement, fail-open defaults, and published resilience milestones.
