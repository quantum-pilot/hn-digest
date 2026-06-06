# CUDA-oxide: Nvidia's official Rust to CUDA compiler

- Score: 347 | [HN](https://news.ycombinator.com/item?id=48096692) | Link: https://nvlabs.github.io/cuda-oxide/index.html

### TL;DR
NVIDIA’s cuda-oxide is an experimental, first-party Rust-to-CUDA toolchain that compiles idiomatic Rust directly to PTX via a custom rustc backend, no nvcc or DSL required. It offers a layered safety model: high-level safe abstractions (e.g., `DisjointSlice`, typed kernel launches) down to unsafe escape hatches, plus async GPU programming via composable `DeviceOperation`s. HN readers are excited about a potential cudarc-like replacement, curious about build times and IR choices, and debating how much real safety Rust can bring to GPU kernels.

---

### Comment pulse
- Rust GPU users see cuda-oxide as a possible cudarc replacement → pure Rust kernels, better safety, no nvcc in build scripts — counterpoint: current nvcc-based flows often aren’t the main build-time cost.  
- Safety model seen as a big differentiator → Rust types enforce disjoint writes, validated kernel args, and safer buffers; still retains unsafe layers for peak performance.  
- Design questions raised → why target PTX instead of NVIDIA’s MLIR/tile IR; and how this relates to Slang, which remains focused on graphics/shaders, not general CUDA compute.

---

### LLM perspective
- View: This makes Rust a serious first-class option for CUDA kernels, but it’s alpha and will likely be unstable for a while.  
- Impact: Rust-based ML, simulation, and infra projects gain a path to safer, more integrated GPU code—at the cost of deeper NVIDIA lock-in.  
- Watch next: Real-world perf vs CUDA C++/cudarc, compile times vs nvcc, and whether the project stabilizes and tracks upstream rustc smoothly.
