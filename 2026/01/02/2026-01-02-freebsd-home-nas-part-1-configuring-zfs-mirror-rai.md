# FreeBSD: Home NAS, part 1 – configuring ZFS mirror (RAID1)

- Score: 126 | [HN](https://news.ycombinator.com/item?id=46462108) | Link: https://rtfm.co.ua/en/freebsd-home-nas-part-1-configuring-zfs-mirror-raid1/

### TL;DR

The tutorial builds a FreeBSD 14.3 NAS prototype with one UFS system disk and two GPT-partitioned disks combined as a ZFS mirror. It demonstrates enabling SSH in the read-only live environment, manual installation, creating `tank`, changing its mount point, enabling LZ4 compression, and configuring ZFS at boot. HN readers highlighted boot environments, snapshots, scrubbing, checksummed integrity, and efficient incremental replication, arguing these reduce maintenance and corruption risk, while debating whether ZFS complexity and hardware expectations justify replacing simpler RAID1-plus-backup setups.

### Comment pulse

- Boot environments make upgrades reversible → ZFS snapshots permit testing patched systems and returning quickly to known-good states.
- ZFS offers more than mirroring → checksums, cheap snapshots, scrubs, and incremental send/receive address corruption and recovery.
- Simpler storage can remain adequate → occasional administrators may prefer familiar filesystems plus verified off-site backups.

### LLM perspective

- View: ZFS’s strongest home-NAS case is verifiable recovery, not merely software RAID.
- Impact: Home administrators gain powerful safeguards but must learn pool health, snapshots, replication, and replacement procedures.
- Watch next: Validate restore drills, disk-failure handling, alerts, off-site replication, and memory use on actual hardware.
