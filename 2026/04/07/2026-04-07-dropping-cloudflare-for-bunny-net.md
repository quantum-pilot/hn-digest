# Dropping Cloudflare for Bunny.net

- Score: 364 | [HN](https://news.ycombinator.com/item?id=47675013) | Link: https://jola.dev/posts/dropping-cloudflare

### TL;DR

A longtime Cloudflare user moved a Phoenix blog’s registrar to Porkbun and its CDN proxy to European provider Bunny.net, mainly to reduce dependence on one US company. The guide configures a Bunny pull zone, custom hostname, TLS, origin-aware caching, Origin Shield, stale serving, and a redirect from the generated CDN domain. HTML caching makes the site fast but requires purging after publication. Bunny charges by usage with a $1 monthly minimum; the author praises its logs and support while acknowledging Cloudflare’s broader free platform.

### Comment pulse

- Readers flagged initially excessive affiliate links; the author disclosed the relationship and removed some links.
- Paying a small predictable fee clarifies the value exchange — counterpoint: paid providers can also change prices abruptly.
- Bunny offers prepaid spend protection and support; Cloudflare retains stronger integrated tooling and a formidable free tier.

### LLM perspective

- **View:** This is a practical CDN substitution, not a full replacement for Cloudflare’s edge platform.
- **Impact:** Small sites gain provider diversity with modest cost and manageable migration work.
- **Watch next:** Cache-purge race behavior, regional debugging, support quality, and portability of proprietary edge APIs.
