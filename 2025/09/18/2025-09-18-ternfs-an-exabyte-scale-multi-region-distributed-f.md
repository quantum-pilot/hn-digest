# TernFS – An exabyte scale, multi-region distributed filesystem

- Score: 222 | [HN](https://news.ycombinator.com/item?id=45290245) | Link: https://www.xtxmarkets.com/tech/2025-ternfs/

- TL;DR
    - XTX open-sourced TernFS, an exabyte-scale, multi-region filesystem powering ML workloads: 256 Raft-like metadata shards + CDC, per-drive block services, and a registry. Files are immutable; clients use a stateless UDP/TCP API or a Linux kernel module. Durability uses CRC32C-per-4KiB, Reed–Solomon (often 10+4), scrubbing, snapshots, and “block proofs” to contain buggy clients. Deployed across 3 data centers (500 PB on 30k disks/10k flash), it serves TB/s; limits include small-file inefficiency and CDC throughput. HN debates RDMA/TCP tradeoffs, custom consensus/testing, and object-store semantics.

- Comment pulse
    - TCP/Go block services limit NVMe bandwidth → RDMA/DPDK can hit 80–90 GB/s per node; TB/s needs many nodes — counterpoint: HDD‑bound workloads; aggregate scale helps.
    - Custom Raft-like consensus risks correctness → building LogsDB from scratch invites bugs; ask for formal verification, simulator, or chaos testing details.
    - Immutable files make it object-store-like → simplifies semantics and safety; but directory-local sharding may bottleneck huge listings versus S3-style prefix scaling.

- LLM perspective
    - View: Trade POSIX mutability for stateless APIs and safety proofs to scale reliably across regions.
    - Impact: Gives on-prem ML/HPC shops an open-source, kernel-backed, erasure-coded alternative to S3/HDFS.
    - Watch next: Benchmark RDMA vs TCP, CDC scaling, and multi-master metadata; ship NFS gateway; publish chaos-testing and durability incident reviews.
