# Cloudflare outage on December 5, 2025

- Score: 516 | [HN](https://news.ycombinator.com/item?id=46162656) | Link: https://blog.cloudflare.com/5-december-2025-outage/

### TL;DR

Cloudflare had a 25‑minute outage on December 5, 2025, affecting roughly 28% of its HTTP traffic. While rolling out WAF protections for a new React Server Components CVE, engineers disabled an internal test ruleset via a global “killswitch” config. A long‑standing Lua bug in the legacy FL1 proxy then crashed request processing, returning 500s for sites using Managed Rules. Cloudflare reverted the change and, after a similar Nov 18 incident, promises safer config rollouts, fail‑open behavior, and broader resilience work.

---

### Comment pulse

- Internet monoculture concern → Cloudflare’s scale creates single-point failures; others argue its aggregate uptime beats most DIY hosting and synchronized downtime may hurt users less.  
- Communication and trust → Status page lagged real outages; some praise transparent postmortems, others say back‑to‑back incidents make “kudos” inappropriate and confidence fragile.  
- Ops and monitoring gaps → Commenters want second‑level alerting, auto‑rollback, strong correlation of config changes to errors, and closer coordination between deployers and on‑call engineers.  

---

### LLM perspective

- View → Centralized edge providers can be net‑reliable, but only with safety cultures akin to aviation or nuclear operations.  
- Impact → Customers should treat Cloudflare as a dependency, not a given; design multi‑CDN or fail‑open paths for critical workloads.  
- Watch next → Whether Cloudflare ships granular config rollouts, stronger isolation, and automated canaries backed by transparent verifiable reliability metrics.
