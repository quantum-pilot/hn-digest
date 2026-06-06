# Additive Blending on the Nintendo 64

- Score: 163 | [HN](https://news.ycombinator.com/item?id=48149259) | Link: https://phoboslab.org/log/2026/05/n64-additive-blending

### TL;DR
Explains why PlayStation-era explosions looked better than Nintendo 64’s: PSX GPU supported clamped additive blending in 16‑bit, so bright effects simply added light to the framebuffer. N64’s more programmable RDP also supports additive formulas, but in the common 16‑bit mode it wraps on overflow instead of clamping, producing ugly artifacts, so games avoided it. The author devises a homebrew workaround: render at darkened 32‑bit color, do additive blending safely, then convert and clamp back to 16‑bit using fast RSP vector code—trading memory bandwidth for better effects.

---

### Comment pulse
- Prior work → Earlier N64 blending behavior was dissected on NESDev; this article stands out by pairing clear explanation with a concrete, performant homebrew implementation.
- Audio analogy → Readers liken color overflow to fixed‑point audio clipping: you either clamp or keep headroom — counterpoint: floating‑point audio mostly avoids this today.
- Reception → People remember “dull” N64 explosions without knowing why; they enjoy finally getting the technical cause, plus jokes about Turok’s smoggy blasts and the RMS gag.

---

### LLM perspective
- View → Neat case study in using extra precision plus a postpass to emulate missing GPU features on constrained, fixed‑function hardware.
- Impact → Gives N64 homebrew/demos a drop‑in recipe for prettier effects without abandoning the standard 16‑bit output path.
- Watch next → Measure performance on content‑heavy scenes; experiment with half‑res 32‑bit effects layers and smarter RSP compositing to reduce bandwidth.
