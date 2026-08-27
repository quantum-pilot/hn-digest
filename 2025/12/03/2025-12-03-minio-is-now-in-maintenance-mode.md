# MinIO is now in maintenance-mode

- Score: 384 | [HN](https://news.ycombinator.com/item?id=46136023) | Link: https://github.com/minio/minio/commit/27742d469462e1561c776f88ca7a1f26816d69e2

### TL;DR

MinIO’s repository now says the project is maintenance-only and accepts no new features, enhancements, or pull requests. Existing issues and pull requests will not be actively reviewed; critical security fixes may be considered individually, and community help continues on a best-effort Slack basis. Users seeking active maintenance are directed to commercial AIStor. Discussion treats the abrupt boundary as an effective end to the community edition’s development and surveys alternatives including Garage, SeaweedFS, RustFS, and smaller projects, while repeatedly questioning production maturity and compatibility.

### Comment pulse

- RustFS drew interest for rapid releases and Apache licensing — counterpoint: one client maintainer reported severe compatibility failures.
- Garage was described as steadier for distributed use, while SeaweedFS may be capable but excessive for simple deployments.
- Some contributors framed the change as a licensing-governance failure and warned against projects requiring broad contributor agreements.

### LLM perspective

- View: Maintenance mode converts MinIO from an evolving dependency into a migration risk with uncertain security coverage.
- Impact: Self-hosters must compare correctness, S3 compatibility, replication, and governance rather than feature lists alone.
- Watch next: Test alternatives against real workloads and failure recovery before the current MinIO release becomes operationally untenable.
