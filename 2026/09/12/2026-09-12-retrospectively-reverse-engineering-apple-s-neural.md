# Retrospectively Reverse-Engineering Apple's Neural Engine

- Score: 229 | [HN](https://news.ycombinator.com/item?id=49670032) | Link: https://eiln.github.io/posts/ane.html

### TL;DR

After pausing work for three years, the author resumes reverse-engineering the M1 Apple Neural Engine to document its architecture rather than promote it as a general accelerator. Their experiments describe 16 compute cores, fixed-point accumulation, piecewise-linear activation lookup tables, fixed-size task descriptors, hardware-managed scheduling, and a specialized memory/dataflow design optimized for predictable CNN reuse. The author argues transformer workloads weakened that specialization’s value and interprets Apple’s later integration of neural units into GPU cores as confirmation. Commenters praise the technical depth while debating Apple’s broader accelerator strategy.

### Comment pulse

- Dataflow matters more than MAC counts → predictable CNN reuse shaped the ANE’s scheduler and memory architecture around specialized workloads.
- The reverse engineering fills documentation gaps → commenters value empirical register probes, driver work, and architectural reconstruction despite limited practical use.
- Specialized NPUs face shifting workloads → transformer-era demands make general GPU-style dataflow more attractive than rigid CNN pipelines.

### LLM perspective

- View: The work’s value is historical and architectural: it exposes which workload assumptions Apple permanently encoded into silicon.
- Impact: Compiler and driver developers gain concrete clues about scheduling, precision, memory movement, and unsupported workload shapes.
- Watch next: Replicate probes across chip generations and compare utilization, power, and latency for CNNs versus transformer inference.
