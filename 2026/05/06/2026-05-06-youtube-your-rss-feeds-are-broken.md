# YouTube, your RSS feeds are broken

- Score: 319 | [HN](https://news.ycombinator.com/item?id=48030964) | Link: https://openrss.org/blog/youtube-your-feeds-are-broken

### TL;DR

Open RSS argues YouTube’s per-channel feeds are effectively neglected: they sometimes vanish or stop updating, remain hidden behind opaque channel-ID URLs, and mix Shorts with long-form videos despite subscribers’ intent. The author sees this as part of platforms steering users toward logged-in algorithmic feeds that maximize engagement and advertising, while promising third-party replacements. HN supplied workarounds: use the channel’s UULF uploads playlist for mostly long-form items, or reload a channel page so its feed-discovery link appears. Commenters also noted that Open RSS itself returned caching errors and network restrictions.

### Comment pulse

- YouTube exposes feed metadata inconsistently → client-side navigation omits discovery, while a full page reload can restore the HTML link.
- UULF playlist feeds mostly separate regular uploads → some Shorts still leak through, so readers may need filtering.
- Open feeds preserve user-controlled subscriptions → commenters fear publicity may prompt Google to remove them — counterpoint: YouTube still operates the infrastructure.

### LLM perspective

- **View:** The core failure is product stewardship, not RSS capability; functioning endpoints without discoverability remain effectively unsupported.
- **Impact:** Feed-reader users depend on undocumented identifiers and community knowledge, increasing fragility and exclusion.
- **Watch next:** Outage duration, SPA discovery fixes, first-party content filters, rate-limit transparency, and continued endpoint availability.
