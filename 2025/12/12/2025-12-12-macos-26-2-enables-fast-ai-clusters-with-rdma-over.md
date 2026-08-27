# macOS 26.2 enables fast AI clusters with RDMA over Thunderbolt

- Score: 512 | [HN](https://news.ycombinator.com/item?id=46248644) | Link: https://developer.apple.com/documentation/macos-release-notes/macos-26_2-release-notes#RDMA-over-Thunderbolt

### TL;DR

Apple’s macOS 26.2 release notes add RDMA over Thunderbolt 5 between Macs, explicitly mentioning distributed AI inference with MLX. Commenters distinguish this from existing MLX pipeline parallelism, which mainly lets models exceed one machine’s memory: they argue lower-latency RDMA could make tensor parallelism practical by sharding every layer across machines. That performance promise is community interpretation, not an Apple benchmark. Discussion also flags mundane cluster constraints, including cabling, rack mounting, power controls, remote administration, and macOS upgrades.

### Comment pulse

- Enthusiasm centers on aggregating Mac unified memory, while commenters dispute whether cost and throughput compare favorably with conventional GPU servers.
- Several readers say Thunderbolt connector reliability and unattended macOS operation may matter as much as raw interconnect latency.

### LLM perspective

- View: RDMA changes the plausible parallelism model, but the supplied evidence establishes capability rather than measured scaling.
- Impact: Small teams could assemble larger-memory inference clusters without adopting a conventional datacenter stack.
- Watch next: Independent tensor-parallel benchmarks, failure behavior, topology limits, and unattended fleet management will determine practical value.
