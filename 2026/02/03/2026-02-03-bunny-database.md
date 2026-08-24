# Bunny Database

- Score: 238 | [HN](https://news.ycombinator.com/item?id=46870015) | Link: https://bunny.net/blog/meet-bunny-database-the-sql-service-that-just-works/

### TL;DR

Bunny Database is a public-preview managed service built on bunny.net’s libSQL fork, offering SQLite-compatible HTTP access, SDKs, metrics, idle spin-down, and read replicas across 41 regions. Bunny claims nearby replicas cut p95 read latency by up to 99%; future pricing meters rows and regional storage, while preview accounts receive 50 free 1 GB databases. Complete SQLite/libSQL parity is not promised, and backups plus import/export remain roadmap items. Commenters debated managed convenience versus self-hosting, while prior missed S3 promises and delayed log delivery made several distrust Bunny with critical data.

### Comment pulse

- Managed value exceeds installation → replication, failover, backups, patching, monitoring, security, and regional reads consume expertise even when a database starts easily.
- Trust is the blocker → commenters cited overdue S3 compatibility and unreported logging delays — counterpoint: rebuilding storage is legitimately substantial.
- Preview gaps matter → automatic backups and file portability are not yet shipped, while compatibility follows Bunny’s chosen libSQL version rather than upstream.

### LLM perspective

- View: Attractive edge economics and locality remain product claims; preview status and missing durability features argue against critical workloads.
- Impact: Small global apps gain low-ops regional reads, but accept provider coupling, compatibility drift, metered writes, and operational trust risk.
- Watch next: Backup launch, recovery guarantees, import/export, write topology, consistency semantics, status transparency, S3 delivery, benchmarks, and post-preview pricing.
