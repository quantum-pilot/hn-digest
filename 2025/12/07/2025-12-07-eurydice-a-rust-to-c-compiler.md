# Eurydice: a Rust to C compiler

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46178442) | Link: https://jonathan.protzenko.fr/2025/10/28/eurydice.html

### TL;DR
Eurydice is a Rust-to-C compiler that hooks into Rust’s MIR, generating relatively readable C so Rust libraries can target legacy, obscure, or C-only toolchains. It monomorphizes generics, reconstructs control flow and data layouts, and uses peephole optimizations plus glue macros to keep output maintainable, at the cost of code size and some undefined-behavior caveats. HN discusses C’s role as universal ABI, why not just use LLVM backends, prior art, and whether cryptography survives such double compilation safely.

---

### Comment pulse
- Readable generated C is hard → author has prior work (Mezzo, friendly C generation); Eurydice continues that underexplored direction of maintainable transpiled C.  
- Why not LLVM? → Embedded teams must use vendor C compilers; C acts as portable IR for weird chips—counterpoint: LLVM’s IRs are already retargetable.  
- Crypto as demo worries some → double compilation through high-level toolchains risks breaking constant‑time behavior; today’s LLVM/GCC lack formal timing-preservation guarantees.  

---

### LLM perspective
- View: Rust-to-C as transitional path makes sense; it decouples language choice from downstream compiler and ecosystem constraints.  
- Impact: If Eurydice handles more stdlib and traits, vendors can ship Rust code while guaranteeing C-only consumers a path.  
- Watch next: benchmarks vs native Rust/C, constant‑time crypto case studies, and tools to auto‑partition monomorphized code into sensible C modules.
