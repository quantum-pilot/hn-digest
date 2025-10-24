# MinIO declines to release Docker builds resolving CVE-2025-62506

- Score: 169 | [HN](https://news.ycombinator.com/item?id=45684035) | Link: https://github.com/minio/minio/issues/21647

TL;DR
MinIO addressed CVE-2025-62506 but stopped publishing official Docker images and binaries for its community edition, declaring it source-only. Maintainers say the decision predated the CVE; critics call the timing a rug-pull that leaves 1B+ Docker pulls stranded on a vulnerable image and breaks auto-updates. Some argue “build it yourself,” while ops teams note compliance, notification, and maintenance burdens. Paying customers get AIStor builds and LTS; non-customers must compile via Go. Downstreams are disabling MinIO; trust concerns and calls for prominent deprecation warnings dominate.

LLM perspective
- View: Source-only flip during a security patch trades convenience for funneling to paid builds; expect mirrors, forks, and third-party images.
- Impact: Breaks update pipelines, increases unpatched exposure and compliance overhead; may accelerate migrations to Ceph, SeaweedFS, or managed S3.
- Watch next: DockerHub deprecation warnings, community-maintained images, potential fork, vendor licensing shifts, and any exploitation reports of CVE-2025-62506.
