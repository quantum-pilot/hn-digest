# Unusual circuits in the Intel 386's standard cell logic

- Score: 208 | [HN](https://news.ycombinator.com/item?id=46020543) | Link: https://www.righto.com/2025/11/unusual-386-standard-cell-circuits.html

### TL;DR

Intel adopted automated standard-cell placement and routing to manage the 386’s 285,000 transistors, helping finish the processor ahead of schedule. Die analysis reveals register-selection logic dominated by large one-hot multiplexers built from CMOS transmission gates, a lone PMOS transistor placed in a routing channel that may be a manual bug fix, and “inverter” cells actually split into independently controlled transistors to extend multiplexers. Commenters connected the work to VLSI automation, Intel’s mainframe-based design tools, physical-substrate circuit evolution, and questions about early 386 errata.

### Comment pulse

- Automation inflection → reusable cells and place-and-route helped bridge handcrafted LSI toward HDL-driven VLSI design.
- Physical workaround → the stray transistor plausibly avoided hours of layout regeneration, though its bug-fix origin remains a hypothesis.
- Historical tooling → Intel used Timberwolf placement, proprietary routing, and an IBM 3081 running Unix for assembly.

### LLM perspective

- View: The anomalies show automated design already depended on human interpretation, exceptions, and physical-level ingenuity.
- Impact: Reverse engineering exposes how workflow constraints shape lasting microarchitectural artifacts alongside logical requirements.
- Watch next: Complete register-control mapping, verify the transistor hypothesis, correlate masks and steppings, and inspect design records.
