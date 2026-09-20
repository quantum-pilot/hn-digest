# What Zig felt like, coming from Rust

- Score: 240 | [HN](https://news.ycombinator.com/item?id=49766637) | Link: https://besok.github.io/posts/what-zig-felt-like-coming-from-rust/

### TL;DR

After seven years with Rust, the author reimplemented an RFC 9535 JSONPath library in Zig. Zig felt direct, fast, CLI-friendly, and naturally flatter in project structure, but its imperative style, explicit allocators, manual ownership, young libraries, shifting standard APIs, and weaker IDE experience made the resulting code less readable and more error-prone for this workload. TestAllocator and failing-allocation tests caught leaks and double frees that Rust prevents through Drop and moves. HN debated whether mutation was Zig-imposed, while broadly contrasting Zig's control with Rust's safety and mature tooling.

### Comment pulse

- Memory safety is Rust's decisive distinction → ownership rules eliminate common leak, error-path, use-after-move, and double-free shapes before production.
- Zig permits functional structure but discourages it economically → immutable transformations require allocations and bookkeeping, though commenters called mutation a programmer choice.
- Tooling maturity remains uneven → Zig's cross-compilation and C interop impressed readers, but language-server breakage and changing APIs complicate serious maintenance.

### LLM perspective

- View: Zig exposes mechanisms Rust deliberately abstracts, improving control and debuggability while transferring ownership correctness back to tests and discipline.
- Impact: Systems programmers gain a modern C-like option, but teams must budget for allocator design, failure-path testing, and ecosystem gaps.
- Watch next: Language stability, ZLS dependency support, Unicode-capable libraries, standard-library churn, and comparative maintenance costs on larger projects.
