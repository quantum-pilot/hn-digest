# Show HN: I built a social media management tool in 3 weeks with Claude and Codex

- Score: 173 | [HN](https://news.ycombinator.com/item?id=47749674) | Link: https://github.com/brightbeanxyz/brightbean-studio

### TL;DR

BrightBean Studio is an AGPL, self-hostable Django platform for composing, approving, scheduling, publishing, and monitoring posts across 12 first-party social APIs, with multi-workspace RBAC, encrypted credentials, queues, inboxes, media, and deployment templates. Its author says detailed specs and parallel Claude/Codex work compressed a year-sized solo build into three weeks. CRUD and documented integrations went quickly; TikTok flows, OAuth failures, retries, UI polish, and cross-tenant authorization required manual intervention, with dangerous leaks surviving tests. Commenters questioned battle-readiness, maintenance, security, and whether self-hosting beats inexpensive SaaS.

### Comment pulse

- Target users say “built in three weeks” signals abandonment and insufficient hardening. — counterpoint: specification-first AI can cheaply produce a serious MVP.
- As code becomes abundant, support, trust, usability, customer acquisition, and API approval replace implementation as bottlenecks.
- Several wanted a calm consumer feed aggregator instead; closed platforms resist tools that weaken algorithmic control.

### LLM perspective

- **View:** The project demonstrates implementation acceleration, not elimination of product and operational work.
- **Impact:** Agencies gain ownership and unlimited workspaces but inherit credentials, upgrades, API compliance, and incident response.
- **Watch next:** Independent security review, tenant-isolation tests, publishing reliability, maintainer continuity, and documented production users.
