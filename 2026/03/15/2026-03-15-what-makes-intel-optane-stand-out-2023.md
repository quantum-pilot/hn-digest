# What makes Intel Optane stand out (2023)

- Score: 169 | [HN](https://news.ycombinator.com/item?id=47388141) | Link: https://blog.zuthof.nl/2023/06/02/what-makes-intel-optane-stand-out/

### TL;DR

Intel Optane’s 3D XPoint media occupied a rare tier between DRAM and NAND: roughly 25-microsecond random reads, direct byte-addressable overwrites, hardware power-loss protection, and exceptionally consistent write latency. P4800X offered 30 drive-writes per day; P5800X reached 100, making both strong for database logs, Ceph WAL, ZFS SLOG, caches, and VDI. Yet high prices, low capacities, platform complexity, and improving NAND prevented broad adoption before Intel ended the line in 2022. HN called it excellent technology without a sustainable market.

### Comment pulse

- Optane excelled at small random writes and durable journals → predictable latency mattered more than headline throughput for databases and storage metadata.
- Product-market fit failed → buyers preferred cheaper NAND or easier cloud services — counterpoint: specialized operators still report unmatched real-world responsiveness.
- Revival interest tracks RAM scarcity and AI demand → commenters considered Optane-like swap or cache tiers, but ecosystem and supply remain obstacles.

### LLM perspective

- **View:** Optane’s lesson is that a useful memory tier needs software defaults and distribution, not merely superior media.
- **Impact:** Storage architects lost a durable low-latency option; used inventory now serves increasingly fragile niche deployments.
- **Watch next:** CXL memory tiers, persistent-memory software support, NAND latency consistency, and any licensed 3D XPoint successor.
