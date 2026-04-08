# Dropping Cloudflare for Bunny.net

- Score: 364 | [HN](https://news.ycombinator.com/item?id=47675013) | Link: https://jola.dev/posts/dropping-cloudflare

## TL;DR

An Elixir/Phoenix blogger describes moving from Cloudflare to Bunny.net mainly to avoid dependence on a single US infrastructure giant and to support an EU-based alternative. Bunny is used as a drop‑in CDN replacement for Cloudflare’s “orange cloud,” while the domain registrar moves to Porkbun. The post walks through creating a Bunny pull zone, configuring DNS, tuning caching (including caching HTML with `s-maxage`), enabling Origin Shield and stale-cache settings, and adding redirect edge rules. HN discussion centers on affiliate-link transparency, free vs. paid infra, lock‑in, support, and billing risk.

---

## Comment pulse

- Affiliate links must be clearly disclosed → otherwise endorsements can violate FTC/UK guidance; readers expect explicit “I earn from…” disclaimers.  
- Preference for small paid providers → clearer value exchange, better support, prepaid billing avoids surprise-bill disasters — counterpoint: CDNs/DNS are easy to switch, free tiers lower startup friction.  
- Cloudflare Workers/Pages offer excellent DX and powerful free tier → but multi-layer edge caching is hard to debug; Bunny competes on simplicity, observability, and responsive support.

---

## LLM perspective

- View: This reflects a broader push away from mega-platform monoculture toward multiple, regionally diverse infra providers.  
- Impact: Indie devs and small SaaS gain more pricing predictability, jurisdictional choice, and operational clarity at the cost of some platform features.  
- Watch next: Benchmark Bunny’s edge/runtime stack vs Cloudflare; track S3-compatible storage launch, WinterCG/WinterTC adoption, and any pricing or free-tier shifts.
