# The death and rebirth of my home server

- Score: 121 | [HN](https://news.ycombinator.com/item?id=48966769) | Link: https://sgt.hootr.club/blog/home-server-rebirth/

### TL;DR
A Raspberry Pi 4 home server died when its microSD card finally gave out, likely finished off by a recent power outage. The author rebuilds the setup around durability: minimizing SD writes (zram swap, tmpfs /tmp, in‑memory logs, noatime), moving all heavy I/O to a btrfs RAID1 pool of mixed old HDDs, and wiring NixOS modules to auto-create subvolumes and restic/S3 backups per service. HN comments debate SD cards on Pis, alternatives like SSDs/NUCs, and realistic expectations for hardware lifetimes and monitoring.

---

### Comment pulse
- SD as root on a Pi is fragile → flash wears quickly under unpredictable writes and power loss; better to use SSD, USB3, Optane, or read‑only root.
- Some report years of trouble‑free Pis → careful I/O patterns and swap off keep reputable uSD cards alive—counterpoint: pushes more complexity onto inexperienced users.
- Hardware life is long but random → HDDs can run >10 years; SMART rarely predicts sudden failures, so redundancy and backups matter more than lifespan daemons.

---

### LLM perspective
- View: Treat SD cards as bootloaders only; put mutable data and services on more durable, monitorable storage layers.
- Impact: Home server builders get closer to datacenter patterns: RAID, snapshots, backups, and declarative config, even on tiny SBCs.
- Watch next: Turn the ad‑hoc monitoring ideas into a minimal Prometheus/Grafana stack plus automated alerts for btrfs and SMART anomalies.
