# How Our Rust-to-Zig Rewrite Is Going

- Score: 386 | [HN](https://news.ycombinator.com/item?id=48933149) | Link: https://rtfeldman.com/rust-to-zig

- TL;DR  
Roc rewrote its 300k‑line compiler from Rust to Zig over 487 days, reaching feature parity while adding hot code loading, zero‑allocation routing, and a zero‑parse caching system. The team chose Zig for allocator-centric APIs, fine‑grained memory layout control, reuse of Zig’s LLVM bitcode emitter, and extremely fast incremental builds (tens of ms on 0.17). They acknowledge Rust’s borrow checker would have prevented two minor UAF bugs but argue overall safety outcomes and performance goals justify Zig for this particular compiler.

- Comment pulse  
  - “Compilers must be memory‑unsafe” is overstated → emitting code is safe; runtimes, hot‑reloading, and compile‑time execution are where unsafety actually appears.  
  - Zig’s ReleaseSafe is likely oversold → docs and experience suggest bounds checks and panics, not robust temporal safety or reliable UaF detection.  
  - Language choice feels under‑justified → critics say algorithms dominate performance and propose a small self‑hosted Roc compiler to explore design trade‑offs more scientifically.

- LLM perspective  
  - View: This is a rare, detailed case study showing how real compiler needs can outweigh generic “Rust vs Zig” narratives.  
  - Impact: Encourages systems projects to prioritize build latency, memory layout, and ecosystem fit over blanket “use Rust” advice.  
  - Watch next: Concrete benchmarks of Roc compile throughput, measurements of zero‑parse cache wins, and how Rust’s upcoming incremental work narrows the build‑time gap.
