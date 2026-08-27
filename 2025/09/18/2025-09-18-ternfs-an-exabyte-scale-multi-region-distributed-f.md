# TernFS – An exabyte scale, multi-region distributed filesystem

- Score: 222 | [HN](https://news.ycombinator.com/item?id=45290245) | Link: https://www.xtxmarkets.com/tech/2025-ternfs/

### TL;DR

XTX Markets open-sourced TernFS, an immutable-file distributed system designed for tens of exabytes, trillions of files, and millions of clients. Its production deployment reportedly stores over 500PB across 30,000 disks, 10,000 flash drives, and three data centers while serving multiple terabytes per second without data loss. The architecture combines 256 replicated metadata shards, a cross-directory coordinator, block services, a registry, snapshots, Reed–Solomon protection, and asynchronous regional replication. Commenters questioned custom consensus, TCP-only I/O, testing rigor, and whether it is fundamentally an object store.

### Comment pulse

- Immutability simplifies correctness and scaling — counterpoint: it omits overwrites, appends, tiny-file efficiency, permissions, and fast directory mutations.
- Storage engineers asked why XTX avoided RDMA and established consensus implementations despite its performance and durability ambitions.

### LLM perspective

- View: TernFS is compelling as a workload-specific data platform whose filesystem interface hides deliberately object-like semantics.
- Impact: Open sourcing exposes rare production-scale design evidence, but adopters must match its constraints to large analytical datasets.
- Watch next: Seek failure-testing methodology, consensus proofs, independent benchmarks, recovery drills, multi-region failover, and non-XTX deployments.
