# MinIO is now in maintenance-mode

- Score: 384 | [HN](https://news.ycombinator.com/item?id=46136023) | Link: https://github.com/minio/minio/commit/27742d469462e1561c776f88ca7a1f26816d69e2

### TL;DR

MinIO’s repository added a maintenance notice ending feature work, enhancements, and acceptance of pull requests. Existing issues and contributions will not be actively reviewed; critical security fixes may be considered individually, and community help continues only on a best-effort basis. The notice directs customers needing active maintenance to commercial AIStor. Discussion treats the abrupt shift as an open-source trust failure and evaluates RustFS, Garage, SeaweedFS, and smaller replacements, but reports that RustFS remains unstable and some alternatives still lack replication, management, or production maturity.

### Comment pulse

- Successor maturity is uneven → Garage wins stability praise, while RustFS reportedly breaks S3 compatibility and labels itself unready for production.
- Licensing affects confidence → Apache attracts enterprise adopters, while AGPL and contributor agreements trigger sharply different reactions.
- Simple deployments remain underserved → users want early-MinIO durability without large distributed-system overhead.

### LLM perspective

- View: Maintenance mode preserves code availability but transfers roadmap, review, and security uncertainty to operators.
- Impact: Self-hosters must freeze versions, buy support, or validate a replacement under their own workloads.
- Watch next: Monitor critical patches, AIStor divergence, fork governance, S3 conformance, replication, and migration tooling.
