# Garage – An S3 object store so reliable you can run it outside datacenters

- Score: 418 | [HN](https://news.ycombinator.com/item?id=46326984) | Link: https://garagehq.deuxfleurs.fr/

### TL;DR

Garage is a self-contained S3-compatible object store designed for heterogeneous machines and multi-datacenter internet links rather than maximum throughput. It replicates each data chunk across three zones and advertises operation with 1 GB RAM, 16 GB disk, under 200 ms latency, and at least 50 Mbps. Commenters praised straightforward deployment and MinIO-replacement potential, but reported lower high-speed performance, missing object tags, and a production guide warning that default LMDB metadata may corrupt after unclean shutdowns without robust filesystems and snapshots. These caveats complicate the site's broad reliability claim.

### Comment pulse

- One internal test reported roughly 5 Gbps versus MinIO's 20–25 Gbps, consistent with Garage deprioritizing peak performance.
- Operators welcomed simplicity but cautioned that power-loss recovery and metadata integrity require deliberate storage choices.
- Missing S3 object tags blocked at least one otherwise favorable evaluation.

### LLM perspective

- View: Garage optimizes geographic resilience and operability, not full S3 parity or datacenter throughput.
- Impact: Small distributed operators gain a lightweight option but inherit filesystem, backup, and compatibility decisions.
- Watch next: Benchmark recovery, metadata engines, tail latency, repair behavior, tagging support, and real three-zone failures.
