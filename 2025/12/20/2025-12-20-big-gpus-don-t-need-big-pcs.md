# Big GPUs don't need big PCs

- Score: 119 | [HN](https://news.ycombinator.com/item?id=46338016) | Link: https://www.jeffgeerling.com/blog/2025/big-gpus-dont-need-big-pcs

### TL;DR

Jeff Geerling benchmarked external GPUs attached to a Raspberry Pi 5 over one PCIe 3.0 lane against a modern Intel desktop. Bandwidth-heavy raw transcoding strongly favored the PC, yet ordinary Jellyfin streams, GPU-bound rendering and several larger-model LLM runs were surprisingly close. The Pi often used less whole-system power, while a four-A5000 setup reportedly reached within 2% of an Intel reference server through an external switch. Results remain workload- and driver-dependent; AMD AI and mixed-card multi-GPU tests exposed significant weaknesses.

### Comment pulse

- Readers agreed cheap, low-power hosts are attractive when GPU compute dominates, but noted memory capacity and PCIe lanes still constrain practical builds.
- Technical discussion distinguished sequential layer splitting from tensor parallelism and suggested latency, not raw transfer volume, can limit multi-GPU inference.

### LLM perspective

- View: Host size matters far less when workloads stay inside GPU memory and avoid heavy I/O.
- Impact: Efficient SBC hosts could reduce idle power and platform cost for dedicated inference or modest media servers.
- Watch next: Driver maturity, large-BAR support, gaming results, and affordable boards exposing more PCIe bandwidth.
