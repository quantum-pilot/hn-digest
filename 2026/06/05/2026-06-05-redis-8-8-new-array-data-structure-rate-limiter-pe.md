# Redis 8.8: New array data structure, rate limiter, performance improvements

- Score: 197 | [HN](https://news.ycombinator.com/item?id=48382047) | Link: https://redis.io/blog/announcing-redis-8-8/

### TL;DR

Redis 8.8 is generally available with a sparse, index-addressable array supporting ring buffers, range aggregation, and search; vendor benchmarks show 8–15% higher random-operation throughput than hashes and roughly 2× list-based ring-buffer inserts, at about 18% more memory than lists. The release also adds bounded expiring counters, stream NACKs, hash-field notifications, multi-aggregation time-series queries, selectable JSON float precision, and broad operation-specific speedups. HN questioned whether the rate limiter is really window-based and focused more on Redis versus Valkey, cloud cost, embedding, and high-availability complexity than the new APIs.

### Comment pulse

- Rate limiting → One reader traced GCRA-inspired leaky-bucket code storing one theoretical-arrival timestamp, challenging the post’s window-counter terminology.
- Fork choice → Cloud users favored Valkey for provider support and cited roughly 33% AWS savings — counterpoint: both projects continue useful development.
- Architecture → Some want SQLite-like embedding and simpler HA; others argued shared-state distribution inherently requires explicit consistency and failure tradeoffs.

### LLM perspective

- **View:** The array is a meaningful server-side primitive when workloads combine numeric indexing with bounded windows, computation, or search.
- **Impact:** Teams can replace Lua and client round trips, but adopting Redis-specific extensions deepens divergence from Valkey-compatible infrastructure.
- **Watch next:** Independent benchmarks, client-library support, persistence overhead, cluster behavior, migration compatibility, and precise documentation of rate-limiter semantics.
