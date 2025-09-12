# Rasterizer: A GPU-accelerated 2D vector graphics engine in ~4k LOC

- Score: 169 | [HN](https://news.ycombinator.com/item?id=45090553) | Link: https://github.com/mindbrix/Rasterizer

- TL;DR
    - Rasterizer is a ~4k‑LOC, Metal-based 2D vector engine using the traditional graphics pipeline: float-mask fills, GPU‑triangulated strokes, quadratic Béziers in-shader, and a novel coverage step; author claims up to 60× CPU speed and stability at any scale. HN compares it with Vello (compute-based) and Slug (text‑centric), praises performance, but flags the ad‑hoc “personal use zlib” license as source‑available at best. Discussion probes GPU path‑winding complexity, requests public benchmarks/blog posts, and wonders about integration with PDF, browsers, and Ruffle.

- Comment pulse
    - Traditional pipeline, not compute; comparable to Vello; Slug is text-focused → aims at Flash-like animated UI; claims robustness at extreme zooms.
    - Ad‑hoc “personal use zlib” license → ambiguous rights and distribution; effectively source‑available; recommend OSI or dual license — counterpoint: authors need sustainable commercial options.
    - 2D on GPUs is hard due to path winding and irregular workloads → huge single-path SVGs stress parallelism; community asks for benchmarks and a write‑up.

- LLM perspective
    - View: Stateless GPU, per-frame writes to shared memory simplify concurrency and can avoid resident-geometry complexity for animated scenes.
    - Impact: Adoption hinges on clarified licensing and cross-platform backends; otherwise comparisons will skew toward Vello, Skia, Pathfinder, and proprietary toolchains.
    - Watch next: Publish reproducible microbenchmarks and nasty-path tests; ship an iOS port; document integration APIs; consider Vulkan/DX12 targets.
