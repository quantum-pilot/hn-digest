# Diskless Linux boot using ZFS, iSCSI and PXE

- Score: 185 | [HN](https://news.ycombinator.com/item?id=48045012) | Link: https://aniket.foo/posts/20260505-netboot/

### TL;DR
Author sets up a fully diskless Debian 13 environment for a Windows gaming PC, booting over the network from a ZFS-backed iSCSI volume via PXE and netboot.xyz. Proxmox hosts ZFS and iSCSI, an Asus router with dnsmasq handles DHCP/TFTP redirection, and a custom iPXE script sanboots the iSCSI LUN or falls back to the Debian netinstaller. This keeps Windows disks untouched, centralizes GRUB on the NAS, and makes OS rebuilds easy, at the cost of slower installs.

---

### Comment pulse
- GRUB is overcomplicated → rEFInd, systemd-boot, or ZFSBootMenu offer simpler, EFI-native boot flows with fewer moving parts and easier recovery—counterpoint: rEFInd’s auto-discovery can feel bloated.
- UEFI entries rarely need manual updates → most setups use GRUB or a stable EFI-stub filename; simple scripts or hooks can atomically swap kernels without touching NVRAM.
- iSCSI vs NBD for network root → iSCSI widely supported and stable across OSes; NBD has improved performance/specs but tooling and initramfs support still lag for diskless boot.

---

### LLM perspective
- View: Network-booted Linux lets you keep a “clean” CUDA/LLM environment while leaving a gaming Windows install untouched.
- Impact: Home labs gain datacenter-like PXE/iSCSI workflows for model experimentation, snapshots, and quick OS rollbacks on shared hardware.
- Watch next: Robust NBD/dracut support, turnkey PXE+iSCSI+ZFS kits, and guides for mixing this with GPU passthrough and model storage on fast local NVMe.
