# AMD and Sony's PS6 chipset aims to rethink the current graphics pipeline

- Score: 299 | [HN](https://news.ycombinator.com/item?id=45546593) | Link: https://arstechnica.com/gaming/2025/10/amd-and-sony-tease-new-chip-architecture-ahead-of-playstation-6/

- TL;DR
  - Reports suggest Sony and AMD will redesign the PS6 graphics pipeline, tightening integration of AI upscaling/frame generation and newer primitives (mesh/neural shaders), and possibly shifting more silicon to ray/path tracing while de-emphasizing legacy raster steps. HN splits: some see hardware limits forcing “fake frames” and cloud offload; others argue consoles’ fixed targets are ideal to go RT-first and simplify rendering. Skeptics note cross‑platform/back‑compat will restrain radical changes and that gameplay/simulation progress, not pixels alone, drives demand—though PS5’s SSD shows platform bets can reset baselines.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Hardware gains plateau → AI upscaling/frame-gen fill gaps but consume die area; cloud rendering looms — counterpoint: ray tracing scales with resolution, simplifying pipelines.
  - Consoles suit RT-first designs → fixed targets could drop legacy raster paths — counterpoint: cross-platform and backward compatibility keep hybrid raster/RT, with primaries still rasterized.
  - Gameplay and simulation drive demand → Switch’s success shows lower specs can win — counterpoint: many still pay for 120/4k; better GI benefits stylized indies.

- LLM perspective
  - View: PS6 likely reallocates die area to AI/RT blocks, integrating frame generation; wholesale raster removal unlikely this gen.
  - Impact: Engines and tooling must deliver low-latency FG/upscaling paths and RT-first workflows; QA shifts to motion artifacts and latency metrics.
  - Watch next: AMD RDNA roadmap, Sony SDKs, neural shader APIs, and end-to-end latency benchmarks for frame-gen under variable refresh and streaming.
