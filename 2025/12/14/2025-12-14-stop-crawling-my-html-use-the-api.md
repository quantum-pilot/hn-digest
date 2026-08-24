# Stop crawling my HTML – use the API

- Score: 111 | [HN](https://news.ycombinator.com/item?id=46265579) | Link: https://shkspr.mobi/blog/2025/12/stop-crawling-my-html-you-dickheads-use-the-api/

### TL;DR

The blogger argues that crawlers wastefully fetch fragile, inconsistent HTML despite machine-readable alternatives advertised in each page: WordPress REST JSON, per-post JSON, ActivityPub, oEmbed, plain text, and an XML sitemap. The same problem affects OpenBenches, whose GeoJSON and documented API are ignored while bots repeatedly request pages. He proposes clearer AI-specific instructions. HN largely challenged the premise: rendered HTML is the canonical human-visible output, APIs may be rare, stale, partial, restricted, or differently shaped, and a universal HTML pipeline often costs less than site-specific integration.

### Comment pulse

- WordPress prevalence made special-casing seem worthwhile to some; others said reliable discovery and semantic mapping still erase the return.
- Commenters preferred crawler identification, caching, and robots.txt compliance as general load controls when API content may differ.
- Prompt poisoning drew skepticism because it may affect neither training nor modern prompt contexts reliably.

### LLM perspective

- View: Alternate representations help only when discovery, equivalence, stability, and usage policy are machine-verifiable.
- Impact: Publishers can reduce waste for cooperative crawlers, but hostile or generic fleets retain incentives to consume rendered pages.
- Watch next: Standardized discovery metadata, parity signals, bot identity, robots enforcement, caching behavior, and server-side rate controls.
