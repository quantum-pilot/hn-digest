# Musashi: Motorola 680x0 emulator written in C

- Score: 120 | [HN](https://news.ycombinator.com/item?id=46535540) | Link: https://github.com/kstenerud/Musashi

### TL;DR

Musashi 4.10 is a portable C emulator for Motorola’s 68000 through 68040 family, including several EC variants. Designed for portability and speed, it has matured through years of use in MAME. A basic host supplies memory callbacks, resets the core, executes cycle budgets, and raises interrupts. Configuration switches add more accurate interrupt handling, prefetch, address errors, function-code address spaces, tracing, multiple CPUs, and saved contexts. Its build generates opcode sources before compiling the core. The permissive license and configurable accuracy make it suitable as an embeddable emulation engine.

### Comment pulse

- The author recounted building Musashi in a tiny Tokyo apartment to see whether portable C could outperform MAME’s assembler core—and succeeding.
- Another reader described a 1994 C emulator with generated opcode dispatch whose source was later lost, highlighting preservation’s fragility.
- A JIT experimenter found limited speed improvement, while a reply suggested portability and maintainability are the more durable advantages.

### LLM perspective

- View: Musashi’s strength is a narrow host interface paired with selectable fidelity, keeping integration costs predictable.
- Impact: A portable, permissively licensed CPU core lets preservation projects spend effort on machine-specific behavior instead of rebuilding instruction semantics.
- Watch next: Conformance coverage across CPU variants, cycle-accuracy regressions, modern compiler portability, and how optional accuracy features affect performance.
