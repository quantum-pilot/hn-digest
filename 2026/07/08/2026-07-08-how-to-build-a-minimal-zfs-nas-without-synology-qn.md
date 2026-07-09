# How to Build a Minimal ZFS NAS Without Synology, QNAP, TrueNAS (2024)

- Score: 328 | [HN](https://news.ycombinator.com/item?id=48827325) | Link: https://neil.computer/notes/how-to-setup-minimal-zfs-nas-without-truenas/

## TL;DR
A 2024 “minimal ZFS NAS” build avoids Synology/QNAP/TrueNAS by running ZFS directly on a general-purpose Linux (often Debian or NixOS) box with Docker or similar. Comments focus on hardware costs (shucked drives cheaper than NAS models), debunking ZFS myths (ECC and huge RAM not mandatory), and the complexity of secure boot (LUKS+TPM+ZFS). Others add client-integration tips (Samba, Avahi, Netatalk), propose alternative stacks (dm-integrity+mdadm+XFS, Btrfs+mdadm), and debate Synology-style convenience versus DIY ZFS reliability.

*Content unavailable; summarizing from title/comments.*

## Comment pulse
- DIY ZFS NAS is attractive, but 2024 disk and SSD prices are painful; shucked helium externals often beat “NAS” drives on price per TB.  
- Proper Avahi/wsdd2/Samba/Netatalk tuning → seamless discovery and better UX for macOS, Windows, and Linux clients; macOS still prefers AFP over its weak SMB stack.  
- Some distrust OpenZFS complexity, choosing dm-integrity+mdadm+XFS or Btrfs+mdadm instead—counterpoint: ZFS offers stronger resilience and faster, data-only rebuilds with simple drive replacement.

## LLM perspective
- View: Minimal ZFS NAS guides should prioritize clear failure-handling workflows; missing “disk X died, now what?” steps is a major gap.  
- Impact: Enthusiasts gain flexibility and features; casual users may still be safer with Synology-style appliances and vendor-supported UIs.  
- Watch next: Comparative real-world data on rebuild times, silent-corruption handling, and admin effort between ZFS and mdadm/Btrfs/XFS stacks.
