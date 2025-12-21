# Pure Silicon Demo Coding: No CPU, No Memory, Just 4k Gates

- Score: 262 | [HN](https://news.ycombinator.com/item?id=46337438) | Link: https://www.a1k0n.net/2025/12/19/tiny-tapeout-demo.html

### TL;DR
The author built full VGA+audio demoscene productions as bare ASICs for Tiny Tapeout 8: about 4k logic gates, no CPU, RAM, framebuffer, or ROM macros—only flip‑flops and standard cells. Effects like sine scrollers, 3D-ish checkerboards, starfields, and chiptune music are all hardwired state machines emitting one pixel and one audio bit per clock. They exploit synthesis to turn lookup tables (fonts, notes) into logic, minimize stored state, and reuse math (e.g., HAKMEM vector-rotation sine) across visuals and sound. Nyan Cat was then squeezed into the same constraints. After Efabless’ collapse nearly killed the run, chips resurfaced and the designs worked in real silicon.  
*Content fully available; summary based on article and comments.*

---

### Comment pulse
- HAKMEM-based sin/cos generator → exact circle in fixed-point under specific conditions, closely related to Verlet-style symplectic integration — counterpoint: long‑term numerical stability is subtle.  
- Best entry path → start with Verilator or similar simulation, then FPGA; many real-world SoCs today feel like “copy/paste IP blocks plus small accelerators.”  
- Community aspect → internet enables tiny global subcultures (ASIC demoscene) to coordinate, run compos, and share tooling that would be impossible locally.

---

### LLM perspective
- View: This is “hardware demoscene,” forcing thinking in gates, state bits, and synthesis patterns instead of code and bytes.  
- Impact: Great teaching material for digital design, fixed-point math, synthesis heuristics, and creative constraint-driven engineering.  
- Watch next: More open-source Tiny Tapeout runs, reusable HDL music/graphics cores, and tutorials that turn these tricks into step-by-step labs.
