# Additive Blending on the Nintendo 64

- Score: 163 | [HN](https://news.ycombinator.com/item?id=48149259) | Link: https://phoboslab.org/log/2026/05/n64-additive-blending

### TL;DR

The PlayStation GPU clamps additive sums into range, producing bright explosions; the Nintendo 64 RDP instead wraps overflow in its usual 16-bit framebuffer. The workaround renders at one-eighth intensity into a 32-bit buffer for headroom, then uses RSP vector code to clamp and convert each frame to 16-bit in about 3.1 ms, versus 70 ms on the CPU. It nearly doubles framebuffer bandwidth, but limiting the 32-bit pass to effects or lower resolution could help. HN readers praised the explanation and connected overflow artifacts to fixed-point audio mixing.

### Comment pulse

- Audio engineers recognized the same fixed-point failure: unclamped sums create harsh artifacts, while floating-point mixing preserves headroom until final integer output.
- Some proposed compressor-like dynamic scaling, though extra math and response tuning would make it expensive on N64-era hardware.
- Readers said the explanation resolved a long-standing visual mystery, including why Turok’s explosions appeared dark and dirty rather than luminous.

### LLM perspective

- View: The technique trades bandwidth for correct saturation, using precision expansion and a cheap vectorized quantization pass.
- Impact: Homebrew developers gain a viable effects pipeline without moving geometry, scaling, or rotation work away from the RDP.
- Watch next: Benchmark effects-only buffers, reduced resolutions, compositing overhead, memory contention, and quality under heavy sprite overlap.
