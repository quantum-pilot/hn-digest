# No Graphics API

- Score: 344 | [HN](https://news.ycombinator.com/item?id=46293062) | Link: https://www.sebastianaaltonen.com/blog/no-graphics-api

### TL;DR

Sebastian Aaltonen argues that Vulkan, DirectX 12, and Metal expose abstractions shaped by older, less coherent GPUs, burdening modern engines with bindings, barriers, pipeline permutations, and translation layers. He sketches a narrower cross-platform interface built around GPU virtual-memory pointers, C-style data structures, global texture descriptors, simpler synchronization, transient command buffers, and powerful indirect execution, while retaining fixed-function rasterization where efficient. The prototype surface is about 150 lines, but it is a design proposal rather than a benchmarked implementation, targets relatively recent hardware, and leaves compatibility and translation work unresolved.

### Comment pulse

- Readers welcomed the clear hardware history and linked the proposal to SDL3 GPU, while noting its abstraction and compatibility choices differ.
- Calls for software rendering met resistance — counterpoint: fixed-function raster and ray hardware deliver performance the proposal deliberately preserves.
- Commenters questioned ReBAR and older-device support, underscoring the tradeoff between a clean model and broad deployability.

### LLM perspective

- View: A smaller API could align engines with modern hardware, but simplicity partly comes from narrowing supported capabilities and generations.
- Impact: Cleaner primitives might reduce shader permutations, synchronization mistakes, driver overhead, and engine-specific remapping.
- Watch next: A working implementation, vendor translation layers, mobile TBDR behavior, measured performance, and shader-language ecosystem adoption.
