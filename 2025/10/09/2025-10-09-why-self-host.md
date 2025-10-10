# Why Self-Host?

- Score: 271 | [HN](https://news.ycombinator.com/item?id=45528342) | Link: https://romanzipp.com/blog/why-a-homelab-why-self-host

- TL;DR
  The post argues for self-hosting to reclaim privacy and digital sovereignty, citing risks from Big Tech lockouts and metadata harvesting. Practical picks: CalDAV/CardDAV for calendars/contacts, cautious but feasible email hosting (Stalwart/Mailcow), Home Assistant to avoid forced cloud accounts, FreshRSS, and a self-hosted location tracker; author runs a 3‑node Kubernetes homelab. HN debate: small SaaS often can self-host on a VPS to cut costs, but security, backups/upgrades, and email deliverability are hard; scrutiny of “sovereignty” claims sparked discussion.

- Comment pulse
  - Small SaaS can self-host on a VPS with Caddy/Nginx → cheaper; apps don’t need cloud scale — counterpoint: OS risk; containers/k8s help; CDN for latency.
  - “Digital sovereignty” scrutiny → enum.co uses Google MX/SPF; founder says early pragmatic choice, migrating; many treat email as the self-hosting exception.
  - Reliability focus → backups/upgrades are the bottleneck; Docker volumes+compose ease restore; Coolify simplifies app hosting; secure remote access via Tailscale or self-hosted NetBird.

- LLM perspective
  - View: Self-host sensitive services; email remains hardest; favor open protocols to reduce lock-in and third-party access.
  - Impact: Indie devs and small teams cut SaaS costs and regain control, but must own monitoring, backups, and security hygiene.
  - Watch next: Measure email deliverability (SPF/DMARC/DKIM), run restore drills, compare edge CDN latencies, follow EU chat-control and provider SMTP policy changes.
