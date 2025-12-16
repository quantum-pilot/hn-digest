# Avoid UUID Version 4 Primary Keys in Postgres

- Score: 328 | [HN](https://news.ycombinator.com/item?id=46272487) | Link: https://andyatkinson.com/avoid-uuid-version-4-primary-keys

### TL;DR
The author argues against using UUID v4 as primary keys in Postgres because their randomness interacts badly with B-tree indexes: inserts cause frequent page splits and fragmentation, indexes are ~40% larger than `bigint`, cache hit rates worsen, and common operations (lookups, range scans, updates) touch vastly more pages. Benchmarks show millions more buffer hits versus `bigint` for the same workload. For most web apps, they recommend sequence-backed integers or bigints; if you truly need UUIDs, prefer time-ordered UUID v7. Obfuscation can be added on top of integers instead of using random PKs.

---

### Comment pulse
- Premature optimization vs semantics in IDs → Some say “never encode data in identifiers”; others argue UUIDv7’s timestamp bias isn’t semantic data and yields real performance gains.  
- DB- and workload-specific trade-offs → Postgres likes ordered keys, but Spanner/Cockroach/Bigtable need non-monotonic keys to avoid hot shards—counterpoint: sharded Postgres often also benefits from randomness.  
- Alternatives to UUIDv4 → Many favor UUIDv7 or encrypted/permuted integer IDs to hide counts/timestamps without random PK costs; article’s XOR/base62 scheme seen as over-engineered.

---

### LLM perspective
- View: Default to `bigint` identity PKs; add obfuscation only where user-facing, not as the storage key itself.  
- Impact: Teams gain simpler indexing, cheaper IO, and more predictable tuning; distributed systems still choose randomness where hotspotting dominates.  
- Watch next: Postgres 18 native UUIDv7, empirical benchmarks on mixed workloads, and patterns combining `bigint` PKs with public opaque IDs.
