# The internet is no longer a safe haven

- Score: 219 | [HN](https://news.ycombinator.com/item?id=45944870) | Link: https://brainbaking.com/post/2025/10/the-internet-is-no-longer-a-safe-haven/

- TL;DR
  - An indie server was knocked offline by scrapers hammering Gitea commit pages with spoofed Chrome UAs; Fail2ban lagged until an iptables drop of Alibaba Cloud 47.79/16 calmed traffic. The author resists Cloudflare/Anubis complexity and tracking, may move Gitea to Codeberg, and laments centralization pressure. HN replies: this barrage is longstanding; cert‑transparency and DNS draw scanners; experiences range from constant probes to oddly polite scrapers. Mitigation approaches spark debate, and countermeasures like zipbombs can backfire.

- Comment pulse
  - Attacks are normal and continuous → scanners hit anything with DNS/TLS; certificate transparency and WordPress probes flood logs since mid‑2000s.
  - Defend at the edge → Nginx rate‑limiting, honeypots, and targeted 403s outperform Fail2ban tailing logs — counterpoint: adds complexity and won’t help a public blog.
  - Not all scrapers are abusive → some hit cgit politely at 2–3 req/min, ironically fetching code mirrored from upstreams.

- LLM perspective
  - View: Push dynamic admin/repo UIs off the public web; keep only static pages internet‑facing; everything else via SSH/VPN.
  - Impact: Smaller attack surface lowers CPU/log churn and reduces centralization pressure without surrendering privacy.
  - Watch next: Automate ASN/ipset blocks; per‑path burst quotas in nginx; measure CT‑driven scanning with canary certs; consider privacy‑respecting CDNs for static assets.
