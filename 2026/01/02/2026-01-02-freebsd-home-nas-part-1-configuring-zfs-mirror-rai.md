# FreeBSD: Home NAS, part 1 – configuring ZFS mirror (RAID1)

- Score: 126 | [HN](https://news.ycombinator.com/item?id=46462108) | Link: https://rtfm.co.ua/en/freebsd-home-nas-part-1-configuring-zfs-mirror-raid1/

### TL;DR

Article walks through building a home NAS on vanilla FreeBSD 14.3: remote installation via SSH, manual GPT partitioning with UFS on the system disk, and creating a mirrored ZFS pool on two data disks using gpart and zpool. It covers enabling compression, autoloading ZFS on a UFS root, and hints at later parts (firewall, VPN, DNS, Samba). HN commenters highlight ZFS boot environments, argue ZFS’s integrity and snapshot advantages versus ext4/UFS, and debate its complexity for casual home admins.

---

### Comment pulse

- Boot environments on ZFS are highlighted → copy‑on‑write snapshots allow safe OS upgrades and rollback to known‑good states. — counterpoint: requires root‑on‑ZFS, not shown here.  
- Is ZFS worth it for home users? → supporters cite bit‑rot protection, cheap snapshots, easy incremental backups, simpler software RAID versus opaque hardware controllers.  
- Some lament low‑level storage tinkering in 2025 → they’d prefer turnkey stacks: storage, backups, app lifecycle, auth, isolation. — counterpoint: FreeBSD still rewards hands‑on customization.  

---

### LLM perspective

- View: This walkthrough is valuable as a reference, but most home users should start with root‑on‑ZFS to gain boot environments.  
- Impact: ZFS features matter most for irreplaceable media, VMs, and archives; casual users with solid cloud backups may see diminishing returns.  
- Watch next: Watch ecosystem trends: simpler ZFS management GUIs, FreeBSD NAS profiles, and comparisons with btrfs and modern appliance OSes for non‑experts.
