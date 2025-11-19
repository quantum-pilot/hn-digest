# Do not put your site behind Cloudflare if you don't need to

- Score: 437 | [HN](https://news.ycombinator.com/item?id=45965060) | Link: https://huijzer.xyz/posts/123/do-not-put-your-site-behind-cloudflare-if-you-dont

- TL;DR  
Cloudflare’s outage led the author to argue that small, low-traffic sites shouldn’t sit behind a centralized service: it introduces a new single point of failure and deepens web centralization, while serious DDoS against tiny blogs is usually unlikely. They propose simple redundancy such as round‑robin DNS instead. HN commenters counter that cheap DDoS‑as‑a‑service, abusive bots, and traffic spikes make Cloudflare‑style protection practically necessary for many, though some admins willingly trade that off to avoid complexity and vendor dependence.

- Comment pulse  
  - Cheap DDoS hits small sites → rented bots can knock you offline; hosts may pull servers — counterpoint: some accept outages to avoid extra complexity.  
  - Bot noise justifies CDNs → scrapers overwhelm small stacks and skew analytics; CDN or cache makes spikes and media features survivable without extra ops work.  
  - Cloudflare convenience vs centralization → free, easy protection and performance, but concentrates power; some see personal use as skills practice, others fear a de‑facto gatekeeper.

- LLM perspective  
  - View: Decision should be threat‑model driven, not emotional: weigh traffic profile, risk tolerance, skills, and political stance on centralization.  
  - Impact: Small hobby sites can often stay origin‑only; commercial or controversial content sites usually benefit from CDNs plus origin‑IP hardening.  
  - Watch next: Track multi‑vendor architectures: dual CDNs, Anycast, or static hosting plus separate DDoS providers to reduce reliance on any single company.
