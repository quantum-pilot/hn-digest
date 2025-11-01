# Kafka is Fast – I'll use Postgres

- Score: 533 | [HN](https://news.ycombinator.com/item?id=45747018) | Link: https://topicpartition.io/blog/postgres-pubsub-queue-benchmarks

TL;DR
- The author benchmarks “Postgres as middleware”: a Kafka‑like pub/sub built from append‑only tables + consumer_offsets, and a simple SKIP LOCKED queue. On 4‑vCPU: ~5k msg/s writes (~4.8 MiB/s) and ~25k msg/s reads (5× fanout) at ~60 ms p99 e2e; a 3‑node HA setup keeps throughput with ~186 ms p99. A 96‑vCPU box reaches ~238 MiB/s writes and 1.16 GiB/s reads but hits per‑partition write limits. Takeaway: default to Postgres/MVI until scale forces Kafka. HN debates missing Kafka baselines and operational pitfalls.

Comment pulse
- Start simple: do you need a queue? Single node + REST + retries suffice — counterpoint: polling degrades fast; queues help even at small scale.
- Postgres caveats: locks, LISTEN/NOTIFY limits, vacuum/GC, burst absorption; Redis Streams or Kafka handle fanout and backpressure better.
- Monotonic offsets are hard: sequences break under reordering; workarounds include batched reservations, no-op fills, or assigning offsets post-commit.

LLM perspective
- View: Use Postgres for modest throughput; adopt Kafka/Redpanda when bursts, cross‑team fanout, or replay needs dominate.
- Impact: Fewer systems, faster delivery; SQL visibility; defer specialized ops overhead and vendor cost.
- Watch next: Publish Kafka/Redpanda baselines, run long soak tests (vacuum/replication), explore a PG extension for durable, scalable queues.
