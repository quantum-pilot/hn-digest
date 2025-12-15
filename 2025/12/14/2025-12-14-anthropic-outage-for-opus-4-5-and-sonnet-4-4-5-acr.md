# Anthropic Outage for Opus 4.5 and Sonnet 4/4.5 across all services

- Score: 172 | [HN](https://news.ycombinator.com/item?id=46267385) | Link: https://status.claude.com/incidents/9g6qpr72ttbr

### TL;DR
Anthropic’s Claude Opus 4.5 and Sonnet 4/4.5 suffered a roughly 80-minute outage caused by a network routing misconfiguration that blackholed traffic to some inference backends. Engineers reverted the bad route and pledged better synthetic monitoring and visibility into high-impact infra changes. HN commenters praised unusually fast, honest status updates, while also noting how dependent they’ve become on LLMs for daily work. Some users saw the outage misreported as a quota/upgrade message and noticed odd, overlong responses before failure.

---

### Comment pulse
- Timely incident comms are rare → Users appreciated near-real-time status updates, avoiding wasted debugging—counterpoint: many status pages update, just not in the crucial first minutes.  
- Root cause clarity → Engineers described an overlapping route advertisement, 75-minute detection, and plans to improve synthetic checks and change visibility for faster catch/rollback.  
- Outage as “intelligence brownout” → Jokes and concern about centralized LLM dependence; confusing quota-style error and strange verbose outputs highlighted UX and robustness gaps.

---

### LLM perspective
- View: Treat LLM platforms like critical SaaS; transparent incidents and postmortems are now table stakes, not nice-to-haves.  
- Impact: Heavy AI-assisted developers and teams need clear error semantics, not misleading quota/upgrade prompts, during infra incidents.  
- Watch next: Better multi-provider failover, synthetic “canary” prompts, and standardized LLM outage/error signaling across vendors.
