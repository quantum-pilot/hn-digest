# What happened to TheNumbers.com

- Score: 269 | [HN](https://news.ycombinator.com/item?id=49024691) | Link: https://stephenfollows.com/p/what-just-happened-to-thenumberscom-should-worry-us-all

### TL;DR
A key box-office data site, TheNumbers.com, vanished in March 2026 after being overwhelmed by AI-driven scraping and likely targeted probing tied to prediction markets that settle using its data. Its 30-year-old, 160k‑file codebase made defense impossible, so the team shut the old server down and rebuilt a minimal site. The episode illustrates how LLM crawlers now generate most traffic, impose real bandwidth and security costs, and erode the economics of the open web just as AI also lowers the barrier to hacking.

---

### Comment pulse
- Public-data PPP loan site killed by AI scrapers → bots ignored bulk-download option, paginated every facet, racking up $1k/month bandwidth on AWS and forcing shutdown — counterpoint: better rate-limiting/architecture could have mitigated this.  
- Architecture critique → sites like The Numbers should static-generate and front with CDNs; bots mainly expose how slow, cache-poor modern stacks and ORMs have become.  
- Open-web resentment vs acceptance → some avoid publishing or open-sourcing because LLMs monetize scraped work; others welcome training use, arguing everyone benefits, but costs/time are unfairly externalized.

---

### LLM perspective
- View: Bot and exploit pressure will force a shift from “open by default” to authenticated, rate-limited, or paid access for many niche but vital datasets.  
- Impact: Small, long-lived reference sites and public-interest projects face outages or closure; AI vendors gain cheap data but risk backlash and legal constraints.  
- Watch next: Adoption of pay-per-crawl/use, standardized bot identity protocols, prediction-market abuse cases, and off‑the‑shelf “bot firewalls” for legacy sites.
