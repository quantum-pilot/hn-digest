# Ubiquiti: Enterprise NAS, Built on ZFS

- Score: 236 | [HN](https://news.ycombinator.com/item?id=48585866) | Link: https://blog.ui.com/article/introducing-enterprise-nas

### TL;DR

Ubiquiti’s ENAS is a 16-bay ZFS appliance built around eight Arm Neoverse N2 cores, 64GB ECC RAM, dual NVMe L2ARC slots, redundant power, dual 25GbE, open drive compatibility, and more than 1PB raw expansion. UniFi supplies identity-aware file access and license-free management; native iSCSI targets Proxmox, VMware, and Hyper-V, while centralized cross-site, rsync, cloud, and Microsoft 365 backups are promised later. HN welcomed ZFS, local control, and avoiding subscriptions, but doubted Ubiquiti’s enterprise readiness because of product abandonment, software quality, security incidents, paid support, and modest compute.

### Comment pulse

- Longevity evidence cuts both ways → some cite 15-year EdgeRouter security updates — counterpoint: others recall abandoned product lines and rushed test-in-production releases.
- License-free storage is attractive but qualified → Identity Enterprise, support, and selected integrations already carry recurring or add-on fees elsewhere in UniFi.
- ZFS cannot compensate for control-plane weaknesses → commenters cited incomplete APIs, SSH-dependent administration, account isolation failures, and ambiguous encryption claims.

### LLM perspective

- **View:** Enterprise storage is a lifecycle promise: filesystem integrity matters, but continuity, recovery tooling, audits, and predictable upgrades matter equally.
- **Impact:** UniFi customers can consolidate storage and identity; operators outside the ecosystem accept platform coupling in exchange for simpler management.
- **Watch next:** Validate sustained 25GbE throughput, rebuild times, iSCSI failover, ZFS recovery access, backup delivery, security architecture, and five-year support.
