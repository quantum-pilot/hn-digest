# I’m leaving Redis for SolidQueue

- Score: 291 | [HN](https://news.ycombinator.com/item?id=46614037) | Link: https://www.simplethread.com/redis-solidqueue/

### TL;DR
Rails 8 drops Redis as the default for jobs, caching, and ActionCable, replacing it with SolidQueue, SolidCache, and SolidCable backed by your relational database. The article argues most apps don’t need Redis-level throughput or sub-millisecond latency and pay unnecessary complexity: extra infra, HA, backups, monitoring, and mental overhead. SolidQueue uses `FOR UPDATE SKIP LOCKED`, recurring schedules, and DB-based semaphores for concurrency, plus a UI (Mission Control). HN discussion questions SolidQueue’s maturity, compares it to GoodJob, and debates scaling and operational tradeoffs.

---

### Comment pulse
- GoodJob vs SolidQueue → many prefer GoodJob for Postgres: mature, readable, feature-rich; SolidQueue seen as constrained by MySQL-friendly “universal SQL”. — counterpoint: portability helps multi-DB Rails.
- Simplifying infra welcomed → for typical Rails volumes, dropping Redis and Sidekiq is attractive; Active Job lets apps swap back to Redis-backed queues if SolidQueue becomes a bottleneck.
- Scaling/DB load debated → SKIP LOCKED and leases avoid long locks, but shared-DB queues need careful connection pooling and can’t match Redis for extreme pub/sub or latency.

---

### LLM perspective
- View: Rails is codifying “boring tech first”: default to the main RDBMS; add Redis only when metrics prove it’s needed.
- Impact: Smaller teams gain from fewer moving parts; DB capacity planning and observability now implicitly include job workloads.
- Watch next: Independent benchmarks, SolidQueue vs GoodJob adoption patterns, and how far Mission Control evolves toward Sidekiq-grade operational tooling.
