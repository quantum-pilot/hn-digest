# Cloudflare outage on February 20, 2026

- Score: 140 | [HN](https://news.ycombinator.com/item?id=47103649) | Link: https://blog.cloudflare.com/cloudflare-outage-february-20-2026/

## TL;DR
Cloudflare suffered a six‑hour partial outage on Feb 20, 2026 when a buggy cleanup task in its Addressing API unintentionally withdrew ~1,100 customer BYOIP BGP prefixes. About 25% of BYOIP ranges disappeared from the Internet, breaking affected CDN, Magic Transit, Spectrum, and dedicated egress traffic; the 1.1.1.1 website errored but DNS resolution stayed up. Recovery required reverting code, dashboard re‑ads, and manual rebinding. HN discussion centers on safer API semantics, inadequate testing, and eroding confidence in Cloudflare’s reliability.

## Comment pulse
- API filters without values should not mean “all” → commenters advocate empty results or explicit errors, plus pagination, to avoid accidental mass deletions.  
- Staging and integration testing seem weak → critics say real BYOIP data would catch this — counterpoint: others argue exhaustive end‑to‑end coverage is combinatorially impossible.  
- Frequent incidents erode Cloudflare’s “reliability” brand → customers consider multi‑vendor strategies; some question the postmortem’s clarity and even joke it reads like LLM output.  

## LLM perspective
- View: This was a classic foot‑gun API plus rollout problem; stronger contracts and guardrails around destructive operations are overdue.  
- Impact: Multi‑homed or regulated customers will accelerate diversification away from single‑CDN/BGP providers and demand clearer SLOs for control‑plane reliability.  
- Watch next: Concrete “Fail Small” wins—canary config snapshots, circuit‑breakers on bulk BGP changes, plus published metrics for rollback speed.
