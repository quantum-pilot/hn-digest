# Show HN: BusterMQ, Thread-per-core NATS server in Zig with io_uring

- Score: 128 | [HN](https://news.ycombinator.com/item?id=46449812) | Link: https://bustermq.sh/

### TL;DR

BusterMQ is a very early Zig implementation of a NATS-compatible publish/subscribe server using io_uring and thread-per-core architecture. On a 16-core Ryzen 9950X, its best busy-polling and shard-routing configuration reports 6.30 million publishes and 58.74 million deliveries per second for a ten-topic, ten-publisher, 100-subscriber fan-out workload—roughly twice Go NATS throughput with much lower tail latency. HN found the numbers intriguing but questioned Bazel, the one-commit presentation, AI involvement, benchmark breadth, and project-maintenance context.

### Comment pulse

- Performance looks promising → the published workload shows substantial throughput and latency gains on consumer hardware.
- Credibility needs context → readers wanted reproducible benchmarks, history, authorship, intent, and clearer AI disclosure.
- The implementation remains narrow → core publish, subscribe, wildcards work, while queue groups and request-reply are pending.

### LLM perspective

- View: A strong localhost microbenchmark is an architecture signal, not yet evidence of production readiness.
- Impact: NATS users gain a potential high-throughput option if compatibility, durability, operations, and maintenance mature.
- Watch next: Demand independent multi-node tests, mixed payloads, connection churn, backpressure, correctness, and CPU-efficiency comparisons.
