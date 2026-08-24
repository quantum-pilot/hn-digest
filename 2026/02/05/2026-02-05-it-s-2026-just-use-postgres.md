# It's 2026, Just Use Postgres

- Score: 519 | [HN](https://news.ycombinator.com/item?id=46905555) | Link: https://www.tigerdata.com/blog/its-2026-just-use-postgres

### TL;DR

Tiger Data argues that most companies should consolidate search, vectors, time series, caching, documents, queues, geospatial work, and scheduled jobs in PostgreSQL through extensions, reducing synchronization, operations, credentials, backups, and failure modes. It presents code examples and vendor benchmarks, claiming specialized systems are rarely necessary until measured scale exposes a real limit. Commenters largely reframed this as “Postgres by default,” not “Postgres exclusively,” citing SQLite for local simplicity and purpose-built systems for demanding workloads. Others challenged the article’s economics, technical equivalences, promotional framing, and apparently AI-generated style.

### Comment pulse

- Default beats dogma → start with Postgres until measurements justify specialization — counterpoint: extensions can impose substantial tuning and operating costs.
- Workload determines simplicity → Postgres suits shared applications; SQLite excels locally, while scaled analytics or caching may reward purpose-built systems.
- Presentation damaged trust → an HN moderator buried the post for seeming AI-generated, though commenters noted detection and authorship remain uncertain.

### LLM perspective

- View: PostgreSQL is a strong consolidation default, but the article’s 99% claim outruns its vendor-supplied comparisons and workload nuance.
- Impact: Consolidation reduces integration overhead; overconsolidation can shift complexity into tuning, extensions, scaling, and a larger failure domain.
- Watch next: Workload-specific benchmarks, extension maturity, operational staffing, replication costs, observed bottlenecks, SQLite suitability, and justified specialist adoption.
