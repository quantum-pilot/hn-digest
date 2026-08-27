# My game's server is blocked in Spain whenever there's a football match on

- Score: 391 | [HN](https://news.ycombinator.com/item?id=45358433) | Link: https://old.reddit.com/r/gamedev/comments/1np6kyn/my_games_server_is_blocked_in_spain_whenever/

### TL;DR

A Spanish developer reports that Project Heartbeat becomes unreachable to users in Spain during football matches because its Cloudflare-fronted server shares IP space caught in LaLiga-related ISP blocks. The VPS itself is abroad and unblocked; collateral damage occurs at the proxy/CDN layer where many domains share addresses. Commenters report similar disruption to Cloudflare R2, Backblaze, GitHub, documentation, and other services, while correcting exaggerations that Spain’s entire internet shuts down. Legal challenges exist, but affected small services lack rapid whitelisting or practical recourse.

### Comment pulse

- Shared-IP blocking is structurally indiscriminate → one suspected stream can make unrelated games, storage, and developer infrastructure unreachable.
- Workarounds shift harm to users → VPNs add friction and can trigger banking or security controls.
- Scope matters → large CDN regions are disrupted during matches, not Spain’s complete internet.

### LLM perspective

- View: Fast copyright enforcement is externalizing its error costs onto innocent services.
- Impact: Small operators lose Spanish availability without notice, evidence, or timely appeal.
- Watch next: Measure blocked prefixes, false-positive duration, ISP variation, court outcomes, and restoration procedures.
