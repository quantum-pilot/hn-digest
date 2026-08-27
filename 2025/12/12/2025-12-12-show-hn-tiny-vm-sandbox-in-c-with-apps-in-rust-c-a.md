# Show HN: Tiny VM sandbox in C with apps in Rust, C and Zig

- Score: 184 | [HN](https://news.ycombinator.com/item?id=46249538) | Link: https://github.com/ringtailsoftware/uvm32

### TL;DR

uvm32 wraps a small RISC-V emulator in a dependency-free, asynchronous C99 sandbox for constrained devices. The project claims an STM32L0 footprint below 4 KB flash and 1 KB RAM, avoids dynamic allocation, limits instruction runs so guest code cannot stall the host, and exposes a minimally typed event-based FFI. Example guests span C, Rust, Zig, and assembly, including games and nested virtualization. It prioritizes portability and isolation over speed, frictionless calls, interpreted convenience, or bundled I/O and networking libraries.

### Comment pulse

- Readers praise the compact implementation and compiler ecosystem, while debating RISC-V decoding costs against embedded WebAssembly runtimes.
- The author says memory-mapped I/O simulation could be added by trapping the emulator’s existing mapped reads and writes.

### LLM perspective

- View: A stable compiler target is the project’s strongest advantage; its sandbox guarantees still deserve adversarial testing.
- Impact: Embedded hosts gain language choice and replaceable guest logic within a remarkably small claimed footprint.
- Watch next: Benchmarks, fuzzing results, memory-isolation audits, and comparisons with minimal WebAssembly interpreters will clarify tradeoffs.
