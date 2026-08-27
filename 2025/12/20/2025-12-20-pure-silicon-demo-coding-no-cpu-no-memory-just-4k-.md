# Pure Silicon Demo Coding: No CPU, No Memory, Just 4k Gates

- Score: 262 | [HN](https://news.ycombinator.com/item?id=46337438) | Link: https://www.a1k0n.net/2025/12/19/tiny-tapeout-demo.html

### TL;DR

For Tiny Tapeout 8, the author built two hardware demos—a retro intro and Nyan Cat—within roughly 4,000 ASIC gates, producing VGA pixels and one-bit audio without a CPU, RAM, ROM, or framebuffer. A custom Verilog state machine generates every pixel per clock; flip-flops hold scarce state, while synthesis turns lookup patterns into distributed logic. Techniques include iterative sine generation, ordered dithering, procedural starfields, compact division, simple synthesized instruments, and sigma-delta output. After Efabless closed mid-production, recovered chips ultimately ran the designs successfully.

### Comment pulse

- Readers admired the project’s hardware-software equivalence and recommended learning through simulation, then FPGA, before attempting fabrication.
- Discussion probed the stability of the HAKMEM circle generator; the author said it is exact under this design’s conditions.

### LLM perspective

- View: Removing stored programs turns audiovisual compression into circuit structure, rewarding regularity and low algorithmic complexity.
- Impact: Affordable tapeouts let software-oriented builders experience physical constraints where state, routing, and mistakes carry concrete cost.
- Watch next: Future demos using standard video modes, synchronized audio, smaller state, and the author’s promised new tricks.
