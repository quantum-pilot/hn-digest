# Barman – Backup and Recovery Manager for PostgreSQL

- Score: 133 | [HN](https://news.ycombinator.com/item?id=47948526) | Link: https://github.com/EnterpriseDB/barman

## TL;DR
Barman is an open‑source, Python-based backup and disaster recovery manager for PostgreSQL, supporting remote backups of multiple servers and maintained by EnterpriseDB. It integrates tightly with PostgreSQL’s native backup tools and is widely used with CloudNativePG in Kubernetes to stream WAL and store backups in object storage (e.g., S3). Discussion centers on tuning WAL limits in K8s, Barman’s now‑mature S3/cloud support, trade‑offs versus pgBackRest, and alternative tools emerging after pgBackRest’s temporary archival.

---

## Comment pulse
- Barman via CloudNativePG in Kubernetes is reliable → but WAL volume limits must be tuned and monitored or WAL growth will stop the database for safety.
- Earlier Barman felt disk-only, pushing users to pgBackRest for S3 → modern Barman Cloud and CNPG plugins add solid object-store support — counterpoint: non-cloud backups need separate setups.
- Barman uses PostgreSQL’s own backup utilities → reduces maintenance across PG versions but sacrifices some custom optimizations; pgxbackup and Databasus cover other niches in the ecosystem.

---

## LLM perspective
- View: Design around native Postgres tooling is strategically wise; lowers coupling to internal formats and version churn.
- Impact: CloudNativePG users, managed Postgres vendors, and self-hosters gain a de facto standard backup stack post-pgBackRest uncertainty.
- Watch next: Track performance improvements, S3 storage-class controls, and whether pgxbackup or successors maintain competitive features and community governance.
