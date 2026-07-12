# We scaled PgBouncer to 4x throughput

- Score: 168 | [HN](https://news.ycombinator.com/item?id=48872874) | Link: https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres

- TL;DR  
  Article describes scaling PgBouncer to roughly 4x throughput by running multiple PgBouncer processes per host with SO_REUSEPORT and using PgBouncer’s built‑in “peering” feature. Peering lets processes coordinate client sessions and forward query cancellations to the correct process, avoiding lost cancels when load is spread across workers. Discussion compares alternatives like Odyssey and pgdog, touches on political concerns about Yandex tooling, and shares operational experiences running PgBouncer fleets on Kubernetes and across multiple machines.  
  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - PgBouncer vs newer proxies → Some prefer Odyssey/pgdog for scalability and sharding; others trust PgBouncer’s maturity — counterpoint: Yandex association makes Odyssey unacceptable for some.  
  - Peering and cancels → Clarification that peering is between PgBouncer processes; cancel keys can embed process IDs so the right peer forwards the signal.  
  - Deployment patterns → People run multiple PgBouncers per host or across machines (often via Kubernetes); SO_REUSEPORT and peering are core to scaling and reliability.

- LLM perspective  
  - View: Multi‑process PgBouncer with peering is a straightforward scaling layer before considering complex sharding or database engine changes.  
  - Impact: Simplifies high‑throughput Postgres for teams already using PgBouncer, reducing pressure on database nodes and avoiding massive connection counts.  
  - Watch next: Rigorous benchmarks of throughput, latency, and cancel behavior comparing PgBouncer peering to Odyssey and pgdog under mixed workloads.
