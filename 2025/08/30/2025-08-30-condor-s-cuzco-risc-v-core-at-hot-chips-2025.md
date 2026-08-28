# Condor's Cuzco RISC-V Core at Hot Chips 2025

- Score: 157 | [HN](https://news.ycombinator.com/item?id=45074895) | Link: https://chipsandcheese.com/p/condors-cuzco-risc-v-core-at-hot

### TL;DR

Condor's configurable Cuzco RISC-V core combines an eight-wide, 256-entry out-of-order frontend with mostly time-based backend scheduling. At rename, a Time Resource Matrix predicts when dependencies and execution resources will be available; schedulers then wait rather than continually checking readiness. Variable-latency loads are assumed to hit L1 and trigger poison-based replay on misses. The design targets roughly 2–2.5 GHz on TSMC 5nm, supports up to eight cores per cluster, configurable caches and slices, and aims to trade some replay work for lower scheduling complexity and power.

### Comment pulse

- Readers welcomed the architectural risk but questioned whether cache misses cause cascading instruction amplification in general-purpose workloads.
- Supporters argue replay may consume otherwise idle execution capacity, potentially exchanging modest performance for substantial energy savings.

### LLM perspective

- View: Cuzco innovates below the ISA, preserving software compatibility while relocating dynamic scheduling complexity.
- Impact: If replay stays bounded, licensees could gain competitive performance-per-watt from a simpler backend.
- Watch next: Silicon benchmarks across cache-stressing workloads must validate performance, power, area, and worst-case replay behavior.
