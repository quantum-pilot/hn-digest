# %CPU utilization is a lie

- Score: 436 | [HN](https://news.ycombinator.com/item?id=45110688) | Link: https://www.brendanlong.com/cpu-utilization-is-a-lie.html

- TL;DR
  - The article shows reported %CPU understates real saturation: on a 12-core/24‑thread Ryzen, “50%” often equals 60–100% of max work (matrix/Nginx nearly saturated). Nonlinearity comes from SMT resource sharing and Turbo down-clocking; scheduling also skews results. Practical takeaway: model capacity with throughput/latency benchmarks and SLOs, not raw %CPU. HN adds that utilization is valid but misused for capacity; memory bandwidth, caches, locks, and burstiness matter; queueing theory suggests conservative headroom (≈40–60%); IPC/stall counters help but are hard to action.

- Comment pulse
  - Utilization isn’t a lie → It measures busy time; nonlinear capacity comes from SMT/turbo, memory/cache/locks, and burstiness—counterpoint: %CPU suggests linearity and misleads capacity planning.
  - Apply queueing theory with headroom → Latency spikes near saturation; many cap production at ~40–60% CPU for user-facing services.
  - Look beyond %CPU → Inspect IPC, stalls, short-window profiles; hyperthreading rarely doubles throughput (typical 15–30%, occasionally higher on memory-bound workloads).

- LLM perspective
  - View: Anchor capacity to throughput/latency SLOs; treat %CPU as nonlinear, hardware-influenced telemetry, not a scaling knob.
  - Impact: SREs and autoscalers shift alerts to latency/backlog, use core pinning, disable SMT selectively, or set per-workload thresholds.
  - Watch next: Vendor SKU curves mapping threads→throughput; dashboards with IPC/stalls and 100ms windows; experiments linking power/thermals to capacity headroom.
