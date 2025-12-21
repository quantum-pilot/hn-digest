# What Does a Database for SSDs Look Like?

- Score: 130 | [HN](https://news.ycombinator.com/item?id=46334990) | Link: https://brooker.co.za/blog/2025/12/15/database-for-ssd.html

### TL;DR
Brooker asks what a database designed today for SSDs and cloud hardware would look like. Updating the classic “five‑minute rule,” he argues optimal cache sizing now keeps pages hot for ~30 seconds (longer if you care about latency). SSDs are throughput‑limited above ~32kB I/O, so page and transfer sizes should center there. He proposes moving durability from local WALs to a distributed log replicated across AZs, using MVCC and accurate clocks for strong consistency and scale‑out reads, while retaining SQL, the relational model, and snapshot isolation by default.

---

### Comment pulse
- Cloud-first durability is overkill for many apps → local fsync plus async replicas give simpler, cheaper resilience; cross-AZ sync adds cost and vendor lock-in.  
- Local disks still matter → SSD commit latency beats inter-AZ RTT and helps recover from correlated failures; distributed stores are slower and complex—counterpoint: business risk often dominates microseconds.  
- This isn’t entirely new → SSD-aware engines (MyRocks, bcachefs, PMEM DBs) already optimize pages, logs, and data structures; the post underplays existing work.

---

### LLM perspective
- View: Treat local WAL+fsync and distributed logs as a tunable spectrum, not a one-size cloud doctrine.  
- Impact: On-prem and multi-cloud users need pluggable durability modes and portable log formats, not tightly coupled cloud services.  
- Watch next: Benchmarks comparing pure-local, hybrid, and fully distributed durability under realistic latencies, failures, and cost models for small vs large deployments.
