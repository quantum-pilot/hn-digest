# End of an era for me: no more self-hosted git

- Score: 103 | [HN](https://news.ycombinator.com/item?id=46969751) | Link: https://www.kraxel.org/blog/2026/01/thank-you-ai/

## TL;DR
Longtime open-source developer Gerd Hoffmann shut down his self-hosted public git server (running since 2011) after it was effectively DDoS’d by “AI” scrapers hammering his cgit web frontend with pointless per-commit requests. He moved everything to GitHub/GitLab and now only self-hosts a static blog, which scrapers still briefly knocked over by filling disks with 404 logs. HN discussion focuses on practical defenses, collateral damage to users, and whether this is really new AI behavior or just old scraping at new scale.

---

## Comment pulse
- Use JS “shibboleth” cookies to distinguish browsers from bots → massively cuts bot traffic. — counterpoint: excludes NoScript/uBlock users and normalizes mandatory client-side code execution.

- Network-level defenses work: fail2ban on suspicious git paths, block abusive ASNs, or return 404 for expensive endpoints; some propose ssh/TUI git interfaces that scrapers won’t handle.

- Logs show named AI bots (ClaudeBot, GPTBot, Amazonbot, Meta, PetalBot) generating tens of millions of mostly redundant requests, straining servers and pay-per-request hosting; others argue this is just traditional scraping turned up to 11.

---

## LLM perspective
- View: Self-hosting public developer services is increasingly costly without serious anti-bot engineering, pushing individuals toward large, shielded platforms.

- Impact: Indie devs and small communities lose autonomy; hosts and the environment pay for vast volumes of redundant AI-crawler traffic.

- Watch next: Standardized AI crawl opt-outs with enforcement teeth, lightweight open-source bot filters for small sites, and hosting plans resilient to scraper-driven cost spikes.
