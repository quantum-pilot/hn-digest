# Stop crawling my HTML – use the API

- Score: 111 | [HN](https://news.ycombinator.com/item?id=46265579) | Link: https://shkspr.mobi/blog/2025/12/stop-crawling-my-html-you-dickheads-use-the-api/

### TL;DR

The author argues crawlers should discover machine-readable alternatives advertised in page metadata instead of repeatedly parsing HTML. Their WordPress site exposes JSON, ActivityPub, oEmbed, plain-text resources, and a sitemap; OpenBenches similarly publishes GeoJSON and an API, yet automated crawlers still hammer rendered pages. Commenters counter that HTML is the human-visible canonical output and works universally, whereas APIs are inconsistent, incomplete, or later restricted. The deeper consensus is that abusive volume and ignoring crawler controls matter more than representation choice alone.

### Comment pulse

- WordPress, MediaWiki, and other common systems may justify special handling, but arbitrary API discovery and schema interpretation add substantial complexity.
- APIs reduce parsing and bandwidth when faithful; counterpoint: stale or summary-only feeds can diverge from what readers actually see.

### LLM perspective

- View: Alternate-resource metadata is useful progressive optimization, not a universal replacement for standards-compliant HTML crawling.
- Impact: Publishers bear avoidable load when crawlers ignore available structured endpoints, caching, identification, and robots directives.
- Watch next: Standardize discovery, freshness equivalence, rate signaling, and fallback behavior across major crawler implementations.
