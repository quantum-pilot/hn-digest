# Big data on the cheapest MacBook

- Score: 293 | [HN](https://news.ycombinator.com/item?id=47349277) | Link: https://duckdb.org/2026/03/11/big-data-on-the-cheapest-macbook

### TL;DR

DuckDB tested a $700 MacBook Neo with an A18 Pro, 8 GB RAM, and 512 GB storage. On 100-million-row ClickBench, its local SSD produced a 59.73-second cold total and a 54.27-second hot total; cloud comparisons used network-attached disks, while a 192-core instance dominated hot runs. TPC-DS SF300 completed in 79 minutes, spilling up to 80 GB, with one query taking 51 minutes. HN praised modest hardware but cautioned against treating unlike storage setups as cloud economics.

### Comment pulse

- Lowering DuckDB's memory limit to 5–6 GB enabled out-of-core execution → constrained RAM remained workable, not invisible.
- Eight gigabytes can support real development → heavier multitasking still produces latency and memory pressure.
- “Big data” definitions shift with hardware → commenters distinguished in-memory, on-disk, and genuinely multi-machine datasets.

### LLM perspective

- **View:** The benchmark demonstrates completion and responsiveness, not daily-workload suitability.
- **Impact:** Students and analysts can explore large local datasets cheaply; sustained users need more memory and I/O.
- **Watch next:** Local-NVMe cloud comparisons, energy and cost measurements, and SSD wear under repeated spilling.
