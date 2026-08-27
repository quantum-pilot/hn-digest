# We built another object storage

- Score: 125 | [HN](https://news.ycombinator.com/item?id=46254087) | Link: https://fractalbits.com/blog/why-we-built-another-object-storage/

### TL;DR

FractalBits proposes AWS-hosted, S3-compatible object storage for small-object AI and analytics workloads, combining strong consistency, directory operations, atomic rename, and a Zig on-disk radix-tree metadata engine. The company reports 982K GET IOPS and 248K PUT IOPS on 4KB objects using an $8-per-hour test cluster, plus sharply lower request economics than S3 Express. Commenters questioned architecture, licensing, operations, governance, and whether batching, caching, filesystems, or databases solve the target problem more simply; published figures remain vendor benchmarks.

### Comment pulse

- Small-object storage may address real random-access and analytics needs → counterpoint: training pipelines commonly batch data and hydrate local NVMe.
- Architecture is differentiated but immature → metadata is centralized, high availability is under testing, and horizontal sharding remains planned.
- Operational confidence matters beyond IOPS → commenters want failure behavior, monitoring, deployment options, governance, and licensing clarity.

### LLM perspective

- View: The product’s wager is that preserving object APIs while removing request penalties beats application-level batching.
- Impact: Success would simplify irregular data access; failure would add another distributed system where preprocessing suffices.
- Watch next: Reproduce benchmarks, test failover and mixed workloads, clarify core-engine licensing, and compare total costs with alternatives.
