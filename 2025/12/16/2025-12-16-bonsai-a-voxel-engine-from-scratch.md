# Bonsai: A Voxel Engine, from scratch

- Score: 211 | [HN](https://news.ycombinator.com/item?id=46285319) | Link: https://github.com/scallyw4g/bonsai

### TL;DR
Bonsai is a from-scratch voxel engine and editor that aims for extreme scale (up to ~1 billion³ blocks) while keeping the codebase brutally simple. Almost everything is hand-written C++ with minimal dependencies; terrain is fully procedural and generated on the GPU via GLSL, with an in-engine SDF-based world editor and custom profiler. The current 2.0.0 prealpha is mostly a terrain generator/editor under heavy rewrite, and HN discussion centers on simplicity tradeoffs and rasterization vs raytraced voxels.

---

### Comment pulse
- Simplicity-first internals → bump/arena allocators, a small buddy heap, freelists; containers avoid complex structures like `std::map` to prevent hidden performance cliffs.
- Homegrown metaprogramming layer → replaces C++ templates, enabling easier debug UIs and robust versioned serialization—counterpoint: designing a language looks anti-simple, but pays off long-term.
- Rendering strategy debate → author favors hybrid: rasterized primary rays plus raytraced GI/shadows for vast scenes; others argue pure voxel raytracing is faster and visually acceptable.

---

### LLM perspective
- View: This is a strong educational codebase for understanding modern engines without the opacity of big frameworks.
- Impact: Indie engine devs, graphics learners, and tool authors gain patterns for allocators, metaprogramming, and GPU terrain pipelines.
- Watch next: Author’s proposed blog series, performance comparisons with pure raytracers, and completion of asset loading and editor workflows.
