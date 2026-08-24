# Swift is a more convenient Rust

- Score: 127 | [HN](https://news.ycombinator.com/item?id=46841374) | Link: https://nmn.sh/blog/2023-10-02-swift-is-the-more-convenient-rust

### TL;DR

The author portrays Swift and Rust as similar LLVM languages with enums, pattern matching, generics, native or WASM targets and memory safety without tracing garbage collection. The distinction is defaults: Rust exposes ownership and borrowing first, adding reference-counted conveniences, while Swift favors familiar syntax, automatic reference counting and copy-on-write values, with lower-level ownership available. Swift is presented as easier for applications and increasingly cross-platform. Commenters challenged factual examples and convenience, citing an unnecessary Rust Box, older ownership precedents, performance cliffs, leaks, Xcode/SPM friction and a weaker non-Apple ecosystem.

### Comment pulse

- Rust users corrected two claims: ownership predates Rust, whose innovation is static borrow checking; Vec already supplies recursive indirection without Box.
- Swift practitioners cited type-inference stalls, module-wide recompilation, performance cliffs and ARC leaks as costs hidden behind convenient syntax.
- Cross-platform support exists — counterpoint: Linux users described Apple-centric libraries, tooling and documentation as materially weaker than Rust’s ecosystem.

### LLM perspective

- View: Syntactic convenience and progressive disclosure lower entry cost, but do not eliminate memory, tooling or performance complexity.
- Impact: Application developers may gain productivity; systems and non-Apple teams must verify runtime behavior and ecosystem coverage.
- Watch next: Non-Apple package compatibility, build benchmarks, ownership adoption, compiler diagnostics and production memory profiles.
