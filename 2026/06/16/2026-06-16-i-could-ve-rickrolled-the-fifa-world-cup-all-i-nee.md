# I Could've Rickrolled the FIFA World Cup. All I Needed Was My ID

- Score: 260 | [HN](https://news.ycombinator.com/item?id=48550936) | Link: https://bobdahacker.com/blog/fifa-hack

- TL;DR  
  - A security researcher registered as a FIFA agent and was silently added to FIFA’s Microsoft Entra tenant. Because backend APIs trusted any authenticated tenant user and enforced roles only in JavaScript, his “NO_ROLES” account could access FIFA’s live Football Data Platform: World Cup 2026 streaming controls, RTMP ingest URLs and keys, live analytics, commentator tools, and internal files. He could likely disrupt or hijack global broadcasts. Reporting it required calling vendors, CISA, and the FBI; FIFA quietly patched it without acknowledgment.

- Comment pulse  
  - AI-written tone ruins trust → repetitive, salesy phrasing feels like LLM output, diminishing perceived authenticity — counterpoint: tools help non-writers tell valuable stories.  
  - Responsible disclosure feels thankless → reporters invest time, sometimes money, get ghosted or rejected; even candidly exposing physical security issues has cost interview opportunities.  
  - Impact on live feed debated → RTMP stream key collision likely glitches between sources; directors might cut fast, but even seconds on-air are disastrous.

- LLM perspective  
  - View: This is a textbook failure of authorization boundaries caused by over-trusting IdP membership and frontend checks.  
  - Impact: Any organization centralizing identities must assume tenant compromise risk; every internal app needs explicit server-side role enforcement.  
  - Watch next: Expect regulators and event organizers to demand formal VDPs, 24/7 escalation paths, and audits of broadcast-chain access controls.
