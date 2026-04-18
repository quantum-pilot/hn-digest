# Healthchecks.io now uses self-hosted object storage

- Score: 135 | [HN](https://news.ycombinator.com/item?id=47806348) | Link: https://blog.healthchecks.io/2026/04/healthchecks-io-now-uses-self-hosted-object-storage/

### TL;DR
Healthchecks.io stores up to 100 kB of each POSTed ping body; small ones live in Postgres, larger ones in S3-compatible storage. After years of flaky performance with OVH and UpCloud (and rejecting AWS for per-request pricing and CLOUD Act concerns), the solo maintainer switched to self-hosted object storage: Versity S3 Gateway on top of Btrfs and mirrored NVMe. Latency and queues dropped significantly, durability is “good enough” via rsync and daily off-site backups, and costs rose but reliability and control improved.

---

### Comment pulse
- New S3 option → Versity S3 Gateway surprises many; seen as a simpler alternative to MinIO/Garage for small deployments—counterpoint: single-node durability remains a concern.  
- Why still S3? → Keeping the S3 API avoids app rewrites, keeps multi-web-server access simple, and preserves portability back to cloud storage.  
- Alternatives and praise → Garage is recommended for self-hosters, while long-time users praise Healthchecks.io’s reliability and the maintainer’s careful infrastructure choices.

---

### LLM perspective
- View → For sub-terabyte, latency-sensitive workloads, single-node S3 gateways over a solid filesystem can beat managed object storage in practice.  
- Impact → Small SaaS operators gain a viable middle ground: S3 semantics, simpler ops than distributed clusters, and better control over data location.  
- Watch next → Track Versity’s stability under failures, compare against NFS + app changes, and benchmark multi-node or ZFS/Btrfs variants for future scaling.
