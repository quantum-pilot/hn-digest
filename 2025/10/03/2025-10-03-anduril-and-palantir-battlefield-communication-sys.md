# Anduril and Palantir battlefield communication system has flaws, Army memo says

- Score: 193 | [HN](https://news.ycombinator.com/item?id=45464269) | Link: https://www.cnbc.com/2025/10/03/anduril-palantir-ngc2-deep-flaws-army.html

- TL;DR
  - An Army CTO memo deems Anduril/Palantir’s NGC2 prototype “very high risk,” citing lack of access controls, user logging, and vulnerable third‑party apps—raising chances of undetectable adversary access. Leadership framed the memo as normal vulnerability triage during prototyping; vendors had earlier touted live-fire performance. HN split: some say early DoD prototypes often defer security; others argue C2 security can’t be bolted on. One commenter notes the Army later said mitigations were applied.

- Comment pulse
  - Normal prototyping → Capability first; hardening added before fielding — counterpoint: for C2, baseline authentication, authorization, auditing must exist from day one.
  - Severity suggests design risk → Breadth of gaps implies architectural debt, not edge cases; late security integration historically causes costly delays.
  - Centralization risk → A monolithic C2 stack can enable misuse and diffuse accountability; keeping humans-in-loop and decentralized control mitigates failure modes.

- LLM perspective
  - View: Prototyping is fine, but C2 needs zero-trust-by-design; RBAC, auditing, and cross-domain controls shouldn’t be deferred.
  - Impact: ATO schedules, downselect odds, and vendor credibility; security debt may shift awards back toward incumbents with certified stacks.
  - Watch next: Independent red-team reports, RMF/ATO terms, CDS accreditation, and performance under EW/jamming during brigade-level exercises.
