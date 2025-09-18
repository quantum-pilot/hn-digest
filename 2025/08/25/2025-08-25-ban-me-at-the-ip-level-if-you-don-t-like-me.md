# Ban me at the IP level if you don't like me

- Score: 599 | [HN](https://news.ycombinator.com/item?id=45010183) | Link: https://boston.conman.org/2025/08/21.1

- TL;DR
  - A blogger found “Thinkbot” crawling his site while ignoring robots.txt and cheekily suggesting IP-level bans. It rotated across 74 IPs spanning 41 Tencent-owned network blocks, prompting him to firewall roughly 476k Tencent addresses. HN discusses how well-behaved crawlers get trapped by robots.txt tarpits, while many sites report bots as a majority of traffic that wreck caches, hog connections, and sometimes DoS. Suggested countermeasures: ASN blocking, ad hoc tokens/parameters, disabling keep-alive, and leaning on CDNs/WAFs; robots.txt isn’t a defense.

- Comment pulse
  - Friendly crawler hit robots.txt tarpit; timeouts treated as Disallow; punishes good actors — counterpoint: tarpitting hides sensitive disallows and slows abusers.
  - Bots can be 60%+ of requests, evict caches, and trigger outages; simplistic rate limits often fail at diffuse, multi-IP scraping.
  - Practical wins are ad hoc: block ASNs, UA heuristics, disable keep-alive, require site-specific tokens; otherwise outsource to Cloudflare-style services.

- LLM perspective
  - View: Distributed scraping from big cloud ASNs defeats single-IP blocking; etiquette-based controls are outdated.
  - Impact: Dynamic/archival sites pay in CPU, bandwidth, and cache churn; CDNs/WAFs become mandatory for many.
  - Watch next: Bot attestation standards, shared ASN/IP reputations, automated tarpit/denylist features in mainstream CDNs.
