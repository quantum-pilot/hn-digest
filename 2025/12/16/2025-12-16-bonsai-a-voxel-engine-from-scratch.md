# Bonsai: A Voxel Engine, from scratch

- Score: 211 | [HN](https://news.ycombinator.com/item?id=46285319) | Link: https://github.com/scallyw4g/bonsai

### TL;DR

Bonsai is a pre-alpha procedural voxel terrain engine and editor whose author wrote nearly every dependency from scratch. It claims worlds roughly one billion blocks per dimension, whole-world view distance, GPU-generated terrain, deferred rendering, editing tools, entities, physics, hot reload, and a built-in profiler. Version 2 is a major rewrite, so asset loading is currently broken and much remains on the roadmap. Discussion focused less on feature claims than on the project’s simplicity choices and hybrid rasterization versus ray tracing.

### Comment pulse

- The author credits arenas, straightforward containers, freelists, and a custom metaprogramming language for keeping long-term systems manageable.
- Ray tracing advocates argued for higher voxel counts; the author said rasterized primary visibility plus traced shadows and lighting performs better at distance.
- Artists expressed interest in importing assets, but the author confirmed that loader support awaits repair after the rewrite.

### LLM perspective

- View: The project is most instructive as a systems-design laboratory, while its extreme scale claims need reproducible benchmarks.
- Impact: Minimal dependencies expose engine tradeoffs directly and can teach more than integrating opaque production middleware.
- Watch next: Version 2 releases, asset restoration, frame-time and memory measurements, terrain-edit persistence, and representative hardware tests.
