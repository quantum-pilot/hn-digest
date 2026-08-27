# Go ahead, self-host Postgres

- Score: 394 | [HN](https://news.ycombinator.com/item?id=46336947) | Link: https://pierce.dev/notes/go-ahead-self-host-postgres#user-content-fn-1

### TL;DR

Pierce Freeman argues that many teams overpay for managed Postgres despite using essentially the same open-source engine wrapped in operational tooling. After two years self-hosting a database serving thousands of users and tens of millions of daily queries, he reports low maintenance, lower cost and more tuning control. The article outlines memory, pooling, NVMe and WAL settings, while acknowledging responsibility for incidents, backups and compliance. Its broad recommendation rests mainly on one operator’s experience, so availability needs and staffing can reverse the calculation.

### Comment pulse

- Debate centered less on technical feasibility than responsibility: managed services can transfer blame and labor without eliminating application-level incidents.
- Critics said backups, failover, monitoring and specialist coverage justify managed pricing; supporters countered that ordinary workloads rarely need extreme availability.

### LLM perspective

- View: Hosting choice is an ownership and risk decision disguised as a simple infrastructure price comparison.
- Impact: Teams with modest availability needs and operational competence may capture large savings and better observability.
- Watch next: Verified recovery drills, true staff time, off-provider backups, and failure costs—not monthly instance prices alone.
