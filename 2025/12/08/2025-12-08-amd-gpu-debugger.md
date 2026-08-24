# AMD GPU Debugger

- Score: 200 | [HN](https://news.ycombinator.com/item?id=46193931) | Link: https://thegeeko.me/blog/amd-gpu-debugging/

### TL;DR

An experimental AMD RDNA3 GPU debugger demonstrates CPU-style pause, inspection, modification, and single-instruction stepping on an RX 7900 XTX under Linux. It bypasses Vulkan through DRM command submission, uses privileged trap registers, and runs an ACO-compiled shader with a trap handler sharing state with the CPU. The proof of concept assumes one wave and targets gfx1100; breakpoints, watchpoints, robust multi-wave handling, debug-name propagation, and normal RADV integration remain unfinished. Discussion situates it beside rocGDB, UMR, Nsight, RenderDoc, and Metal tooling.

### Comment pulse

- Existing tools cover pieces → rocGDB, UMR, cuda-gdb, Nsight, and RenderDoc exist, but support and workflows remain fragmented.
- Metal’s capture and logging impressed users → counterpoint: vendor lock-in, hangs, and compute-debugging gaps still undermine it.

### LLM perspective

- View: Direct trap control proves feasibility, while unfinished concurrency and safety dominate readiness.
- Impact: AMD shader developers gain a blueprint for deeper inspection outside ROCm.
- Watch next: Multi-wave state isolation, breakpoints, watchpoints, symbols, and RADV integration.
