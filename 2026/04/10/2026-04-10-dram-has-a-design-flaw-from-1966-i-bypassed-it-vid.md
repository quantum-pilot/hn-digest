# DRAM has a design flaw from 1966. I bypassed it [video]

- Score: 381 | [HN](https://news.ycombinator.com/item?id=47680005) | Link: https://www.youtube.com/watch?v=KKbgulTp3FE

### TL;DR

LaurieWired’s Tailslayer attacks DRAM refresh stalls, which periodically block reads for roughly 400 ns. It reverse-engineers undocumented address scrambling to place duplicate data on independent memory channels with uncorrelated refresh schedules, then races concurrent reads and returns the first result. Across Intel, AMD, Graviton, DDR4, DDR5, x86, and Arm, the project reports up to 15× lower p99.99 latency. Commenters praised the hardware investigation but called “design flaw” a tradeoff: hedging doubles storage, bandwidth, cache pressure, and threading complexity to eliminate rare ~250 ns spikes, making practical workloads—including HFT—unclear.

### Comment pulse

- A 9950X3D test showed periodic jumps from 70 ns to 330 ns, validating the refresh-stall signal across commodity hardware.
- HFT generally prioritizes cache and FPGA control — counterpoint: duplicating cold DRAM reads may worsen overall throughput despite tighter tails.
- A dedicated instruction that races two memory reads could retain the idea while removing Tailslayer’s expensive multi-threaded software machinery.

### LLM perspective

- **View:** Hedged DRAM reads exchange average resource efficiency for a narrower extreme-latency distribution; neither objective universally dominates.
- **Impact:** Specialized latency-sensitive, read-mostly systems may benefit, while general applications likely pay excessive memory and bandwidth costs.
- **Watch next:** End-to-end workload benchmarks, throughput loss, cache pollution, power, NUMA comparisons, mutation support, and possible hardware primitives.
