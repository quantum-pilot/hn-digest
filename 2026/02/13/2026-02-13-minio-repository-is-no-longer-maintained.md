# MinIO repository is no longer maintained

- Score: 442 | [HN](https://news.ycombinator.com/item?id=47000041) | Link: https://github.com/minio/minio/commit/7aac2a2c5b7c882e68c1ce017d8256be2feea27f

- TL;DR  
MinIO has archived its GitHub repository and explicitly marked it as “no longer maintained.” The AGPLv3-licensed code and historical binaries remain available but are unsupported and “use at your own risk.” MinIO now points users to its proprietary AIStor Free and AIStor Enterprise products instead. HN commenters are scrambling to evaluate or migrate to alternatives like Ceph, RustFS, SeaweedFS, Garage, and NVIDIA AIStore, while debating open‑source sustainability, contributor license agreements, and the high operational cost of switching core storage infrastructure.

- Comment pulse  
Ceph and a few others emerge as go‑to replacements → Ceph praised as battle‑tested; RustFS fast and simple; SeaweedFS and RustFS draw distrust over code quality and CLA.  
MinIO’s closure sparks COSS debate → some say free‑rider problem makes this inevitable; others call it a bait‑and‑switch that undermines trust in “FOSS” vendors.  
Infra lock‑in risk is highlighted → many had no migration runbook; object‑store swaps mean multi‑week data moves and subtle S3‑compat differences only visible under production load.

- LLM perspective  
View: Treat self‑hosted object storage as a strategic dependency; always maintain a tested migration path between at least two S3‑compatible systems.  
Impact: Enterprises on MinIO must choose between freezing on unsupported bits, buying AIStor, or absorbing migration pain to another platform.  
Watch next: Which OSS S3 store gains momentum (Ceph, RustFS, Garage, others), and whether new licensing/governance models emerge to avoid repeats.
