# Unexpected productivity boost of Rust

- Score: 525 | [HN](https://news.ycombinator.com/item?id=45041286) | Link: https://lubeno.dev/blog/rusts-productivity-curve

- TL;DR
    - Author argues Rust becomes more productive as projects grow because the compiler enforces invariants (ownership, lifetimes, Send/Sync), enabling fearless refactoring. A real bug: holding a MutexGuard across an await made a handler’s future non-Send; the compiler flagged it before runtime. By contrast, a TypeScript redirect bug stemmed from browser event-loop semantics, slipping to production. Tests help, but Rust encodes many pitfalls into the type system. Zig example shows how small design choices affect guarantees. HN agrees Rust often “just works” when it compiles, while debating TS blame and “static typing vs Rust’s extras.”

- Comment pulse
    - If it compiles, it often works → ownership, Send/Sync, and libraries prevent misuse; big refactors finish once the build turns green.
    - TS bug is Web API semantics, not TS → href defers navigation; early return fixes — counterpoint: Rust APIs could encode single-use ownership to prevent double navigation.
    - Not just “static typing” → Rust adds ownership, enums + exhaustive matching, traits; tradeoff: strictness impedes half-done refactors.

- LLM perspective
    - View: Rust front-loads effort, then scales via compile-time guarantees; async/threading bugs surface early.
    - Impact: Backend/service teams, library authors, and anyone refactoring large codebases benefit; fewer heisenbugs.
    - Watch next: Clippy lints for “lock across await,” safer web-API wrappers with ownership semantics, Zig error-set typing ergonomics.
