# Nvidia announces native GPU programming in Rust

- Score: 739 | [HN](https://news.ycombinator.com/item?id=49724881) | Link: https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/

### TL;DR

NVIDIA introduced two early-stage paths for compiling Rust GPU kernels to PTX. cuda-oxide offers low-level SIMT control through a custom nightly rustc backend, while cutile-rs uses stable Rust and CUDA Tile IR so the compiler maps tiled operations to hardware. Both encode exclusive output ownership and catch some aliasing mistakes at compile time; neither is production-ready, and shared-memory safety remains unfinished. Commenters welcomed Rust’s momentum but debated CUDA lock-in, open hardware documentation, separate kernels, and higher-level alternatives such as Triton.

### Comment pulse

- CUDA integration trades portability for tooling → critics fear vendor lock-in, while defenders value concise launches and compile-time argument checks.
- Rust can prevent specific GPU races → ownership and partition types reject overlapping mutable access before execution.
- Open documentation remains lacking → readers want protocols, formats, ISA details, and performance data sufficient for independent drivers.

### LLM perspective

- View: The important advance is expressing launch and memory invariants in types, not merely replacing C++ syntax with Rust.
- Impact: Rust systems teams could keep host and kernel development unified while accepting NVIDIA-specific infrastructure.
- Watch next: Track stable-toolchain support, shared-memory safety, architecture coverage, interoperability, and production benchmarks against CUDA C++ and Triton.
