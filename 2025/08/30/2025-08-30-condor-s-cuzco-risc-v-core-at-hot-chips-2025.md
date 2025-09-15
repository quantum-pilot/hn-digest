# Condor's Cuzco RISC-V Core at Hot Chips 2025

- Score: 157 | [HN](https://news.ycombinator.com/item?id=45074895) | Link: https://chipsandcheese.com/p/condors-cuzco-risc-v-core-at-hot

- TL;DR
  - Condor (Andes) unveiled Cuzco, an 8‑wide OoO RISC‑V core aiming high end via “time‑based” scheduling: the rename stage preplans issue using a Time Resource Matrix, leaving simpler back‑end queues and using replays for variable latencies. Specs: 256‑entry ROB, TAGE‑SC‑L predictor, 64KB I‑cache, configurable L2/L3, vector via 64‑bit slices, 2.0–2.5 GHz on TSMC N5, up to 8‑core clusters over CHI. HN debates perf‑vs‑efficiency tradeoffs, memory‑bound risks, target markets, and Andes’s odds of landing marquee licensees.

- Comment pulse
  - Time-based scheduling trades few% perf for energy → renamer+TRM plan issue; replays handle misses; concern: cascades on memory-bound DC — counterpoint: replays fill idle width.
  - Andes/Condor must win licensees → hyperscaler backing reduces risk; Ampere struggled without captive customer; Andes already strong in low-power RISC‑V sockets.
  - Best fit may be edge/RT-ish segments → static-ish scheduling enticing; compiler-marked blocks debated; author: they predict all ops, replay variable-latency (memory, divides).

- LLM perspective
  - View: Cuzco re-centers OoO cost to rename; replay makes latency tolerance a software-transparent knob traded for power/area.
  - Impact: If silicon matches claims, RISC-V gets a licensable high-end core; vendors can scale slices and caches per SKU and workload.
  - Watch next: Measure PPA: SPEC, replays/kinst, MPKI; check memory-bound throughput under contention; watch first big design win and node access.
