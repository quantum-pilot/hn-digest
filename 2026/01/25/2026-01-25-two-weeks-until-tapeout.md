# Two Weeks Until Tapeout

- Score: 186 | [HN](https://news.ycombinator.com/item?id=46749671) | Link: https://essenceia.github.io/projects/two_weeks_until_tapeout/

### TL;DR
Solo engineer Julia Desmazes tapes out a custom AI-oriented chip in just 10 frantic days for a free Tiny Tapeout experimental shuttle on GlobalFoundries 180nm. The design combines a hand-rolled 2×2 int8 systolic MAC array (with in-place weights, custom Booth radix‑4 multiplier, clamping, buffers for I/O bottlenecks) and a JTAG TAP with custom USER_REG for deep in-silicon observability across clock domains. She leans heavily on OpenROAD/LibreLane flows, FPGA emulation, Cocotb tests, and plans future floating‑point and richer DFT work.

---

### Comment pulse
- Hardware posts widen horizons → readers realize most of tech isn’t web CRUD; much of this stack (ASIC flows, DFT, systolic arrays) feels like arcane wizardry.
- Tapeout veterans: shuttle deadlines plus timing/DRC/LVS closure mean month-long 80–100 hour weeks; miss the slot and you slip by months—counterpoint: software also has brutal crunch tied to external gates.
- Many praise the writing: dense hardware details made funny and readable, inspiring some to dream about doing their own silicon someday.

---

### LLM perspective
- View: This showcases how mature open-source EDA plus disciplined personal flows let one person execute genuinely sophisticated silicon projects.
- Impact: Lowers psychological and practical barriers for firmware/FPGA folks to step into ASICs, especially for AI accelerators and debug IP.
- Watch next: Larger arrays with SRAM, open-source DFT/ATPG integration, and more community-friendly documentation around multi-clock-domain JTAG + accelerator designs.
