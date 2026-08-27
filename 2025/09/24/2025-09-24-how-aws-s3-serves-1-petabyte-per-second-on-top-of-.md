# How AWS S3 serves 1 petabyte per second on top of slow HDDs

- Score: 233 | [HN](https://news.ycombinator.com/item?id=45358280) | Link: https://bigdata.2minutestreaming.com/p/how-aws-s3-scales-with-tens-of-millions-of-hard-drives

### TL;DR

This technical explainer attributes S3’s claimed petabyte-per-second aggregate throughput to parallelism over tens of millions of inexpensive but seek-limited hard drives. It describes sequential log-structured writes, multipart uploads, byte-range reads, erasure-coded shards, speculative hedge requests, randomized “power of two choices” placement, continual rebalancing, and increasingly smooth aggregate demand at scale. Together these mechanisms spread work across clients, front ends, and storage nodes while avoiding hot disks. Some implementation details are inferred from AWS presentations, and commenters disputed the asserted universal five-of-nine erasure-coding scheme and several drive calculations.

### Comment pulse

- Readers noted S3 prices remained stable despite falling disk costs, questioning competitive pressure and margins.
- Storage specialists corrected seek-time reasoning and said AWS uses multiple erasure-code configurations rather than one fixed ratio.

### LLM perspective

- View: S3’s scale comes from coordinating abundant slow components, not making any individual disk behave like flash.
- Impact: Erasure coding serves load distribution and straggler tolerance alongside durability and capacity efficiency.
- Watch next: Authoritative details on coding ratios, ShardStore placement, rebalancing cost, and per-object rather than fleet throughput.
