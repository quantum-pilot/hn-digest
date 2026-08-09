# Building an FPGA 3dfx Voodoo with Modern RTL Tools

- Score: 147 | [HN](https://news.ycombinator.com/item?id=47477284) | Link: https://noquiche.fyi/voodoo

### TL;DR

A solo developer reimplemented the 3dfx Voodoo 1 on an FPGA using SpinalHDL and conetrace. SpinalHDL encoded four register-write behaviors—queued, drain-before-apply, direct, and float-converted—alongside 430 configuration fields, keeping timing semantics executable rather than scattered. Netlist-aware tracing then disproved a suspected framebuffer hazard: premature precision loss, texture-coordinate and LOD rounding, and incorrect blend inputs compounded into missing translucent pixels. Commenters admired the hardware recreation and reminisced about early 3D acceleration, while some objected to the article’s apparent LLM-assisted prose.

### Comment pulse

- Hardware nostalgia ran deep → readers recalled Glide-era visuals and difficult late-1990s Linux driver setup.
- The debugging method impressed → stage-by-stage comparison isolated several nearly-correct behaviors whose combination created visible corruption.
- AI-shaped writing drew criticism → some rejected its cadence — counterpoint: others argued presentation assistance does not erase substantial engineering work.

### LLM perspective

- **View:** Executable register metadata is the project’s strongest generalizable lesson.
- **Impact:** Better abstractions let individual engineers reason about timing-heavy RTL without flattening hardware semantics.
- **Watch next:** Compare more games, edge-case blending modes, synthesis targets, timing closure, and physical-board compatibility.
