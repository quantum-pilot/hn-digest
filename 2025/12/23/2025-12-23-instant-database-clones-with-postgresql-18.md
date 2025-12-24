# Instant database clones with PostgreSQL 18

- Score: 305 | [HN](https://news.ycombinator.com/item?id=46363360) | Link: https://boringsql.com/posts/instant-database-clones/

### TL;DR
PostgreSQL has long cloned databases from templates, but v15 changed cloning to WAL-based, trading I/O spikes for slow big copies. This article shows how v18’s `CREATE DATABASE ... STRATEGY=FILE_COPY` plus `file_copy_method=clone` uses filesystem reflinks (ZFS, XFS, APFS) for near‑instant, zero‑extra‑space clones, demonstrated with a 6GB database copying in ~200ms vs 67s. It details copy‑on‑write behavior and caveats (no active connections, single filesystem, rarely available on managed services). HN commenters compare snapshot tooling and debate Postgres’ role versus other databases.

### Comment pulse
- Many are already using snapshot-based branching tools (Velo, Neon, btrfs, immutable/ClickHouse-style parts) → achieve instant clones, often with full-instance isolation.
- Teams clone RDS production into “pseudo-prod” before migrations → catches data-specific migration bugs that never show in CI; lightweight scripts keep it routine.
- Postgres often default SQL → features, extensions; some still choose MySQL/ClickHouse/Cassandra for sharding or analytics, citing MVCC issues. — counterpoint: others report excellent general-purpose reliability.

### LLM perspective
- View: Treat filesystem-backed clones as ephemeral branches, not backups; pair with logical backups and monitoring of copy-on-write growth.
- Impact: Teams with self-managed Postgres gain near-free per-test databases and safe sandboxes for risky schema or configuration experiments.
- Watch next: Cloud vendors exposing reflink-based clone APIs, plus tooling that auto-provisions and tears down clones inside CI pipelines.
