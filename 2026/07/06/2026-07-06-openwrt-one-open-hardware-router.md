# OpenWrt One – Open Hardware Router

- Score: 390 | [HN](https://news.ycombinator.com/item?id=48808482) | Link: https://openwrt.org/toh/openwrt/one

### TL;DR

OpenWrt One is a purpose-built open router using MediaTek’s Filogic 820, Wi‑Fi 6, 1GB RAM, 2.5GbE WAN, 1GbE LAN, NVMe expansion, PoE, and built-in USB‑C serial. It ships ready with LuCI and separates normal NAND storage from NOR recovery, enabling USB, initramfs, serial, and TFTP restoration even after firmware damage. HN valued long support and advanced networking beyond vendor firmware, while debating upgrade complexity versus Attended Sysupgrade and owut tooling. Alternatives included x86 OPNsense or Linux routers with separate access points and cheap used enterprise hardware; commenters considered 1GB ample.

### Comment pulse

- OpenWrt extends hardware life → community firmware continues patches and unlocks unusual setups, including parallel PPPoE sessions for public IPv6 and non-CGNAT IPv4.
- Upgrade experience remains contested → device-image sprawl and scattered documentation frustrate users — counterpoint: Attended Sysupgrade and owut now automate customized release transitions.
- Integrated appliances trade flexibility for simplicity → x86 OPNsense or Debian plus separate APs offer broader hardware choice, performance, and failure isolation.

### LLM perspective

- **View:** Recoverability and ownership matter more than benchmark leadership; documented boot paths turn firmware failure from replacement into repair.
- **Impact:** A canonical OpenWrt device reduces vendor-image fragmentation and gives maintainers hardware designed around upstream support, debugging, and unbrickability.
- **Watch next:** Wi‑Fi 7 successor, dual-2.5GbE demand, NVMe mounting fix, upgrade reliability, long-term firmware support, pricing, thermals, and real throughput.
