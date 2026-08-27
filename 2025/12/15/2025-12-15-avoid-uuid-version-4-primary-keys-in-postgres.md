# Avoid UUID Version 4 Primary Keys in Postgres

- Score: 328 | [HN](https://news.ycombinator.com/item?id=46272487) | Link: https://andyatkinson.com/avoid-uuid-version-4-primary-keys

### TL;DR

For monolithic PostgreSQL applications, random UUIDv4 primary keys scatter B-tree writes, trigger more page splits, enlarge indexes, reduce page density, and pressure the buffer cache. The author’s tests found integer leaf pages about 98% full versus 79% for UUIDv4, and dramatically more buffer accesses during a large update workload. Sequences or big integers are recommended; UUIDv7 is the compromise when distributed generation matters. Commenters stress this is workload-specific: distributed databases and sharded systems may benefit from random keys and their collision resistance.

### Comment pulse

- PostgreSQL locality favors ordered keys → smaller indexes and append-like inserts reduce memory and write amplification.
- Distributed systems may favor entropy → random keyspaces avoid hot shards and simplify independent identifier generation.
- UUIDv7 balances locality and decentralization — counterpoint: embedded time can expose creation order.

### LLM perspective

- View: Primary-key choice is an access-pattern decision, not a universal contest between integers and UUIDs.
- Impact: Teams can trade local PostgreSQL efficiency against sharding flexibility, privacy, and client-side generation.
- Watch next: Benchmark production-shaped workloads, index residency, WAL volume, shard distribution, and UUIDv7 leakage requirements.
