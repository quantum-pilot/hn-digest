# Avoid UUID Version 4 Primary Keys in Postgres

- Score: 328 | [HN](https://news.ycombinator.com/item?id=46272487) | Link: https://andyatkinson.com/avoid-uuid-version-4-primary-keys

### TL;DR

Andrew Atkinson argues that random UUIDv4 primary keys are a poor default for monolithic PostgreSQL OLTP applications. Their 16-byte, unordered values make B-tree indexes larger, scatter writes, increase page splits and WAL, and pressure the buffer cache. His 10-million-row experiment found 97.64% average leaf fill for integers, 79.06% for UUIDv4, and 90.09% for UUIDv7. He recommends integer or bigint sequences, using separate obfuscated public identifiers when needed, or time-ordered UUIDv7 when decentralized generation or UUID compatibility matters.

### Comment pulse

- Critics called this premature optimization — counterpoint: the author’s million-update test estimated seconds of additional memory-access latency.
- Distributed databases may prefer random keys to avoid hot shards, so the recommendation depends on storage architecture and workload.
- UUIDv7 improves PostgreSQL locality while retaining decentralized generation, but its timestamp component can disclose creation time.

### LLM perspective

- View: The article makes a strong PostgreSQL-specific case, not a universal verdict on identifier design.
- Impact: Choosing keys early affects index footprint, write amplification, cache efficiency, privacy, and future distribution.
- Watch next: Workload-specific benchmarks, PostgreSQL 18 UUIDv7 adoption, migration costs, and sharded-database comparisons.
