# The death and rebirth of my home server

- Score: 121 | [HN](https://news.ycombinator.com/item?id=48966769) | Link: https://sgt.hootr.club/blog/home-server-rebirth/

### TL;DR

A blackout exposed a failing Raspberry Pi microSD card that had served as the NixOS root filesystem for years. Because service data lived mainly on external disks and configuration was declarative, recovery cost little beyond caches and torrent metadata. The rebuild reduces card writes with zram swap, tmpfs, volatile journaling, and noatime; moves service state onto a mixed-drive btrfs RAID1 pool; and adds per-service subvolumes, restic backups, and a UPS. Monitoring remains unfinished, and the author openly flags uncertainty around systemd dependencies and btrfs mount behavior.

### Comment pulse

- Most readers blamed writable flash, not Raspberry Pi hardware → suggested SSDs, USB or NVMe storage, read-only roots, disabled swap, or pre-imaged replacement cards.
- SMART helps observe wear but rarely predicts sudden death → veterans favored redundancy, tested backups, and readily available spares over scheduled replacement.
- Longevity anecdotes varied wildly → SD cards sometimes ran five years, while servers and disks survived 10–16 years, reinforcing that workload and luck dominate.

### LLM perspective

- **View:** The successful recovery came from separating reproducible configuration, service data, redundancy, and off-device backup—not from preventing every failure.
- **Impact:** Write reduction may extend card life, but moving mutable state to old disks trades one risk for others.
- **Watch next:** Verify restore drills, scrub alerts, SMART notifications, systemd ordering, usable mixed-drive RAID capacity, and behavior during another outage.
