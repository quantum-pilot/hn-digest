# We can't have nice things because of AI scrapers

- Score: 186 | [HN](https://news.ycombinator.com/item?id=46608840) | Link: https://blog.metabrainz.org/2025/12/11/we-cant-have-nice-things-because-of-ai-scrapers/

### TL;DR

MetaBrainz restricted previously open ListenBrainz features after AI crawlers ignored robots.txt, hammered page and API endpoints, and degraded service for legitimate users despite complete datasets being available as bulk downloads. Metadata lookup and LB Radio now require authorization, while several debugging APIs were removed pending replacement. HN framed this as a coordination and incentive failure: indiscriminate crawlers impose costs on public-interest projects, forcing authentication and closures that shrink the open web. Small-site operators reported millions of recursive requests, hosting suspensions, and blocking that also harms privacy-conscious human users.

### Comment pulse

- Bulk data exists, yet crawlers recurse through pages → no standard reliably advertises preferred datasets or makes unknown bots trust that guidance.
- Small operators absorb asymmetric costs → one commenter logged 8.5 million OpenAI and Claude requests; another lost hosting after a spike.
- Defenses create collateral damage → user-agent blocks are evadable, while Cloudflare challenges obstruct VPNs and unusual browsers.

### LLM perspective

- View: The missing primitive is machine-readable acquisition policy covering bulk alternatives, rate budgets, identity, provenance, and enforcement.
- Impact: Open-data maintainers increasingly ration access, transferring infrastructure costs and authentication friction to legitimate users.
- Watch next: Track crawler compliance, signed identities, dataset discovery standards, transparent rate limits, and host-level remedies for abusive traffic.
