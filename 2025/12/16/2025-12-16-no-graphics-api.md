# No Graphics API

- Score: 344 | [HN](https://news.ycombinator.com/item?id=46293062) | Link: https://www.sebastianaaltonen.com/blog/no-graphics-api

### TL;DR

Sebastian Aaltonen argues decade-old low-level graphics APIs preserve abstractions built for heterogeneous hardware that modern bindless GPUs no longer need. His prototype combines mapped GPU memory, 64-bit pointers, descriptor heaps, C/C++-style shaders, dynamic state, and explicit hazards to shrink API surface and avoid pipeline-state permutation caches. He contends existing DirectX, Vulkan, Metal, and WebGPU applications could run through translation layers. Commenters welcomed the direction but questioned minimum hardware, mobile tilers, fixed-function performance, documentation, and adoption feasibility.

### Comment pulse

- Supporters blamed legacy binding models and optional extensions for driver complexity, shader-cache growth, and poor developer ergonomics.
- Hardware counterpoints stressed that recent feature support limits deployment and dedicated rasterization or ray-tracing units still deliver major speedups.
- Several readers wanted a concise motivation sooner; the article’s exhaustive hardware history obscured its proposed clean break.

### LLM perspective

- View: The proposal is a credible design exploration, not yet evidence that one minimal cross-vendor API fits every architecture.
- Impact: A bindless reset could simplify engines and drivers, but shifts portability, safety, and compatibility costs into tooling and translation.
- Watch next: Prototype benchmarks, mobile results, debugger quality, translation completeness, and vendor participation would test practical viability.
