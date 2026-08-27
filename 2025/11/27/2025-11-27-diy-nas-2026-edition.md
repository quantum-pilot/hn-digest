# DIY NAS: 2026 Edition

- Score: 380 | [HN](https://news.ycombinator.com/item?id=46065034) | Link: https://blog.briancmoses.com/2025/11/diy-nas-2026-edition.html

### TL;DR

The 2026 DIY NAS combines an eight-bay Jonsbo N4 case, Intel N355 Topton board, 32GB DDR5, 10GbE, mirrored NVMe storage, hard drives, and TrueNAS 25.10 in under 20 liters. The build stresses personal requirements, disk burn-in, RAID-Z2, snapshots, off-site replication, UPS support, and the warning that RAID is not backup. Benchmarks largely saturate the network, but rising component prices weaken DIY value. Commenters debated 67-watt idle draw, constrained PCIe lanes, AliExpress board reliability, alternative operating systems, and appliance economics.

### Comment pulse

- Performance fit → file-serving throughput can exceed home networks, making 10GbE the meaningful target rather than maximum NVMe speed.
- Efficiency concern → disks and feature-rich boards raise continuous power costs; measurements prompted disputed appliance comparisons.
- Reliability trade-off → compact low-cost hardware adds vendor and PCIe compromises, while burn-in cannot establish long-term reliability.

### LLM perspective

- View: The build is a documented hobby platform, not a universally optimal alternative to commercial appliances.
- Impact: Self-hosters gain flexibility and learning while assuming integration, support, power, and backup responsibilities.
- Watch next: Track drive temperatures, idle tuning, failure history, TrueNAS stability, electricity cost, and replacement-part availability.
