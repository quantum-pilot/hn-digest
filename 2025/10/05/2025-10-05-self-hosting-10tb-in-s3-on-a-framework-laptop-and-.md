# Self hosting 10TB in S3 on a framework laptop and disks

- Score: 179 | [HN](https://news.ycombinator.com/item?id=45480317) | Link: https://jamesoclaire.com/2025/10/05/self-hosting-10tb-in-s3-on-a-framework-laptop-disks/

### TL;DR

The author describes running roughly 10TB of S3-compatible storage on a secondhand, screenless Framework laptop, using Ubuntu, ZFS over USB-attached JBOD disks, and Garage. After four unattended months, restarts, upgrades, and a Garage major-version migration reportedly worked. Heavy I/O initially exposed problems when SQLite metadata lived on the USB array; moving metadata to the laptop fixed them. The setup uses raidz1 and lacks an offsite replica, making this an encouraging personal experiment rather than proof of long-term durability.

### Comment pulse

- Garage users praised its compatibility with common S3 tools and low-maintenance operation.
- Commenters warned that USB cabling and RAID redundancy do not replace independent backups.

### LLM perspective

- View: Commodity hardware can serve substantial personal object storage when failure assumptions are explicit.
- Impact: Separating latency-sensitive metadata from USB storage may matter more than raw disk capacity for stability.
- Watch next: Longer uptime, restore tests, drive failures, and an affordable offsite copy will determine resilience.
