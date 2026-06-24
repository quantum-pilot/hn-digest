# The new HTTP QUERY method explained

- Score: 210 | [HN](https://news.ycombinator.com/item?id=48640974) | Link: https://kreya.app/blog/new-http-query-method-explained/

## TL;DR
HTTP QUERY is a new method for safe, idempotent requests that need a body, avoiding the long-standing, fragile practice of using GET with a body. It targets cases where parameters are too large or sensitive for URLs and where POST’s “might mutate” semantics and caching behavior are wrong. Hacker News discussion focuses on compatibility: many browsers, servers, and middleboxes already mishandle GET bodies, but a new verb may also break legacy gear and force long-delayed upgrades.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- QUERY replaces GET-with-body hacks → explicit idempotent method with body, better for sensitive parameters and avoiding POST semantics; many stacks today ignore GET bodies.  
- Middleboxes and enterprise gear may choke on QUERY → some WAFs/proxies block unknown verbs, so deployment could cause failures or accidental DoS until vendors upgrade.  
- Why not standardize GET bodies? → many legacy devices mishandle them; a new verb creates a hard break to justify upgrades — counterpoint: fix middleboxes.  

## LLM perspective
- View: QUERY mainly helps API-style requests, not traditional web pages; browser and tooling support will determine real-world impact.  
- Impact: Vendors of WAFs, API gateways, SDKs, and load balancers must add QUERY handling, logging, and policy knobs to avoid breakage.  
- Watch next: Watch for caching semantics, browser Fetch support, and major cloud APIs adopting QUERY for search/filter operations awkwardly done via POST.
