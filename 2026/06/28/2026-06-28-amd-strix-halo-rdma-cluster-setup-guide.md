# AMD Strix Halo RDMA Cluster Setup Guide

- Score: 222 | [HN](https://news.ycombinator.com/item?id=48703258) | Link: https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/blob/main/rdma_cluster/setup_guide.md

### TL;DR

The guide turns two 128 GB Strix Halo systems into a 256 GB distributed-inference cluster using Intel E810 RoCE v2 adapters, a direct 100GbE cable, Fedora 43, Ray, vLLM tensor parallelism, and a patched RCCL library adding missing gfx1151 RDMA support. Its x4 PCIe link achieved about 50 Gbps and 5 μs latency versus roughly 68 μs over TCP; Thunderbolt is offered as an easier fallback. HN praised the obtainable memory capacity but flagged $800 networking, awkward mini-PC expansion, rapidly rising hardware prices, and slower inference than high-memory Apple systems.

### Comment pulse

- Unified memory expands local model size → two nodes can shard models beyond 24 GB consumer GPUs, approaching provider-style capacity on prosumer hardware.
- Memory bandwidth limits usefulness → generation and prefill can trail M4/M5 Macs — counterpoint: kernel and software optimization may recover performance.
- Economics deteriorated quickly → 128 GB Strix systems rose from roughly €2,500 to far more, while frontier APIs remain cheap and hardware evolves.

### LLM perspective

- **View:** RDMA solves inter-node latency, not local memory-bandwidth scarcity; both determine tensor-parallel token throughput.
- **Impact:** Homelabbers gain larger private-model capacity; adopters accept kernel tuning, patched collectives, unusual PCIe mechanics, and operational fragility.
- **Watch next:** Benchmark prefill, generation, scaling efficiency, energy, Thunderbolt versus RoCE, upstream RCCL support, and stability without forced eager mode.
