# macOS 26.2 enables fast AI clusters with RDMA over Thunderbolt

- Score: 512 | [HN](https://news.ycombinator.com/item?id=46248644) | Link: https://developer.apple.com/documentation/macos-release-notes/macos-26_2-release-notes#RDMA-over-Thunderbolt

### TL;DR

macOS 26.2 adds RDMA over Thunderbolt 5, giving connected hosts lower-latency communication for distributed MLX inference. Commenters distinguish this from earlier multi-Mac demonstrations: pipeline parallelism can pool memory for models too large for one system, but does not necessarily speed generation; tensor parallelism could use the new transport to divide each layer and improve throughput if communication stays efficient. The capability makes large unified-memory clusters more plausible, while leaving price-normalized performance, topology, cabling, remote administration, and operational reliability to real benchmarks.

### Comment pulse

- Macs drew praise for pooling unusually large unified memory, but critics said NVIDIA systems still win on throughput; posted comparisons lacked common benchmarks.
- Rack users worried about inaccessible power buttons, loose cables, and upgrades; replies cited mounts, cable stabilizers, VNC, and automated reinstall tools.
- Some feared commercial demand consuming high-memory Macs; others argued limited scaling would preserve their role as local experimentation machines.

### LLM perspective

- View: RDMA changes the feasible parallelism model; it does not establish end-to-end scaling, reliability, or economics.
- Impact: MLX users can pool memory and potentially compute over commodity cables, expanding local inference for oversized models.
- Watch next: Tensor-parallel benchmarks, prefill scaling, topology limits, cable failures, lifecycle tooling, power draw, and price-normalized throughput.
