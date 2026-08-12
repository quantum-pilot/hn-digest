# Cloud VM benchmarks 2026

- Score: 325 | [HN](https://news.ycombinator.com/item?id=47293119) | Link: https://devblog.ecuadors.net/cloud-vm-benchmarks-2026-performance-price-1i1m.html

### TL;DR

Testing across 44 two-vCPU instance families and seven providers compared generic CPU, compression, web, cryptographic, and video workloads, including regional variance and January 2026 pricing. AMD EPYC Turin led raw performance decisively; AWS C8a dominated multithreaded results, while Google Axion stood out among Arm designs. Hetzner and Oracle generally delivered the strongest on-demand value, whereas AWS improved mainly through commitments or spot pricing. Because noisy neighbors, availability, geography, and workload shape results, the published ranges matter more than any single winner.

### Comment pulse

- Self-racked consumer EPYC systems can beat rented compute — counterpoint: colocation, capital, redundancy, and utilization change the payback.
- Oracle’s low prices impressed, but account handling, support, and lock-in can outweigh portable Linux VM savings.
- Readers praised the breadth while noting DigitalOcean’s old fleet and Azure’s too-late Turin release could skew provider impressions.

### LLM perspective

- **View:** Price-performance is a portfolio decision because commitments, availability, and operational trust can outweigh CPU leadership.
- **Impact:** Portable compute workloads gain negotiating leverage; stateful or provider-specific systems cannot switch on benchmark results alone.
- **Watch next:** Azure Turin, refreshed DigitalOcean hardware, repeated regional variance, and interruption-adjusted spot economics.
