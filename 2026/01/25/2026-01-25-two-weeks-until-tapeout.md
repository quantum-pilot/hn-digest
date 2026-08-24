# Two Weeks Until Tapeout

- Score: 186 | [HN](https://news.ycombinator.com/item?id=46749671) | Link: https://essenceia.github.io/projects/two_weeks_until_tapeout/

### TL;DR

Julia Desmazes used a free experimental Tiny Tapeout shuttle to design and submit a GlobalFoundries 180 nm ASIC in ten days. The chip combines a four-unit, 8-bit 2×2 systolic matrix accelerator with a reusable JTAG test-access block that can inspect internal registers. She parallelized RTL, simulation, FPGA emulation, firmware, and physical implementation using Cocotb, OpenOCD, LibreLane, and OpenROAD. Tight pin bandwidth, unavailable SRAM, two clock domains, verification, and resisting extra features defined the sprint; the design is now in fabrication.

### Comment pulse

- Mature automation made the deadline plausible → reusable flows moved the bottleneck from tooling to architecture and verification.
- Fixed shuttle dates intensify crunch → missing submission can delay fabrication by months rather than days.

### LLM perspective

- View: The accelerator is principally a realistic test vehicle for reusable silicon-debug infrastructure.
- Impact: Open tooling and shared shuttles make hands-on ASIC development accessible to experienced individuals.
- Watch next: First-silicon functionality, JTAG observability, timing at assumed I/O rates, and expanded scan-chain support.
