# Show HN: Tiny VM sandbox in C with apps in Rust, C and Zig

- Score: 184 | [HN](https://news.ycombinator.com/item?id=46249538) | Link: https://github.com/ringtailsoftware/uvm32

## TL;DR
uvm32 is a tiny, dependency-free RISC‑V–based virtual machine sandbox aimed at microcontrollers and other constrained systems. It’s a single C99 file with no dynamic allocation, non-blocking execution, and an event-based syscall interface, making it resilient against misbehaving guest code. Developers can compile apps in C, Rust, Zig, or assembly to run inside the VM, enabling “write once, run anywhere” on hardware lacking native toolchains. HN discussion centers on comparisons to WASM, code size, and embedded testing use cases.

---

## Comment pulse
- RISC‑V base → extremely compact core via mini-rv32ima; guest FP handled by compiler-emitted software routines rather than emulator hardware support.  
- Common VM vs WASM → RISC‑V gives stable, simple target; WASM offers browser portability and richer tooling—counterpoint: RISC‑V immediate decoding may be slow in software.  
- Use cases → attractive for medical devices and firmware testing; smaller than embedded WASM runtimes; memory-mapped I/O simulation suggested and shown feasible via existing hooks.

---

## LLM perspective
- View: A pragmatic sweet spot between custom interpreters and heavyweight VMs for embedded scripting and sandboxing.  
- Impact: Embedded vendors, testing teams, and hobbyists gain safer extension mechanisms on tiny MCUs without complex language runtimes.  
- Watch next: Benchmarks vs WAMR/libriscv, real-world device integrations, and hardened APIs for simulated peripherals and I/O.
