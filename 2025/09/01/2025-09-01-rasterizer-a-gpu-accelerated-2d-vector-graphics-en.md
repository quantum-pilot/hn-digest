# Rasterizer: A GPU-accelerated 2D vector graphics engine in ~4k LOC

- Score: 169 | [HN](https://news.ycombinator.com/item?id=45090553) | Link: https://github.com/mindbrix/Rasterizer

### TL;DR

Rasterizer is a roughly 4,000-line C++11 and Metal engine for GPU-accelerated 2D vector graphics on macOS, developed over ten years and claimed to reach 60 times CPU performance. It supports PostScript-style paths, fills, strokes, SVGs, PDFs, clipping, and animated interfaces. Small fills copy raw geometry to GPU memory; large fills use fat scanlines, while GPU algorithms calculate coverage, triangulate strokes, and solve quadratic Béziers. The implementation uses the traditional graphics pipeline and is source-available under a custom personal-use zlib license.

### Comment pulse

- Discussion compared it with compute-based Vello and text-focused Slug; the author said Rasterizer prioritizes scale robustness and competitive performance.
- The ad hoc license raised uncertainty about redistribution, commercial use, and whether the project qualifies as open source.

### LLM perspective

- View: The compact implementation is technically intriguing, but its custom license limits confident adoption and collaboration.
- Impact: Efficient path rendering could benefit animated interfaces, document viewers, and Flash-style content on constrained hardware.
- Watch next: Independent benchmarks, pathological-path tests, an algorithm write-up, and a standard dual-license would clarify its value.
