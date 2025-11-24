# Unusual circuits in the Intel 386's standard cell logic

- Score: 208 | [HN](https://news.ycombinator.com/item?id=46020543) | Link: https://www.righto.com/2025/11/unusual-386-standard-cell-circuits.html

- TL;DR  
Ken Shirriff reverse‑engineers a standard‑cell region of Intel’s 1985 386, showing how its complex register‑selection logic is built from huge multiplexers implemented with CMOS transmission‑gate switches and inverters. He finds a lone “out‑of‑grid” PMOS transistor, likely a late ECO bug‑fix dropped into the routing channel, and a reused inverter cell whose transistors are secretly driven separately to add extra mux cases. HN readers dig into the IBM‑mainframe CAD toolchain, transmission‑gate practice, and evolution‑designed circuits that exploit analog chip quirks.

- Comment pulse  
  - Evolved hardware can look even stranger → Thompson’s 1990s FPGA experiments produced unstructured circuits exploiting parasitics and analogue behavior, working only on one specific chip.  
  - Transmission gates as muxes → commenters note this standard‑cell style reduces static hazards versus AND/OR muxes—counterpoint: hazards are often removed by adding redundant consensus terms.  
  - Toolchain and schedule context → Intel used Timberwolf and custom tools on IBM 3081 mainframes; despite early-stepping bugs, 386 development beat its 50 man‑year plan.

- LLM perspective  
  - View: These artifacts show how standard‑cell flows still require creative “escape hatches” for ECOs and quirky late‑stage fixes.  
  - Impact: Understanding historical mux and latch tricks can inspire leaner datapath control in FPGAs and open‑source ASIC libraries today.  
  - Watch next: Systematically catalog other 386 regions to quantify how much area timing‑driven automatic layout sacrificed versus hand‑tuned blocks.
