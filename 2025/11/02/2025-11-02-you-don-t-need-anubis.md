# You Don't Need Anubis

- Score: 168 | [HN](https://news.ycombinator.com/item?id=45787775) | Link: https://fxgn.dev/blog/anubis/

### TL;DR

The author argues that sites facing JavaScript-incapable LLM scrapers can replace Anubis's proof-of-work challenge with a tiny page that sets a verification cookie, avoiding a visible delay. They explicitly label the Caddy example a private-use proof of concept that can block search crawlers and non-JavaScript users, and still recommend stronger services for real DDoS attacks. Commenters contested the claim that Anubis costs attackers almost nothing, described successful production protection, noted optimized native solvers, and debated its deliberate curl exemption and arms-race role.

### Comment pulse

- Critics said proof-of-work disadvantages browsers more than optimized scrapers; defenders said current friction already prevents bot-driven outages.
- The cookie gate and Anubis both exclude non-JavaScript users, making accessibility collateral damage.
- Anubis's curl bypass is intentional for identifiable automation, though readers disputed whether hostile bots exploit it.

### LLM perspective

- View: Protection should match the observed attacker; a minimal gate is reasonable only while bots omit JavaScript.
- Impact: Small operators trade visitor compatibility and latency against keeping services online without centralized protection.
- Watch next: Bot adaptation, false positives, no-JavaScript fallbacks, search indexing, stateful rate limits, and measured server load.
