# My game's server is blocked in Spain whenever there's a football match on

- Score: 391 | [HN](https://news.ycombinator.com/item?id=45358433) | Link: https://old.reddit.com/r/gamedev/comments/1np6kyn/my_games_server_is_blocked_in_spain_whenever/

TL;DR
During Spanish football matches, rights-holders trigger rapid ISP blocks to curb live piracy, often taking down entire IP ranges and CDNs, which knocks unrelated services offline. HN reports widespread collateral damage (game servers, developer tooling), legal justifications via dynamic court orders, and prior invasive enforcement by LaLiga. Commenters connect this to fragmented, high-cost broadcasting markets across Europe that fuel piracy and declining youth interest. Some advocate decentralizing away from mega-CDNs; others note IXPs show the internet mostly continues working, with big sites quietly exempted.

Comment pulse
- Live blocking targets CDNs/IPs → match-time takedowns cause collateral outages: Cloudflare R2, Backblaze B2, GitHub, Docker, game servers; Friend MTS court orders cited.
- Fragmented rights inflate costs → multiple subscriptions (€100–200/month) push fans to piracy/dodgy boxes; youth interest drops in Italy, Germany, Ireland.
- Aggressive enforcement invades privacy → LaLiga app used mic+GPS to detect bar broadcasts; seen as dystopian — counterpoint: performance licensing fees are standard across Europe.

LLM perspective
- View: Broad, dynamic IP blocking for live sports is miscalibrated; precision filtering and due-process transparency are needed to reduce collateral.
- Impact: Developers on CDNs, registries, and storage see downtime; Spanish users lose access during match windows; trust in ISPs erodes.
- Watch next: Outcomes of Cloudflare/RootedCON cases, ISP disclosure of blocklists, measurement dashboards, and technical carve-outs for critical services.
