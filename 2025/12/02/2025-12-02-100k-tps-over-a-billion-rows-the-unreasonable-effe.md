# 100k TPS over a billion rows: the unreasonable effectiveness of SQLite

- Score: 252 | [HN](https://news.ycombinator.com/item?id=46124205) | Link: https://andersmurphy.com/2025/12/02/100000-tps-over-a-billion-rows-the-unreasonable-effectiveness-of-sqlite.html

### TL;DR

An M1 Pro benchmark argues that database architecture, not raw engine speed, dominates interactive transaction throughput. With durable SQLite settings, a mixed workload reached about 100,405 transactions per second, while local PostgreSQL at serializable isolation reached 10,026; added network latency cut the latter to 660 at 10 milliseconds. SQLite benefits from eliminating round trips and batching its single writer. The author treats this as an architectural lesson, not a universal verdict: multi-host operation, resilience, elasticity, and operational expertise can still favor PostgreSQL.

### Comment pulse

- Comparison framing remained disputed → critics saw embedded versus client-server as unfair — counterpoint: supporters said that boundary was the benchmark’s subject.
- Scale-up earned qualified praise → one host offers ample headroom but constrains failover and sudden-demand handling.

### LLM perspective

- View: The benchmark usefully isolates latency, contention, and transaction-boundary costs, while remaining hardware- and workload-specific.
- Impact: Teams may avoid needless database hops or batch operations when one machine already offers ample capacity.
- Watch next: Reproduce results on production hardware with realistic durability, failure recovery, concurrency, and latency distributions.
