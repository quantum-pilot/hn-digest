# Gentoo bugzilla closed due AI bot scraper overload

- Score: 151 | [HN](https://news.ycombinator.com/item?id=49221864) | Link: https://social.treehouse.systems/@mgorny/117058483039362779

### TL;DR
Gentoo’s Bugzilla instance was taken offline after being swamped by high-volume, distributed web scrapers, likely feeding AI training, making the service unusable for its maintainer. The Mastodon thread shows other infra operators seeing similar attacks via botnets and residential proxies, making IP or user‑agent blocking ineffective. HN discussion circles around who’s scraping, how AI’s demand for data is eroding the open web, and proposed defenses—logins, micropayments, proof‑of‑work, or P2P delivery—all with serious usability and equity trade‑offs.

### Comment pulse
- Attribution is murky: some traffic matches big AI companies, but much comes from Southeast-Asia ranges, botnets, and browser-masquerading scrapers using residential IPs.  
- Operators say valuable data now gets “eaten alive,” forcing logins or lockdowns; others see less AI, more push toward walled‑garden, identity‑gated internet.  
- Suggested defenses include per-request micropayments or in-browser proof‑of‑work/crypto‑mining gates, but critics say friction, exclusion of poorer users, and wasted time make them untenable.

### LLM perspective
- AI training’s externalities land hardest on volunteer-run infra, who lack time and tooling to distinguish “good” vs “bad” bots.  
- Expect more open resources—bug trackers, docs, forums—to hide behind logins, CAPTCHAs, or CDNs, reducing crawlability and casual access.  
- Standardized bot disclosure, rate‑limit protocols, and enforceable opt‑out mechanisms could rebalance scraping, but need buy‑in from AI labs and regulators.
