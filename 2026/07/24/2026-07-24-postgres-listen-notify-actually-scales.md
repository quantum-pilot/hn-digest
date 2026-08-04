# Postgres LISTEN/NOTIFY actually scales

- Score: 174 | [HN](https://news.ycombinator.com/item?id=49040296) | Link: https://www.dbos.dev/blog/postgres-listen-notify-scalability

### TL;DR

Postgres LISTEN/NOTIFY stalls when every write emits a notification: each notifying transaction takes a global exclusive lock through commit and fsync to preserve notification order, limiting the authors’ first design to 2.9K stream writes per second. Treating notifications as wake-up hints let them buffer and batch NOTIFY calls, keep rows as the source of truth, and use slow polling for crash recovery. Their benchmark reached 60K writes per second at 15–100 ms latency. HN found the pattern useful but stressed workload fit, hardware disclosure, traffic bursts, and operational headroom.

### Comment pulse

- Scaling is contextual → commenters favored matching anticipated load with margin, avoiding both undersized primitives and costly infrastructure built for hypothetical millions.
- Benchmark context weakens the headline → tests reportedly used 96 cores and 384 GB RAM; network placement, redundancy costs, and burst behavior remained unspecified.
- Historical framing drew pushback → critics said the earlier warning had been corrected — counterpoint: Postgres 19 still leaves this global-lock bottleneck intact.

### LLM perspective

- **View:** This is database-backed signaling, not a durable queue: correctness comes from table state, while notifications optimize freshness.
- **Impact:** Teams can postpone another messaging service when Postgres capacity and latency targets fit, reducing deployment and consistency complexity.
- **Watch next:** Reproduce results on ordinary hardware, inject crashes and bursts, measure recovery delay, then load-test with realistic readers.
