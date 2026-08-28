# E-paper display reaches the realm of LCD screens

- Score: 595 | [HN](https://news.ycombinator.com/item?id=45185756) | Link: https://spectrum.ieee.org/e-paper-display-modos

### TL;DR

Modos’s crowdfunded development kit drives standard 13-inch or 6-inch e-paper panels at up to 75 hertz using Caster, an open-source FPGA controller, and a multi-panel Glider adapter. Pixel-level control and a C API allow different screen regions to use modes optimized for low-latency text, grayscale maps, or higher-fidelity video. The open hardware can also repurpose compatible salvaged displays. Commenters emphasized that the controller, documentation, and flexibility—not a newly invented panel—are the core achievement, while questioning power use and panel longevity under frequent updates.

### Comment pulse

- Modos said its driver board draws roughly 1 to 1.5 watts under continuous use.
- Users valued fast bursts for scrolling and navigation more than sustained video, especially on non-emissive reading displays.

### LLM perspective

- View: Variable, region-specific refresh is more consequential than matching LCD headline rates across an entire screen.
- Impact: Open control could improve e-paper interaction and experimentation without sacrificing its reflective-display advantages during static use.
- Watch next: Shipped hardware, endurance measurements, ghosting, power by mode, panel compatibility, and compositor integration.
