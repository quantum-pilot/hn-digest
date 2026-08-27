# Instant database clones with PostgreSQL 18

- Score: 305 | [HN](https://news.ycombinator.com/item?id=46363360) | Link: https://boringsql.com/posts/instant-database-clones/

### TL;DR

PostgreSQL 18 can turn template databases into near-instant copy-on-write clones when `CREATE DATABASE` uses `STRATEGY=FILE_COPY`, `file_copy_method=clone`, and a reflink-capable filesystem such as XFS, ZFS, or APFS. In the author's test, cloning a 6 GB database took 212 milliseconds versus 67 seconds with WAL logging, initially sharing all physical blocks. Writes and vacuum gradually duplicate changed pages. Constraints include disconnecting the source, staying within one filesystem, and controlling storage unavailable on most managed services.

### Comment pulse

- Fast clones improve migration safety → production-shaped data can be tested repeatedly before deployment without lengthy restore cycles.
- Filesystem snapshots offer broader isolation → ZFS-based tools can branch whole PostgreSQL instances across older server versions.
- PostgreSQL is versatile, not universal → commenters still favor other databases for analytics, sharding, replication, or write-heavy workloads.

### LLM perspective

- View: PostgreSQL 18 productizes a proven filesystem primitive into a simple database-level testing workflow.
- Impact: Self-hosted teams can create realistic disposable environments with negligible initial storage and latency.
- Watch next: Measure clone divergence, checkpoint disruption, vacuum amplification, concurrent workflows, and recovery behavior under sustained writes.
