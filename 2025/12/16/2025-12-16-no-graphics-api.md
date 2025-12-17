# No Graphics API

- Score: 344 | [HN](https://news.ycombinator.com/item?id=46293062) | Link: https://www.sebastianaaltonen.com/blog/no-graphics-api

### TL;DR
Aaltonen argues that “modern” graphics APIs (DX12, Vulkan, Metal) are relics of 2010-era hardware: they bake in complex state objects, descriptor abstractions, and buffer types that solved old architectural quirks but now cause PSO cache bloat, stutter, and engine-side complexity. Modern GPUs have coherent caches, bindless resources, and 64‑bit pointers, so he proposes almost no graphics API: CUDA‑style `gpuMalloc`/pointers, a raw descriptor heap as an array, and a single root pointer struct per draw/dispatch. HN readers mostly praise this vision but question hardware baselines and fixed‑function tradeoffs.

---

### Comment pulse
- Much of Vulkan/DX12 looks obsolete → GPUs already support pointers/bindless; a minimal CUDA‑like API could outperform today’s heavy driver layers and emulated legacy APIs.  
- Motivation resonates → like NVMe replacing SATA for SSDs; new GPU APIs should drop legacy abstractions and embrace generic compute + pointers.  
- Caution on hardware and pipelines → reBAR/UMA and recent GPUs are prerequisites; fixed‑function raster/ray units still deliver big speedups—counterpoint: many engines already “software render” via compute.

---

### LLM perspective
- View: Treat the GPU as a pointer-rich parallel computer; keep “graphics” as a thin, mostly-rasterization-specific veneer.  
- Impact: Engine and driver teams gain simpler architectures, fewer PSO/stutter issues; shader languages must evolve toward C/C++-like pointer semantics.  
- Watch next: Wider Vulkan descriptor-buffer adoption, real pointer support in HLSL/GLSL, and any console/PC API experiments resembling this malloc+root-struct model.
