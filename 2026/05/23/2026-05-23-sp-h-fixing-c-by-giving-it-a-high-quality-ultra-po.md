# sp.h: Fixing C by giving it a high quality, ultra portable standard library

- Score: 183 | [HN](https://news.ycombinator.com/item?id=48207043) | Link: https://spader.zone/sp/

### TL;DR

`sp.h` is a 15,000-line, single-header C99 library that replaces rather than wraps libc where platforms allow. It builds on roughly 40 low-level primitives, requires explicit allocators and error handling, avoids mutable globals, and uses pointer-plus-length strings for zero-copy parsing. The author prioritizes readability, modification, mainstream portability, and useful I/O abstractions over interface compatibility, obscure targets, SIMD, or universal peak performance. HN liked several primitives but challenged the pitch: extreme portability conflicts with x86-64/AArch64 scope, abbreviations hurt readability, pthread use weakens syscall purity, and redesigning C may simply create another language.

### Comment pulse

- Portability has multiple axes → compiler and OS breadth can coexist with narrow architectures — counterpoint: embedded targets are where much new C still lives.
- Pointer-length values generalize beyond strings → commenters advocated fat arrays with bounds-aware syntax but noted POSIX interoperability still expects null-terminated pointers.
- Lowest-level purity met pragmatism → direct `clone3` was suggested over pthreads — counterpoint: others called that nonportable and exceptionally risky.

### LLM perspective

- **View:** A standard-library replacement is effectively a dialect boundary; success depends on whether conventions remain legible to C programmers.
- **Impact:** Users gain explicit memory and modern strings but absorb migration, interop, training, auditing, and long-term maintenance costs.
- **Watch next:** Compare binaries, target coverage, safety defects, zero-copy gains, onboarding, and integration effort against libc and newer systems languages.
