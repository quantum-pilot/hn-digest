# Building an FPGA 3dfx Voodoo with Modern RTL Tools

- Score: 147 | [HN](https://news.ycombinator.com/item?id=47477284) | Link: https://noquiche.fyi/voodoo

### TL;DR
An engineer reimplements the 3dfx Voodoo 1 GPU on an FPGA using SpinalHDL, showing how “simple” fixed‑function chips hide lots of timing and control complexity. They classify 430+ configuration fields into architectural register behaviors (FIFO, FIFO+stall, direct, float aliases) and encode this directly in the HDL, making the register map an executable spec. Debugging a translucent‑overlay bug with netlist‑aware tracing (conetrace) exposes stacked precision, rounding, and blending mismatches, illustrating how modern RTL abstractions and queryable tooling let one person realistically rebuild such hardware.

---

### Comment pulse
- Retro admiration → Voodoo is remembered as unbelievably good for its era; this faithful rebuild hits HN’s sweet spot of deep, nerdy craftsmanship.  
- History comparison → Some argue NV‑1 was more advanced (NURBS, forward mapping) but doomed once DirectX standardized triangles—counterpoint: Voodoo’s simplicity and ecosystem won.  
- LLM-text unease → Several readers feel the article “smells” LLM‑written; others defend tool-assisted writing as analogous to using math/engineering aids.

---

### LLM perspective
- View → Encoding register semantics and timing as first-class HDL metadata is a powerful pattern for complex legacy reimplementations.  
- Impact → Lowers the bar for solo or small‑team hardware archaeology: GPUs, sound chips, and consoles become more reproducible and testable.  
- Watch next → Wider adoption of netlist‑aware tracing, formal equivalence to reference models, and reusable “behavioral register maps” across open FPGA cores.
