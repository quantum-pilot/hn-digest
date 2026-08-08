# Securing a DoD contractor: Finding a multi-tenant authorization vulnerability

- Score: 156 | [HN](https://news.ycombinator.com/item?id=48012162) | Link: https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup

### TL;DR

Security vendor Strix says its autonomous testing agent found that Schemata, a military-training platform with DoD contracts, failed to scope several API endpoints by tenant. An ordinary account could enumerate users, organizations, courses, service members’ bases and emails, obtain direct links to sensitive training documents, and potentially reach write-enabled routes. Strix stopped testing, began disclosure on December 2, 2025, and says Schemata acknowledged and fixed the endpoints only after a final notice on May 1, 2026. HN blamed basic startup security gaps and questioned what compliance certifications actually prove.

### Comment pulse

- Authorization failures remain common at startups → product speed and generalist teams often outrank platform, database, and security expertise.
- Automated white-box testing can outperform costly engagements → one commenter reported better $50 results — counterpoint: the $10,000 comparison used a harder grey-box scope.
- Security badges can create false reassurance → commenters doubted cursory audits would catch tenant-isolation failures or sustain credibility after breaches.

### LLM perspective

- **View:** The failure was architectural, not exotic; every data-access path needed server-side tenant authorization.
- **Impact:** Affected customers need exposure timelines, log review, notification decisions, and evidence that write operations were not abused.
- **Watch next:** Independent remediation verification, incident reporting under applicable DoD rules, audit-log findings, and improved vulnerability-intake procedures.
