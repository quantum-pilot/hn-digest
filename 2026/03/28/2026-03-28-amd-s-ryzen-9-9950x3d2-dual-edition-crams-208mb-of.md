# AMD's Ryzen 9 9950X3D2 Dual Edition crams 208MB of cache into a single chip

- Score: 294 | [HN](https://news.ycombinator.com/item?id=47550878) | Link: https://arstechnica.com/gadgets/2026/03/amds-ryzen-9-9950x3d2-dual-edition-crams-208mb-of-cache-into-a-single-chip/

### TL;DR
AMD’s Ryzen 9 9950X3D2 “Dual Edition” puts 64MB of 3D V-Cache on *both* chiplets of its 16-core Zen 5 CPU, for 208MB total cache. This removes the hybrid X3D/non-X3D core split and the driver/“core parking” headaches of earlier 12–16 core X3D models, while boosting cache-sensitive gaming and simulation workloads by up to ~10% over the 9950X3D. Trade-offs: slightly lower boost clock, a 200 W TDP, and an expected premium price atop already painful DDR5 RAM costs.

---

### Comment pulse
- DDR5 sticker shock → High RAM prices make AM5/X3D upgrades hard to justify, even for enthusiasts with money—counterpoint: combo deals and falling prices soften the blow.  
- Cache vs history → People marvel that modern L3 exceeds entire 80s–90s systems; speculate about future TB-scale cache and OSes effectively “living” in cache.  
- Does cache matter? → One claim says extra cache adds ~2%, gains mostly from clocks—counterpoint: benchmarks and CFD/sim workloads see tens-of-percent speedups.

---

### LLM perspective
- View: Doubling V-Cache per chiplet simplifies scheduling and makes performance more predictable, which matters as software stacks grow more complex.  
- Impact: High-FPS gamers, scientific/engineering simulations, and latency-sensitive workloads benefit most; general users are better served by cheaper non-flagship chips.  
- Watch next: Independent benchmarks under constrained RAM, thermals at 200 W, and whether Intel responds with larger on-package caches or new tiering tricks.
