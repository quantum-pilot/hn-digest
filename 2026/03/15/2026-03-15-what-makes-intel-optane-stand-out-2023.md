# What makes Intel Optane stand out (2023)

- Score: 169 | [HN](https://news.ycombinator.com/item?id=47388141) | Link: https://blog.zuthof.nl/2023/06/02/what-makes-intel-optane-stand-out/

- TL;DR  
  Intel Optane SSDs used 3D XPoint to sit between DRAM and NAND: extremely low latency (~25 µs 4K reads), rock‑steady write performance, and orders‑of‑magnitude higher endurance (30–100 DWPD) plus power‑loss protection. This made them ideal for high‑write, random‑IO workloads like databases, ZFS logs, Ceph, and vSAN caching. Hacker News discussion focuses on why such strong tech failed: high cost, confusing branding, weak ecosystem/marketing, Intel‑only lock‑in, and a cloud market that values convenience over microsecond performance.

- Comment pulse  
  Optane was technically superb → unbeatable random‑IO latency and endurance made it a “beast” for databases and journaling workloads.  
  Business failure, not tech → high cost, Intel/Micron lock‑in, no cost roadmap, muddled Optane DIMM story, poor marketing of its real benefits.  
  Misaligned with cloud reality → most workloads run on generic cloud storage; without a killer app or ecosystem, microsecond gains couldn’t justify adoption.

- LLM perspective  
  View: Optane shows that raw performance gains alone rarely overcome ecosystem, pricing, and platform-lock barriers in infrastructure markets.  
  Impact: Database, storage, and virtualization stacks lost a uniquely fast, durable tier between RAM and SSD that’s hard to replace.  
  Watch next: CXL-attached memory, high-bandwidth flash, and AI-oriented memory hierarchies may resurrect Optane-like concepts with better integration and economics.
