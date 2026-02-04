# Bunny Database

- Score: 238 | [HN](https://news.ycombinator.com/item?id=46870015) | Link: https://bunny.net/blog/meet-bunny-database-the-sql-service-that-just-works/

### TL;DR
Bunny Database is a managed, SQLite-compatible service built on libSQL, aiming to be a lightweight, low-cost, multi-region SQL backend that “just works.” It offers HTTP access, SDKs, automatic and manual region placement across 41 locations, and usage-based pricing with databases spinning down when idle; preview is free. Under the hood, it prioritizes operational stability over strict SQLite/libSQL feature parity. Hacker News discussion, however, questions Bunny’s reliability and transparency, citing delayed S3-compatibility promises and logging outages, and debates whether DBaaS beats self‑hosting Postgres/MySQL.

---

### Comment pulse
- Trust concerns → Missed S3-compatibility timelines and unanswered support tickets erode confidence in Bunny’s roadmap and leadership — counterpoint: storage rewrite made original schedule unrealistic.  
- Operational doubts → Multi-day log delivery delays despite “5 minutes” SLA, not shown on status page, make commenters wary of delegating critical databases to Bunny.  
- DBaaS vs self-host → Some say RDBMS is easy on a VPS; others highlight backups, security, multi‑region, and failover as non-trivial reasons to pay for managed.

---

### LLM perspective
- View: Technically appealing “SQLite for the web,” but success hinges more on operational excellence and trust than on feature checklist.  
- Impact: Most attractive to indie devs and small teams needing global read latency without running Postgres or complex infra themselves.  
- Watch next: Clear SLOs, public incident reports, automated backups, and real-world latency/cost benchmarks will determine whether this can rival Neon/Turso-class offerings.
