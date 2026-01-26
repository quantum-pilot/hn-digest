# Using PostgreSQL as a Dead Letter Queue for Event-Driven Systems

- Score: 149 | [HN](https://news.ycombinator.com/item?id=46755115) | Link: https://www.diljitpr.net/blog-post-postgresql-dlq

## TL;DR
A Kafka-based reporting pipeline pushed unprocessable events into PostgreSQL instead of a Kafka DLQ topic, turning failures into queryable rows. A simple DLQ table (JSONB payload, error metadata, PENDING/SUCCEEDED status, retry_after, retry_count) plus indexes lets engineers inspect, filter, and selectively replay failures using plain SQL. A periodic retry job uses ShedLock and `FOR UPDATE SKIP LOCKED` to safely distribute work across instances. HN largely agrees this is a pragmatic default for most workloads, with warnings about DLQ overload and lifecycle management.

## Comment pulse
- Postgres queues fit 90% of business apps → good for <100M events/day and <10k workers, with flexible prioritization and easy introspection—counterpoint: not for “extremely high scale.”
- DLQs can flood during bugs → add circuit breakers, rate limits, and strong monitoring to avoid overloading the DLQ database or silently dropping failures.
- `SKIP LOCKED` praised for work distribution → but needs LIMIT, good indexing, cleanup/partitioning, and attention to ANALYZE to avoid bad query plans and performance.

## LLM perspective
- View: Treating failures as first-class relational data brings observability, ad-hoc analysis, and targeted replays without bespoke tooling.
- Impact: Backend and data teams can operate DLQs with standard SQL skills instead of specialized Kafka/queue tooling.
- Watch next: Benchmarks comparing Postgres DLQs vs Kafka DLQs, plus patterns for automatic DLQ draining, archiving, and schema evolution on JSONB payloads.
