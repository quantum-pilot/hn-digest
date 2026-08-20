# Linux 7.3 improves performance when running out of vRAM

- Score: 540 | [HN](https://news.ycombinator.com/item?id=49342719) | Link: https://pixelcluster.dev/VRAM-Overcommit/

### TL;DR

A Linux/SteamOS engineer explains why VRAM overcommit becomes unstable and slow: evicted GPU data crosses PCIe, TTM lock conflicts can reject submissions, and physically contiguous display buffers can trigger gigabytes of eviction plus ping-pong restoration. SteamOS now uses hard/soft reclaim throttles and honors application memory priorities, keeping a game requesting 9GB on an 8GB GPU near 19.6ms average frames; 10GB raised variance and averaged 29.8ms. Earlier VRAM patches are queued for Linux 7.3, but the work described remains on experimental upstream branches. Commenters expect little benefit for bandwidth-bound LLM inference.

### Comment pulse

- An NVIDIA user asked about paging and defragmentation; the article’s AMD/TTM work does not establish proprietary-driver support.
- CPU-RAM freeze complaints prompted oomd, MGLRU, and earlyoom suggestions, but that is distinct from the VRAM path discussed.
- Application hints beat kernel guesswork—counterpoint: adoption varies, with D3D12 translation supplying priorities better than tested native Vulkan games.

### LLM perspective

- View: Graceful degradation requires kernel, driver, API, and application coordination, not merely a larger swap pool.
- Impact: Lower-VRAM GPUs can remain playable past nominal capacity, though PCIe bandwidth and access patterns impose hard limits.
- Watch next: Upstream scope, deadlock fixes, more games and GPUs, frametime percentiles, priority adoption, regressions, and stability.
