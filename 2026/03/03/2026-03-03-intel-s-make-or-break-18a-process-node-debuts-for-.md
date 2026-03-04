# Intel's make-or-break 18A process node debuts for data center with 288-core Xeon

- Score: 225 | [HN](https://news.ycombinator.com/item?id=47236958) | Link: https://www.tomshardware.com/pc-components/cpus/intels-make-or-break-18a-process-node-debuts-for-data-center-with-288-core-xeon-6-cpu-multi-chip-monster-sports-12-channels-of-ddr5-8000-foveros-direct-3d-packaging-tech

- TL;DR  
Intel’s new Xeon 6+ “Clearwater Forest” is its first 18A (1.8‑nm‑class) server CPU: up to 288 Darkmont efficiency cores across 12 18A chiplets stacked via Foveros Direct on Intel 3 base dies, with Intel 7 I/O tiles, 12‑channel DDR5‑8000 and 96 PCIe 5.0 / 64 CXL 2.0 lanes. It targets dense, power‑efficient cloud, telecom and edge AI workloads. HN discussion centers on cloud vs on‑prem economics, software/NUMA scaling limits, and the strategic importance of Intel’s packaging and foundry story.

- Comment pulse  
  - High‑core servers make fixed workloads cheaper on‑prem than cloud over years → fewer boxes, lower bills — counterpoint: infra staff and operations are expensive.  
  - All‑E‑core design suits massively threaded, light per‑thread work; weak single‑thread and missing AVX‑512 plus NUMA/scheduling pitfalls limit gains for latency‑sensitive or vector‑heavy workloads.  
  - Commenters highlight 18A/3/7 multi‑die Foveros packaging as the real story: de‑risking yields, proving Foundry’s capabilities, and positioning Xeon as a CXL hub amid ARM competition.

- LLM perspective  
  - View: Core‑dense x86 with serious packaging reopens the on‑prem vs cloud math for “boring” enterprise workloads that rarely need elasticity.  
  - Impact: Hyperscalers, telcos, and large SaaS vendors gain new consolidation levers; cloud CPU SKUs and pricing will adjust in response.  
  - Watch next: Real‑world perf‑per‑watt vs Graviton, Epyc and accelerators; CXL memory pooling deployments; and whether IFS customers adopt 18A/Foveros stacks.
