# Show HN: Tiny VM sandbox in C with apps in Rust, C and Zig

- Score: 184 | [HN](https://news.ycombinator.com/item?id=46249538) | Link: https://github.com/ringtailsoftware/uvm32

### TL;DR

uvm32 packages a RISC-V interpreter and management layer into dependency-free C99 for embedded hosts, using no dynamic allocation and under 4 KB of flash plus 1 KB of RAM on an STM32L0. Hosts run guest instructions in bounded slices, receive events for syscalls, errors, and completion, and expose only chosen capabilities through a minimal FFI. Guest examples compile from C, Rust, Zig, and assembly, including games and a self-hosting demonstration. The project favors portability, isolation, and robustness over speed, frictionless interop, or batteries-included scripting.

### Comment pulse

- Reviewers praised the compact wrapper around mini-rv32ima and noted software floating point comes from compiler routines, not emulated hardware instructions.
- Wasm offers browser support and a purpose-built sandbox model — counterpoint: configurable RISC-V can provide a smaller, stable target.
- One commenter proposed memory-mapped I/O simulation for firmware tests; the author identified existing read and write traps that could support it.

### LLM perspective

- View: This is a capability boundary and portable compilation target, not a general operating-system emulator.
- Impact: Tiny hosts can isolate plugins and accept modern-language guest code without maintaining native toolchains for every microcontroller.
- Watch next: Fuzzing, syscall validation, memory-mapped I/O hooks, worst-case execution costs, code-size comparisons, and production integrations.
