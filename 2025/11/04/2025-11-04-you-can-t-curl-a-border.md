# You can't cURL a Border

- Score: 445 | [HN](https://news.ycombinator.com/item?id=45806263) | Link: https://drobinin.com/posts/you-cant-curl-a-border/

- TL;DR
  - Border decisions are opaque state machines. An iOS app, Residency, acts like a linter: simulating trips against Schengen 90/180, UK midnight counts, tax residency, passport/IDP timers, and timezone quirks—locally, with versioned rules and reproducible results. It turns “will this break later?” into specific, fixable warnings; the Iceland fare case validated the approach. HN debates the bureaucracy’s absurdities (and UK-rule nuances), the title metaphor, marketing vibes, and the engineering: DSLs, pinned tzdb, and heavy unit tests over LLM-written math.

- Comment pulse
  - Bureaucracy is arbitrary/opaque → UK uses receipt date; Home Office misses trips; EU free movement shows the contrast — counterpoint: some think it’s content marketing.
  - Overstay-to-legalization debated → common, seemingly tolerated; enables low-wage labor, while skilled workers face strict sponsorship deadlines; raises fairness and wage-suppression concerns.
  - Engineering focus matters → rolling-window math is tricky; DSLs plus unit tests recommended; LLMs struggled to implement accurate calculations; manual calendar checks build trust.

- LLM perspective
  - View: Treat jurisdictions as pluggable, versioned state machines; provenance and determinism matter more than perfect coverage.
  - Impact: Primary beneficiaries: frequent travelers, expats, global mobility teams; fewer border/tax surprises, better trip planning, and documentation readiness.
  - Watch next: Publish rule provenance and test suites; monitor tzdb and policy changes (ETIAS/ETA); consider export formats for interop with payroll/immigration tools.
