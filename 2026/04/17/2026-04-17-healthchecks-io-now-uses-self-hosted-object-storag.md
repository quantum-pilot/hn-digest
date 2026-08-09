# Healthchecks.io now uses self-hosted object storage

- Score: 135 | [HN](https://news.ycombinator.com/item?id=47806348) | Link: https://blog.healthchecks.io/2026/04/healthchecks-io-now-uses-self-hosted-object-storage/

### TL;DR

Healthchecks.io moved 14 million request-body objects—119 GB, averaging 30 uploads per second with 150-per-second spikes—from deteriorating managed storage to a dedicated Versity S3 Gateway backed by Btrfs files. The one-person operation rejected clustered MinIO, SeaweedFS, and Garage as too complex. Its server uses mirrored NVMe drives, WireGuard, two-hour rsync replication, and 30 encrypted daily off-site backups. Latency and upload queues improved, though costs rose and simultaneous drive failure could lose two hours. Hacker News clarified that retaining S3 lets three redundant web servers share data without rewriting the application.

### Comment pulse

- Versity preserves the existing S3 contract while storing ordinary files, avoiding application changes, database metadata, and heavyweight cluster operations.
- The workload fits one machine because payload loss is less critical than PostgreSQL loss — counterpoint: durability now depends on backup lag.
- Commenters initially questioned object storage at this scale; shared access across three web servers and future provider portability justified the interface.

### LLM perspective

- **View:** This is deliberately bounded self-hosting: operational simplicity and predictable latency outweighed managed-service abstraction and maximum durability.
- **Impact:** Users inspect payloads faster, the subprocessor list shrinks, and one maintainer assumes hardware, backup, and recovery responsibility.
- **Watch next:** Availability history, restore drills, growth beyond one host, deletion performance, two-hour recovery exposure, and whether managed alternatives improve.
