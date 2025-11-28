# DIY NAS: 2026 Edition

- Score: 380 | [HN](https://news.ycombinator.com/item?id=46065034) | Link: https://blog.briancmoses.com/2025/11/diy-nas-2026-edition.html

### TL;DR
An annual DIY NAS guide outlines a compact 8‑bay, sub‑20L build: Topton N22 Mini‑ITX board with Intel Core 3 N355, 10GbE, 32GB DDR5, Jonsbo N4 case, SFX PSU, dual NVMe for apps/VMs, and TrueNAS Community Edition 25.10. The parts (minus HDDs) land just under $1k, but the author stresses that disks dominate cost and reliability, and prices are rising. Benchmarks show 10GbE essentially saturated; idle power is ~67W with 8 HDDs. He auctions the finished box instead of keeping it.

---

### Comment pulse
- Power draw is high for an always‑on box → 60–70W idle with many HDDs seems wasteful vs compact appliances and cloud storage—counterpoint: most of that is spinning rust; motherboard itself is modest.

- N‑series CPUs are fine for pure NAS → but their thin PCIe budgets cripple NVMe and VM performance; used AM4/ECC platforms offer more lanes and compute at similar prices.

- Trust in AliExpress and OS stack is split → some won’t put critical data on China‑market boards; others say Topton/Jonsbo are mainstream. OS camps split between TrueNAS, vanilla FreeBSD, NixOS, and XigmaNAS.

- Annual rebuild confuses some → critics see no long‑term reliability proof; author says builds are reference designs for newcomers, not personal yearly replacements.

---

### LLM perspective
- View: This is a solid mid‑range homelab template, but overkill for “just a file server” and under‑specced for heavy virtualization.

- Impact: Buyers of N‑class NAS boards must understand PCIe and power tradeoffs versus used server/workstation platforms.

- Watch next: Compare real‑world 24/7 power and reliability of N‑class/Topton builds against Synology/QNAP and used enterprise gear over multi‑year horizons.
