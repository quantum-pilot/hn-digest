# How AWS S3 serves 1 petabyte per second on top of slow HDDs

- Score: 233 | [HN](https://news.ycombinator.com/item?id=45358280) | Link: https://bigdata.2minutestreaming.com/p/how-aws-s3-scales-with-tens-of-millions-of-hard-drives

- TL;DR
    - S3 overcomes HDD IOPS/latency limits by turning each request into many parallel ones: objects are erasure-coded and striped across many disks/servers; clients use multipart uploads and byte-range GETs; randomized “power-of-two” placement, continuous rebalancing, and hedged requests reduce hot spots and tail latency; multi-tenancy smooths bursts at scale. HN readers question the exact erasure-coding ratios and some HDD timing figures, note request-pricing economics, and underscore the key: single-object throughput exceeds a drive via parallel shard reads.

- Comment pulse
    - S3 prices haven’t fallen with HDDs → limited competition; request charges fund idle capacity to satisfy bursts.
    - 5:9 erasure coding claim is wrong → AWS uses multiple, wider codes for lower overhead, more parallelism, and AZ-failure tolerance.
    - HDD mechanics correction → full seek nearer 25ms; average seek ≠ half-distance due to acceleration/settling; uniform 1/3 model doesn’t reflect modern drives.

- LLM perspective
    - View: Parallel striping + client concurrency beats HDD IOPS limits; replication alone can’t deliver per-object throughput gains.
    - Impact: Expect more “diskless” architectures using S3 (Kafka tiered storage, Iceberg tables), trading latency for lower cost and elastic scaling.
    - Watch next: Quantify per-GET scaling vs part count; publish EC/AZ placement details; track object-store price moves and MinIO/GCS performance benchmarks.
