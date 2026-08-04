# How to Build a Minimal ZFS NAS Without Synology, QNAP, TrueNAS (2024)

- Score: 328 | [HN](https://news.ycombinator.com/item?id=48827325) | Link: https://neil.computer/notes/how-to-setup-minimal-zfs-nas-without-truenas/

### TL;DR

A 2024 guide builds a GUI-free OpenZFS/Samba NAS: identify four 4 TB NVMe drives by persistent IDs, create RAIDZ1 with `ashift=12`, enable LZ4, create datasets, and expose authenticated general and Time Machine shares. Its central appeal is recoverability: pool metadata lives on the disks, so another ZFS host can import them after OS or hardware loss. The stated scope excludes encryption and backup. HN appreciated the simplicity but argued a durable NAS guide must also cover monitoring, alerts, failed-drive replacement, resilvering, discovery, capacity planning, and tested off-host recovery.

### Comment pulse

- Self-describing pools simplify host recovery → stable disk IDs prevent device-order mistakes, while on-disk topology lets replacement hosts import arrays without recreating configuration.
- Appliances sell operations, not filesystems → hot-swap labeling, audible alerts, guided replacement, updates, and recovery workflows reduce human error during stressful failures.
- Minimalism lowers complexity → direct ZFS and Samba remain understandable — counterpoint: omitted backups, encryption, health checks, and failure drills shift complexity to the operator.

### LLM perspective

- **View:** The setup is minimal only at installation; trustworthy storage requires an operational design for detection, replacement, recovery, and backup.
- **Impact:** Owning the stack improves portability and comprehension, but also makes the operator responsible for alerts, upgrades, and disaster procedures.
- **Watch next:** Add SMART/ZED alerts, scrub schedules, replacement drills, snapshot policy, remote replication, restore tests, UPS handling, and spare strategy.
