# Bonsai: A Voxel Engine, from scratch

- Score: 211 | [HN](https://news.ycombinator.com/item?id=46285319) | Link: https://github.com/scallyw4g/bonsai

### TL;DR

Bonsai is a from-scratch voxel-engine project built as a learning exercise around simple, inspectable systems. Its README claims a procedurally generated world roughly one billion blocks per side, full-world view distance, shader-configurable terrain, SDF editing, deferred rendering, and a broad set of custom engine subsystems. Version 2.0.0-prealpha-rc0 is a major rewrite and currently functions chiefly as a terrain generator and editor; many gameplay and tooling items remain unfinished. Binaries target Windows and Linux, while source builds require modern Clang.

### Comment pulse

- The author credits arena and buddy allocators, straightforward containers, and custom metaprogramming for keeping serialization and debug tooling manageable.
- A rasterization-versus-ray-tracing debate converged on hybrid rendering: rasterized primary visibility with traced shadows or illumination where useful.
- Asset loading is temporarily broken after the rewrite, with restoration identified as the next priority.

### LLM perspective

- View: Bonsai is most compelling as an unusually ambitious learning engine, not yet a finished game platform.
- Impact: Its simple custom systems offer concrete material for studying large-world rendering and engine architecture.
- Watch next: Restored assets, reproducible performance measurements, gameplay milestones, documentation, and stability beyond pre-alpha.
