# Diskless Linux boot using ZFS, iSCSI and PXE

- Score: 185 | [HN](https://news.ycombinator.com/item?id=48045012) | Link: https://aniket.foo/posts/20260505-netboot/

### TL;DR

A home-lab guide boots Debian 13 on a gaming PC without repartitioning its Windows NVMe drives. A Debian/Proxmox server hosts netboot.xyz, TFTP, an authenticated iSCSI target, and a ZFS zvol; router-side dnsmasq directs PXE clients into an iPXE menu. On first boot, the menu falls back to Debian’s installer, which connects to the remote LUN and installs the whole system, including GRUB, there. Subsequent boots use `sanboot` from that same target. The author accepts slower network installation because models and other heavy data remain on local NVMe.

### Comment pulse

- Bootloader debate favored rEFInd or systemd-boot over GRUB — counterpoint: the remote-disk design avoids modifying local EFI state.
- Readers compared iSCSI’s broad OS support with NBD’s modern tooling, performance features, and weaker diskless-boot integration.
- An LTSP veteran recalled centrally updated diskless office fleets, showing the pattern scales beyond one experimental workstation.

### LLM perspective

- Availability now depends on router, server, storage pool, and network; each deserves a recovery path.
- Credentials embedded in boot scripts create exposure and rotation tradeoffs; prefer machine-specific secrets.
- Test cold boots and network interruption, not just successful installation, before trusting the setup.
