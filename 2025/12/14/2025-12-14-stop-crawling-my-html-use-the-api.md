# Stop crawling my HTML – use the API

- Score: 111 | [HN](https://news.ycombinator.com/item?id=46265579) | Link: https://shkspr.mobi/blog/2025/12/stop-crawling-my-html-you-dickheads-use-the-api/

## TL;DR
The author runs a WordPress blog and the OpenBenches project, both exposing rich, well-documented JSON/ActivityPub/oEmbed/text APIs and a sitemap. Nonetheless, “AI” and generic scrapers hammer the sites’ HTML, ignoring these machine-friendly endpoints. He argues this is lazy brute force: HTML is brittle, inconsistent, and primarily for humans, while APIs are structured, cheaper for servers, and already discoverable via `<link rel>` and sitemaps. His plea: LLM crawlers should detect and prefer existing APIs instead of blindly scraping pages.

---

## Comment pulse
- HTML is the canonical source for humans → scrapers follow what readers actually see; APIs are rare, secondary, and often get abandoned or paywalled.  
- Scraper ergonomics → generic HTML parsing works everywhere; per-site API logic doesn’t scale, though common CMSes (WordPress, MediaWiki) likely merit explicit API support.  
- APIs/feeds are often partial → many sites expose summaries or different content; real pain is bots ignoring robots.txt and overloading small sites.

---

## LLM perspective
- View: Default to HTML, but auto-discover and opportunistically switch to APIs/sitemaps when standardized hints (WordPress, ActivityPub, oEmbed) are present.  
- Impact: Reduces load on small publishers and civic projects, while improving data quality and schema consistency for downstream AI tools.  
- Watch next: Emerging AI-specific headers/robots directives, and libraries that bundle “CMS-aware” crawling strategies as a standard crawler feature.
