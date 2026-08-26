# I’m leaving Redis for SolidQueue

- Score: 291 | [HN](https://news.ycombinator.com/item?id=46614037) | Link: https://www.simplethread.com/redis-solidqueue/

### TL;DR

Rails 8’s Solid Queue lets most apps run background jobs in their existing relational database, replacing Redis and Sidekiq while simplifying deployment, monitoring, backups, scheduling, concurrency, and debugging. PostgreSQL’s `FOR UPDATE SKIP LOCKED` prevents workers contending, while Active Job makes migration mostly configuration. The author recommends it below 100 jobs/second or when 100ms latency is acceptable, retaining Redis for extreme throughput, pub/sub, or atomic counters. HN welcomed simplification but questioned benchmarks, database coupling, connection load, missing features, and whether mature GoodJob is safer.

### Comment pulse

- Database queues can exceed typical workloads → batching makes headline benchmarks misleading and leaves real unbatched transaction rates unclear.
- Active Job preserves an escape hatch → returning to Redis is straightforward, though transactional enqueue guarantees complicate later database separation.
- GoodJob appears more mature and capable → counterpoint: established Sidekiq users gain little from either option unless eliminating Redis matters.

### LLM perspective

- View: Solid Queue is an operational default, not a universal performance replacement.
- Impact: Small Rails teams trade a service for database capacity, connections, and disciplined isolation.
- Watch next: Compare unbatched throughput, failure recovery, UI behavior, batch jobs, and primary-database contention.
