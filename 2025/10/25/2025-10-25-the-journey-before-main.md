# The Journey Before main()

- Score: 139 | [HN](https://news.ycombinator.com/item?id=45706380) | Link: https://amit.prasad.me/blog/before-main

- TL;DR
  - From execve to main, this primer walks through ELF loading, stacks, auxv, and the _start runtime that bridges to language-level main. Linux maps PT_LOAD segments, sets up argv/envp/auxv, and—when PT_INTERP exists—transfers control to the user-space dynamic linker, which relocates and loads shared libraries before invoking the program’s entry. Examples show RISC-V layouts and custom _start in Rust. HN corrects kernel-vs-ld.so responsibilities and debates bypassing libc with raw syscalls, portability trade-offs, and the scarcity of alternative loaders.

- Comment pulse
  - Dynamic linking is ld.so's job → Kernel maps PT_LOAD, notes PT_INTERP, jumps to dynamic linker; ld.so self-relocates, mmaps libs, applies relocations.
  - Avoid libc; use raw syscalls → Smaller, controllable startup costs — counterpoint: portability suffers; Win32-only builds avoid CRT but reduce cross-platform reach.
  - Pre-main experimentation → Packing logic into _start or single-function programs highlights runtimes’ overhead and control-flow flexibility.

- LLM perspective
  - View: Startup is a userland pipeline; choices around ld.so, libc, and _start materially affect size, latency, and control.
  - Impact: Minimal runtimes help containers, embedded, FaaS; better auxv/stack understanding improves debugging, crash triage, and security hardening.
  - Watch next: Benchmark glibc vs musl vs static startup; inspect with strace/readelf/LD_DEBUG; implement custom _start; verify auxv, PIE, ASLR.
