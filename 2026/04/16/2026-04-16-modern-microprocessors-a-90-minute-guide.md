# Modern Microprocessors – A 90-Minute Guide

- Score: 176 | [HN](https://news.ycombinator.com/item?id=47737499) | Link: https://www.lighterra.com/papers/modernmicroprocessors/

### TL;DR
A long-running, continually updated guide explains how modern CPUs get speed not from MHz but from microarchitecture: pipelining, superscalar issue, VLIW, dependencies and latency, branch prediction and predication, out-of-order execution, and the “brainiac vs speed-demon” tradeoff. It shows why power and ILP walls ended the MHz race, how x86 hides a RISC-like core behind µop translation, and why SMT/multicore became central. HN readers praise the clarity, wish for a microcontroller-focused sibling, and discuss power, FLOPs, and web minimalism.

---

### Comment pulse
- “Do this for microcontrollers” → shorter pipelines for interrupts, heterogeneous cores, TCM SRAM, DMA-heavy peripherals, and explicit bus/topology awareness shape performance differently than big CPUs.  
- “More topics please” → modern tricks like pattern-based predictors, approximate LRU in caches, prefetchers, and return-address stacks add a lot beyond the article’s already rich overview.  
- “Love this old-school site” → static, ad-free HTML feels refreshing versus today’s tracking-heavy, bloated web — counterpoint: a few big modern sites still deliver huge value.

---

### LLM perspective
- View: This guide is still one of the best “mental models” for how CPUs actually run your code.  
- Impact: Helps programmers reason about performance, predict bottlenecks, and understand why compilers and hardware behave “weirdly.”  
- Watch next: Similar deep, practical explainers for MCUs, GPUs, AI accelerators, and memory systems, with up-to-date real-world measurements.
