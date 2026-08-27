# Do not put your site behind Cloudflare if you don't need to

- Score: 437 | [HN](https://news.ycombinator.com/item?id=45965060) | Link: https://huijzer.xyz/posts/123/do-not-put-your-site-behind-cloudflare-if-you-dont

### TL;DR

The author argues that small sites often adopt Cloudflare from disproportionate fear of DDoS attacks, then inherit a centralized failure domain they may not need. They recommend direct hosting and, for redundancy, another server behind round-robin DNS. Commenters strongly contest that simplification: inexpensive attacks, ordinary bot floods, certificates, caching, WAFs, and traffic spikes can make a CDN useful even for obscure sites. Others accept downtime for personal blogs and view avoiding Cloudflare as reducing complexity and web centralization.

### Comment pulse

- Direct-hosting advocates value autonomy and consider occasional personal-site downtime cheaper than permanent dependency.
- Cloudflare users cite real attacks, abusive scraping, easy scaling, and outsourced operations — counterpoint: bypass plans can preserve optionality.

### LLM perspective

- View: The decision depends on threat model and downtime cost, not site popularity alone.
- Impact: Small operators trade provider-wide outages and centralization for stronger filtering and lower operational burden.
- Watch next: Origin readiness, alternate DNS procedures, certificate independence, and measured bot versus provider downtime.
