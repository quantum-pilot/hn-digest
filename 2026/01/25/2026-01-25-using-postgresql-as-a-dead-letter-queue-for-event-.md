# Using PostgreSQL as a Dead Letter Queue for Event-Driven Systems

- Score: 149 | [HN](https://news.ycombinator.com/item?id=46755115) | Link: https://www.diljitpr.net/blog-post-postgresql-dlq

### TL;DR

A reporting pipeline kept Kafka for ingestion but stored failed events in PostgreSQL so engineers could query, audit, and selectively replay them with SQL. Each row preserves the JSON payload, error context, status, retry count, eligibility time, and timestamps. A six-hour scheduler processes batches and marks successes, while delayed retries avoid hammering unhealthy dependencies. The design uses ShedLock for one active scheduler and FOR UPDATE SKIP LOCKED for row coordination, making failures visible and durable without adding another operational system.

### Comment pulse

- Database-backed queues suit ordinary scale → dynamic priority and ad hoc inspection often matter more than specialized throughput.
- Failure bursts can overwhelm the safety net → rate limits, circuit breakers, monitoring, cleanup, and bounded selection are essential.
- Locking choices need simplification → ShedLock serializes scheduling while SKIP LOCKED exists to permit concurrent workers.

### LLM perspective

- View: PostgreSQL is serving as an operational failure ledger, not replacing Kafka’s primary stream.
- Impact: Queryable state shortens diagnosis and makes targeted recovery routine.
- Watch next: Retry limits, poison-event handling, retention, table bloat, alerting, and whether concurrency is actually required.
