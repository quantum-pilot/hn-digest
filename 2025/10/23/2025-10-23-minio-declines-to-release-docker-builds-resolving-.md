# MinIO declines to release Docker builds resolving CVE-2025-62506

- Score: 169 | [HN](https://news.ycombinator.com/item?id=45684035) | Link: https://github.com/minio/minio/issues/21647

### TL;DR

A MinIO GitHub issue records users' anger that official Docker images stopped receiving builds around a security-fix release. A maintainer said the decision predated the CVE and called the timing unfortunate, while participants warned that unattended or lightly managed installations could remain on vulnerable images without obvious notice. Others argued that source remains available and users can build or mirror images themselves. The thread became contentious, was locked, and leaves the practical migration and notification burden with operators and community distributors.

### Comment pulse

- Issue participants disputed whether self-building is ordinary open-source responsibility or a costly, repeated burden shifted onto users.
- Several alleged worsening lock-in and lost trust; others characterized the reaction as excessive.

### LLM perspective

- View: Distribution is part of the security contract when users depend on an official update channel.
- Impact: Ending builds without prominent deprecation signals can strand deployments even while source fixes exist.
- Watch next: Clear registry warnings, maintained community images, and verifiable upgrade guidance for existing installations.
