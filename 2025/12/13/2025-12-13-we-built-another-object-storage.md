# We built another object storage

- Score: 125 | [HN](https://news.ycombinator.com/item?id=46254087) | Link: https://fractalbits.com/blog/why-we-built-another-object-storage/

### TL;DR

FractalBits proposes AWS-based bring-your-own-cloud object storage for small-object workloads, combining S3 compatibility, directories, atomic rename, and strong consistency. Its Zig metadata engine uses a full-path on-disk adaptive radix tree, while a Rust gateway serves requests. The team reports 982,000 4KB GETs and 248,000 PUTs per second on a replicated, roughly $8-per-hour cluster, plus far lower estimated request costs than S3 Express. HN pressed for architecture, governance, and failure details and disputed the premise: critics prefer batching or local NVMe; defenders need random sampling, compaction, and HTTP access across trust domains.

### Comment pulse

- The author disclosed centralized metadata, CP priorities, quorum replication, one metadata node today, pending high-availability tests, and horizontal data-node scaling.
- Batching into WebDataset, Parquet, TFRecord, or tar was proposed — counterpoint: arbitrary sampling and concurrent analytics make fixed packing or compaction costly.
- Operational maturity mattered more than peak IOPS: readers asked about monitoring, deployment, licensing, stewardship, failure behavior, and who maintains the system long-term.

### LLM perspective

- View: The product hides distributed-system complexity behind a low-latency object API; workload shape decides whether that abstraction pays.
- Impact: Teams with small-object datasets may cut request costs; sequential training pipelines may add an unnecessary storage tier.
- Watch next: Independent benchmarks, metadata failover, sharding, recovery tests, total cloud costs, compatibility, and production case studies.
