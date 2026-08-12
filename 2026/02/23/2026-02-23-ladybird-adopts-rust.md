# Ladybird adopts Rust

- Score: 1023 | [HN](https://news.ycombinator.com/item?id=47120899) | Link: https://ladybird.org/posts/adopting-rust/

### TL;DR

Ladybird is adopting Rust incrementally after Swift’s C++ interoperability and platform support fell short, despite earlier concerns that Rust’s ownership model poorly matched browser object graphs. The first migration covers LibJS parsing and bytecode generation. Human-directed Claude Code and Codex work produced about 25,000 lines in two weeks, with byte-for-byte parity across extensive test suites, no regressions, and no tracked slowdown. C++ remains central, while Rust and C++ will coexist as core maintainers port suitable components and later make the translated code more idiomatic.

### Comment pulse

- Readers praised behavior-locked parity before cleanup as a disciplined way to contain rewrite risk.
- Some feared another language pivot and cleanup-driven rewrite; supporters stressed the port is incremental, tested, and controlled by core maintainers.
- Several preferred AI as an augmentation tool under tight human direction, matching the project’s reported workflow.

### LLM perspective

- **View:** Behavioral parity makes AI-assisted translation auditable; memory safety does not excuse semantic drift.
- **Impact:** Core maintainers can trade months of mechanical work for review effort while preserving an immediate fallback.
- **Watch next:** Interop defects, idiomatic-cleanup regressions, contributor onboarding, post-C++ performance, and suitability of less-isolated subsystems.
