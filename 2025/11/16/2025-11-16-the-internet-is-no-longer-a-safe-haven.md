# The internet is no longer a safe haven

- Score: 219 | [HN](https://news.ycombinator.com/item?id=45944870) | Link: https://brainbaking.com/post/2025/10/the-internet-is-no-longer-a-safe-haven/

### TL;DR

A burst of distributed scraping overwhelmed a hobbyist's small server: Gitea and Fail2ban consumed CPU while requests spoofed a normal Chrome user agent and rotated within an Alibaba-hosted `47.79` range. Per-IP bans and log processing reacted too slowly, so blocking the entire `/16` with iptables provided immediate relief. The author resents being pushed toward Anubis, Cloudflare, or Codeberg. Commenters say hostile scanning long predates AI, recommend native Nginx rate limiting, and distinguish public sites from private services that can use mTLS or WireGuard.

### Comment pulse

- Longtime operators treat constant exploit scans as normal and rely on patching, minimal exposure, backups, and layered controls.
- Defensive tricks such as zip bombs can backfire by increasing bandwidth costs and attracting more bots.

### LLM perspective

- View: The new burden may be scraper volume, while the underlying hostile environment is decades old.
- Impact: Small operators either spend more time filtering traffic or surrender infrastructure to centralized intermediaries.
- Watch next: Server-side rate limits, Gitea migration, resource ceilings, subnet churn, and false-positive effects on readers.
