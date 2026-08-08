# How fast is a macOS VM, and how small could it be?

- Score: 216 | [HN](https://news.ycombinator.com/item?id=47984852) | Link: https://eclecticlight.co/2026/05/02/how-fast-is-a-macos-vm-and-how-small-could-it-be/

### TL;DR

Testing macOS 26.4.1 on an M4 Pro Mac mini, a Viable guest with five cores and 16 GB scored 98% of host single-core CPU and 95% of host Metal performance. Multi-core comparison was complicated by unequal allocations, while virtualized neural-engine half-precision and quantized results lagged sharply. Lightweight Safari and settings tasks remained usable at two cores and 4 GB RAM. Storage is the harder floor: volumes below 50 GB may not update reliably, so 60 GB is advised; an APFS-sparse 100 GB VM consumes about 54 GB.

### Comment pulse

- Readers debated whether lower memory use reflected fewer cores — counterpoint: macOS may simply retain fewer caches when total RAM shrinks.
- An M1 Pro experiment on two efficiency cores was slow loading pages but retained responsive spellcheck, modest typing lag, and cooler operation.
- Developers reported difficulty combining PyTorch, compute-GPU acceleration, and VM-style isolation on macOS.

### LLM perspective

- Everyday responsiveness does not predict sustained compilation, AI, or memory-pressure workloads.
- Benchmarking equal core counts would isolate RAM-driven behavior from per-core overhead.
- Sparse allocation saves initial space but does not remove update headroom requirements.
