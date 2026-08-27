# Cloudflare was down

- Score: 811 | [HN](https://news.ycombinator.com/item?id=46158191) | Link: https://www.cloudflare.com/

### TL;DR

The supplied page extraction is Cloudflare’s generic homepage and contains no incident account, so this summary relies on the contemporaneous discussion. Users observed plain HTTP 500s across some unrelated services while other proxied sites, tunnels, Workers, or CDN configurations continued operating. A quoted status notice blamed a Web Application Firewall parsing change intended to mitigate a React Server Components vulnerability and denied an attack. Commenters inferred product-specific impact, criticized incomplete status reporting, and worried that repeated incidents reveal weak isolation and third-party concentration risk.

### Comment pulse

- Repeated outages prompt dependency reviews and concern about reputational damage, though affected configurations differed.
- Users wanted immediate status-page visibility; replies say company-run status pages routinely lag partial incidents.
- WAF exclusions reportedly stayed available, suggesting selective impact rather than a complete network failure.

### LLM perspective

- View: User observations identify symptoms and boundaries, but not a complete root cause.
- Impact: Customers without bypass plans expose their availability to opaque upstream configuration changes.
- Watch next: Official affected-product matrix, status-page latency, isolation controls, and customer failover guidance.
