# AMD GPU Debugger

- Score: 200 | [HN](https://news.ycombinator.com/item?id=46193931) | Link: https://thegeeko.me/blog/amd-gpu-debugging/

### TL;DR
The author builds a low-level, ROCm-independent AMD GPU debugger by talking directly to `/dev/dri`, using libdrm to allocate GPU-visible buffers, then wiring a custom trap handler via privileged TBA/TMA registers exposed through amdgpu’s debugfs (using UMR’s register database). The trap shader saves per-wave register state to scratch memory, spins until the CPU inspects/modifies it, then restores state and resumes. SPIR-V is compiled through RADV’s ACO in `null_winsys` mode. Planned features include stepping, breakpoints, watchpoints, and eventually full Vulkan integration.  
*Content unavailable; summarizing from provided excerpt and comments.*

---

### Comment pulse
- Metal/Xcode offers best-in-class GPU debugging and logging, especially for learning and small projects → integrated, polished tools—counterpoint: crashes, profiling limits, and Apple-only lock-in.
- NVIDIA users point to cuda-gdb, Nsight, nsys/nvtx, and RenderDoc → relatively mature debugging and profiling across graphics and compute workflows.
- AMD already ships tools (rocgdb via GDB, UMR, Radeon GPU Detective, broader Radeon Developer Tool Suite) → this project instead explores a fully custom, open, low-level path.

---

### LLM perspective
- View: Using trap shaders plus debugfs to implement a debugger is a reusable pattern for other GPU families and vendors.
- Impact: Helps Linux/AMD developers move closer to CPU-like debugging workflows, especially for complex compute and graphics shaders.
- Watch next: Better NIR/ACO debug-info plumbing, Vulkan driver integration, and generalized watchpoint/breakpoint UIs on top of this low-level core.
