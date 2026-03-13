# Big data on the cheapest MacBook

- Score: 293 | [HN](https://news.ycombinator.com/item?id=47349277) | Link: https://duckdb.org/2026/03/11/big-data-on-the-cheapest-macbook

### TL;DR
DuckDB’s team benchmarked Apple’s new entry‑level 8 GB MacBook Neo (A18 Pro) on serious analytics workloads. On ClickBench (100M‑row, 14 GB Parquet), it completed all 43 queries in under a minute on cold runs and stayed competitive with a mid‑tier AWS instance on hot runs, thanks mainly to fast local NVMe. On TPC‑DS SF300, it finished all 99 queries in 79 minutes via heavy disk spilling. Conclusion: fine for occasional local “biggish” work, but disk and RAM limit it as a daily big‑data workhorse.

---

### Comment pulse
- You can do substantial dev on modest hardware → M1 Airs, even phones with Termux, handle real projects; 8 GB Apple Silicon often feels “good enough” for many workflows.  
- Cloud economics questioned → some see results as evidence of overpriced cloud; others stress EBS vs local SSD and missing cost/performance analysis—counterpoint: bare‑metal servers still beat laptops.  
- “Big data” definition shifting → with huge RAM ceilings and fast NVMe, many once‑distributed workloads fit on one box; DuckDB/Polars rewrites can yield 40–80× speedups.

---

### LLM perspective
- View: Treat low‑end laptops as capable local analytics/dev nodes, reserving clusters or cloud only for genuinely distributed or latency‑sensitive jobs.  
- Impact: Helps solo devs and small teams avoid over‑spending on cloud when a single well‑tuned machine plus DuckDB may suffice.  
- Watch next: Benchmarks that include on‑device vs cloud cost, energy, and NVMe‑equipped instances will clarify when cloud still wins decisively.
