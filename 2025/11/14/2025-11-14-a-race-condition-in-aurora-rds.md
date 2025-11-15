# A race condition in Aurora RDS

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45929921) | Link: https://hightouch.com/blog/uncovering-a-race-condition-in-aurora-rds

- TL;DR
  - Hightouch hit an Aurora PostgreSQL failover race while upsizing: a manual failover briefly flipped writers; both tried to accept writes, storage rejected them, instances crashed, and the failover reverted. Quiescing writers let the failover succeed. AWS confirmed an internal demotion signaling bug; fix pending; current mitigation is avoiding writes during failover and monitoring for writer-role flips. HN debates how widespread this is, offers alternate log interpretations, notes AWS opacity, and observes storage preserved ACID even if orchestration faltered.

- Comment pulse
  - If failovers under write load fail, why not widespread? → Rare edge case; restarts mask issues — counterpoint: AWS said nothing unique; could affect anyone.
  - Promotion didn’t happen; watchdog killed nodes → Log order suggests storage crash message followed kill -9, not dual-writer writes.
  - Many report robust heavy-write failovers → Apps use AWS JDBC wrapper and automation; storage layer blocked concurrent writes, preserving ACID despite orchestration bug.

- LLM perspective
  - View: Treat orchestrated failover as a split-brain risk; add fencing and session invalidation to prevent stale writers.
  - Impact: Connection pools and clients must respect role changes: short TTLs, server-side read-only on demoted nodes, transaction timeouts.
  - Watch next: Track Aurora release notes for demotion signaling fix; load-test failovers; evaluate RDS Proxy/JDBC wrapper; enforce idempotent writes and retry-safe semantics.
