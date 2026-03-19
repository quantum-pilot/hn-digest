# Write up of my homebrew CPU build

- Score: 229 | [HN](https://news.ycombinator.com/item?id=47389696) | Link: https://willwarren.com/2026/03/12/building-my-own-cpu-part-3-from-simulation-to-hardware/

### TL;DR

An 8‑bit homebrew CPU moves from clean Logisim simulations to messy but working 1 MHz hardware. The author battles real‑world demons: SMT parts on breadboards, misdesigned control ROM PCBs, bad solder joints, ugly clock edges, EEPROM output glitches, and asynchronous RAM corrupting itself. Fixes include Schmitt‑triggered clocks, an extra latch stage before the microcode ROMs, and clock‑gated RAM writes. A Python microcode generator and 6502‑style assembler drive programs, currently loaded via an Arduino, with plans for a self‑contained LED‑rich PCB and a more advanced WCPU‑2.

### Comment pulse

- Better registers with LEDs → Use two ’574s in parallel: one always drives LEDs, the other tri‑states to the bus, reducing loading and propagation delays.  

- Scaling homebrew CPUs is hard → Discontinued MSI parts (74181, register files) make >8/16‑bit builds part‑hungry and slow—counterpoint: tiny tapeout ASICs could recreate these blocks.  

- Culture of bench chaos → Readers relate to multi‑breadboard rats’ nests, Rigol scopes, and SMD‑only parts, emphasizing experiential learning over “proper engineer” one‑shot designs.  

### LLM perspective

- View: This is a near‑textbook case of why synchronous design discipline and verification matter once you leave idealized simulators.  

- Impact: Great teaching material for hobbyists or classes moving from HDL/Logisim to wires, scopes, and real‑world timing margins.  

- Watch next: An FPGA WCPU‑1 plus open‑sourced schematics, ROM tools, and maybe a tiny‑tapeout ALU slice would solidify this as a reusable learning platform.
