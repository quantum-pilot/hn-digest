# Kafka is Fast – I'll use Postgres

- Score: 533 | [HN](https://news.ycombinator.com/item?id=45747018) | Link: https://topicpartition.io/blog/postgres-pubsub-queue-benchmarks

### TL;DR

Benchmarks implement Kafka-like pub-sub logs and work queues atop PostgreSQL, arguing familiar infrastructure can cover many modest workloads. A replicated three-node, four-vCPU setup sustained about 5,000 1 KiB writes and 25,000 fan-out reads per second; its queue handled roughly 2,400 messages per second. Larger tests reached much higher throughput but exposed partition, client, storage, and efficiency limits. The author recommends PostgreSQL as minimum viable infrastructure until requirements justify Kafka, while conceding Kafka's scaling, schema evolution, ecosystem, and efficiency advantages.

### Comment pulse

- Supporters favored reusing an existing database to avoid another system's operational and organizational costs.
- Critics noted short tests, absent Kafka baselines, storage growth, vacuuming, lock semantics, weak queue scaling, and dramatically poorer efficiency.

### LLM perspective

- View: The useful claim is “Postgres may be sufficient,” not “Postgres performs like Kafka.”
- Impact: Small teams can defer distributed infrastructure, but must isolate messaging load and plan retention before it threatens transactional work.
- Watch next: Run long-duration comparative tests covering failures, replay, retention, schema changes, backpressure, vacuuming, and total cost.
