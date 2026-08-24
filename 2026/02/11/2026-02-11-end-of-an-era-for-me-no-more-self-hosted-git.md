# End of an era for me: no more self-hosted git

- Score: 103 | [HN](https://news.ycombinator.com/item?id=46969751) | Link: https://www.kraxel.org/blog/2026/01/thank-you-ai/

### TL;DR

After running public Git since 2011, Gerd Hoffmann retired his self-hosted service because scrapers overwhelmed cgit with repetitive requests. Existing GitLab and GitHub mirrors became primary repositories, leaving only a mostly static self-hosted website. Bots continued requesting removed cgit pages; millions of 404 responses filled the disk faster than default log rotation could cope, causing another outage before reconfiguration. Commenters shared defenses including Anubis challenges, cookies, rate limits, fail2ban, blocked networks, basic authentication, and reduced commit views, while debating accessibility costs and whether AI meaningfully changes ordinary scraper abuse.

### Comment pulse

- Cheap friction stops many bots → JavaScript reloads, basic authentication, and route-specific blocks reportedly cut traffic dramatically.
- Defense can exclude legitimate users → anti-bot JavaScript penalizes NoScript users and reinforces expectations that pages execute untrusted code.
- AI attribution remains contested → named bot user-agents and code demand support it; critics see familiar indiscriminate scraping at greater volume.

### LLM perspective

- View: The decisive cost is operator attention: even manageable traffic can make volunteer hosting no longer worth defending.
- Impact: Small forges centralize onto large platforms, reducing infrastructure diversity and transferring bot-control costs to better-resourced providers.
- Watch next: Crawler compliance, caching and rate-limit defaults, log safeguards, lightweight Git frontends, hosting bills, and scraper identification accuracy.
