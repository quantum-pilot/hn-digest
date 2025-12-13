# macOS 26.2 enables fast AI clusters with RDMA over Thunderbolt

- Score: 512 | [HN](https://news.ycombinator.com/item?id=46248644) | Link: https://developer.apple.com/documentation/macos-release-notes/macos-26_2-release-notes#RDMA-over-Thunderbolt

- TL;DR  
Apple’s macOS Tahoe 26.2 adds RDMA over Thunderbolt 5, letting Macs communicate with much lower latency and enabling true tensor-parallel multi-node inference in the MLX framework. This makes high‑RAM M-series clusters attractive for running trillion-parameter models locally: relatively cheap, quiet, and power‑efficient, but with much lower throughput than NVIDIA GPU setups. HN discussion dives into pipeline vs tensor parallelism, price/performance trade-offs versus RTX/GH200, and the practical headaches of physically and remotely managing Mac-based clusters.

- Comment pulse  
  - MLX already chains Macs via pipeline parallelism; RDMA over Thunderbolt enables tensor parallelism, promising near-linear speedups if latency stays low.  
  - For ~$50k, commenters compare an M3 Ultra RDMA cluster (3 TB, ~15 t/s) against RTX and GH200 setups trading capacity for much higher throughput.  
  - Skeptics highlight Mac Studios’ awkward rackmounting, Thunderbolt cabling fragility, and GUI-heavy macOS upgrades—counterpoint: existing rack kits and automation tools partly mitigate those issues.

- LLM perspective  
  - View: RDMA over Thunderbolt turns consumer-ish Macs into credible mid-scale inference nodes, especially where memory capacity and energy efficiency matter most.  
  - Impact: Best fit is labs and startups needing on-prem, privacy-preserving LLM inference without wrestling with GPU shortages or datacenter contracts.  
  - Watch next: Watch: real-world RDMA latency, MLX tensor-parallel scaling benchmarks, Thunderbolt reliability in racks, and whether Apple ever sells M-chip cluster time.
