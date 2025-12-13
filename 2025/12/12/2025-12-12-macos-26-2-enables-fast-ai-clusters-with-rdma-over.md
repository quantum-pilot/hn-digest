# macOS 26.2 enables fast AI clusters with RDMA over Thunderbolt

- Score: 199 | [HN](https://news.ycombinator.com/item?id=46248644) | Link: https://developer.apple.com/documentation/macos-release-notes/macos-26_2-release-notes#RDMA-over-Thunderbolt

- TL;DR  
    - macOS 26.2 adds RDMA over Thunderbolt for Apple’s MLX framework, letting multiple M‑series Macs share tensors fast enough for true tensor parallelism, not just pipeline ‘model-splitting’. Hobbyists can chain Mac Studios into relatively cheap, high-capacity inference clusters that run multi‑trillion‑parameter models, albeit slowly, challenging GPU VRAM limits. HN debates cost vs throughput versus NVIDIA, physical and remote‑management pain of Mac clusters, and whether Apple should commercialize M‑chip clouds or focus on local, privacy‑preserving experimentation.  
    - *Content unavailable; summarizing from title and discussion only.*

- Comment pulse  
    - RDMA over Thunderbolt enables tensor parallelism in MLX → Macs can shard layers and approach N× speedup—counterpoint: Thunderbolt latency may cap scaling efficiency.  
    - Apple M3 Ultra clusters maximize memory capacity for huge models → 3TB unified RAM for ~$50k, trading throughput versus similarly priced RTX 6000 GPU workstations.  
    - Operating Mac clusters is awkward → consumer hardware, fragile Thunderbolt cabling, and GUI‑centric macOS updates complicate rackmounting, remote upgrades, and professional data‑center use.

- LLM perspective  
    - View: Apple is accidentally building an affordable inference platform where memory, not FLOPs, is the primary constraint and differentiator.  
    - Impact: Hobbyists, labs, and on‑prem privacy‑sensitive users gain a middle ground between tiny local models and expensive GPU data centers.  
    - Watch next: benchmarks of RDMA tensor parallelism, any Apple‑run M‑chip cloud, and better open‑source tooling for Mac cluster management.
