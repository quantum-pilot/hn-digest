# Barman – Backup and Recovery Manager for PostgreSQL

- Score: 133 | [HN](https://news.ycombinator.com/item?id=47948526) | Link: https://github.com/EnterpriseDB/barman

### TL;DR

Barman is an EnterpriseDB-maintained, Python-based disaster-recovery tool for PostgreSQL. It centralizes remote backups for multiple servers, aiming to reduce operational risk and assist DBAs during recovery in business-critical environments. The GPLv3 project moved from SourceForge to GitHub beginning with version 2.13; the repository shows version 3.18.0 released in March 2026. Its source tree includes the application, documentation, tests, and auxiliary scripts, while separate project resources provide installation guidance, downloads, community help, and professional support.

### Comment pulse

- CloudNativePG users called backup and restore solid but warned that poorly tuned WAL limits can fill volumes and halt database availability.
- An S3-support concern was corrected by users pointing to Barman Cloud and its CloudNativePG object-storage plugin.
- Commenters compared it with pgBackRest, praising native PostgreSQL utilities while noting fewer custom optimizations and some large-upload limitations.

### LLM perspective

- Recovery drills matter more than successful backup-job status alone.
- WAL growth needs monitoring, thresholds, and capacity planning alongside retention policy.
- Tool selection should weigh recovery objectives, storage targets, scale, and operator complexity.
