# FreeBSD 14.4-Release Announcement

- Score: 147 | [HN](https://news.ycombinator.com/item?id=47321499) | Link: https://www.freebsd.org/releases/14.4R/announce/

### TL;DR

FreeBSD 14.4, the fifth stable/14 release, is a maintenance update available across amd64, i386, Arm, PowerPC, and RISC-V targets. Highlights include OpenSSH 10.0p2 with a hybrid post-quantum key exchange enabled by default, OpenZFS 2.2.9, better cloud-init compatibility, p9fs host-directory sharing for bhyve guests, and manual-page improvements. Support runs through December 31, 2026. Commenters praised the system’s cohesive base, documentation, networking, ZFS boot environments, and simple service configuration, while debating whether new installations should choose 14.4 or 15.0.

### Comment pulse

- Version choice depends on risk tolerance → 14.4 remains reasonable before 15.1 despite 15.0 offering the newer branch.
- p9fs simplifies bhyve storage → guests can share ZFS datasets without managing large dedicated ZVOLs.
- FreeBSD’s appeal is cohesion → counterpoint: missing Docker and fewer integrations can still block development workflows.

### LLM perspective

- **View:** This release prioritizes operational polish and compatibility over headline features, fitting stable/14’s role.
- **Impact:** Existing deployments gain security and virtualization improvements without a major-version migration.
- **Watch next:** p9fs performance, Azure image availability, 15.1 guidance, and migrations before 14.3 reaches end-of-life.
