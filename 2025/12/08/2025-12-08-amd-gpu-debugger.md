# AMD GPU Debugger

- Score: 200 | [HN](https://news.ycombinator.com/item?id=46193931) | Link: https://thegeeko.me/blog/amd-gpu-debugging/

### TL;DR

A proof-of-concept debugger for AMD RDNA3 GPUs works below standard compute stacks: it opens the DRM device, allocates memory, compiles shaders through ACO, constructs PM4 packets, and installs a trap handler through privileged debug registers. Traps save a wave’s context for CPU inspection; the debugger can halt, modify, resume, and instruction-step one wave, with source mapping from compiler debug information. It remains deliberately incomplete and risky: VMID handling is hacked across processes, while breakpoints, watchpoints, variables, Vulkan integration, and multi-wave operation remain future work.

### Comment pulse

- Readers compare it with Metal, cuda-gdb, Nsight, RenderDoc, ROCgdb, and UMR, exposing a fragmented GPU-debugging landscape.
- Integrated vendor tools earn praise, but commenters also report portability limits, crashes, and missing compute-capture support.

### LLM perspective

- View: The valuable result is proving wave-level debugging possible with public-enough primitives.
- Impact: A safer integration could shorten shader debugging without requiring heavyweight vendor stacks.
- Watch next: Multi-wave correctness, process isolation, stable register access, and real breakpoint semantics.
