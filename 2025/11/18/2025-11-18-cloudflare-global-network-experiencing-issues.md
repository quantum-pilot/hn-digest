# Cloudflare Global Network experiencing issues

- Score: 2300 | [HN](https://news.ycombinator.com/item?id=45963780) | Link: https://www.cloudflarestatus.com/incidents/8gmgl950y3h7

### TL;DR

Cloudflare reported a global internal service degradation beginning at 11:48 UTC, affecting Access, Bot Management, CDN/cache, Dashboard, Firewall, Network, WARP, and Workers. Access and WARP recovered first; application services, dashboard logins, bot scores, latency, and intermittent errors took longer. A fix was deployed by 14:42, normal operation was reported at 17:44, and the incident closed at 19:28. Discussion relayed Cloudflare's early explanation that a routine configuration change triggered a latent bot-mitigation failure, not an attack.

### Comment pulse

- Operators shared API and Terraform procedures for bypassing the proxy, warning about certificates, origin exposure, lost caching, WAF, and DDoS protection.
- The outage exposed status dashboards and administrative controls that depended on the same failing provider.

### LLM perspective

- View: Recovery plans must remain usable when both data-plane service and customer controls degrade together.
- Impact: Concentrated edge infrastructure turns one vendor incident into synchronized failures across unrelated sites.
- Watch next: Root-cause controls, staged configuration delivery, independent status paths, and rehearsed DNS bypasses.
