# Alternatives to MinIO for single-node local S3

- Score: 269 | [HN](https://news.ycombinator.com/item?id=49709381) | Link: https://rmoff.net/2026/01/14/alternatives-to-minio-for-single-node-local-s3/

### TL;DR

Seeking a simple, free Dockerized S3 substitute for local demos, the author tested S3Proxy, RustFS, SeaweedFS, Zenko CloudServer, Garage, Apache Ozone, and considered Ceph. SeaweedFS and S3Proxy best matched the lightweight single-node requirement; CloudServer remained plausible, RustFS promising but immature, Garage too configuration-heavy, and Ozone and Ceph excessive. Governance and bus factor remain concerns. HN updates complicated the ranking: MinIO’s maintained Silo fork, Garage’s newer single-node setup, and VersityGW offer additional practical choices.

### Comment pulse

- MinIO remains usable through Silo → users report the maintained fork works well for local S3 simulation and preserves the familiar workflow.
- Garage has become simpler → version 2.3 added automatic single-node configuration, while users report reliable multi-terabyte deployments after setup.
- VersityGW deserves inclusion → several homelab users value its simple directory backend, POSIX exposure, stability, and static-site support.

### LLM perspective

- View: Local-development suitability depends more on initialization friction and maintenance signals than distributed-storage sophistication.
- Impact: Teams can replace MinIO without redesigning applications, but should separate demo convenience from production requirements.
- Watch next: Re-test current Garage, Silo, VersityGW, and SeaweedFS releases under concurrency and failure-recovery workloads.
