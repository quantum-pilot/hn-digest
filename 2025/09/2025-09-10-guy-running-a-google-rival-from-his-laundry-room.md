# Guy running a Google rival from his laundry room

- Score: 213 | [HN](https://news.ycombinator.com/item?id=45197187) | Link: https://www.fastcompany.com/91396271/searcha-page-seekninja-diy-search-engines

TL;DR (70–90 words)
A solo developer is building a Google-style search engine from his laundry room on a single, beefy server. His services (Search‑a‑Page and privacy-focused Seek Ninja) use traditional crawling/indexing with LLMs for keyword/context expansion. A sudden HN-driven traffic spike caused errors—context expansion, not search, was the bottleneck. Commenters focus on the real hurdles: crawling an adversarial web on limited IPs, ranking quality, and bootstrapping via public indexes. Some question broad usefulness in today’s hub‑dominated web, suggesting niches or small‑site search as the pragmatic path.
_Content unavailable; summarizing from title/comments._

Comment pulse
- Crawling is hardest → adversarial sites block single-IP crawlers; crowdsourcing/proxies suggested — counterpoint: rented proxies often blocked; ranking harder than just 'having pages'.
- Bootstrap via public indexes → personal domain lists, Common Crawl, and OpenWebSearch could seed coverage; licensing/freshness/quality trade-offs remain.
- Value question → web centralized into content hubs; indie crawlers may excel at niche or small-site search, not general-purpose Google replacement.

LLM perspective
- View: Use LLMs only for query expansion/summarization with strict budgets; cache aggressively; keep ranking features classic and measurable.
- Impact: Low-cost, single-node engines can serve communities or verticals; broad web coverage demands distributed crawling and partnerships.
- Watch next: open web index releases, crawl-sharing pilots, ranking evals vs baselines, stability fixes for traffic spikes and context bottlenecks.
