# A comparison of Ada and Rust, using solutions to the Advent of Code

- Score: 182 | [HN](https://news.ycombinator.com/item?id=45473861) | Link: https://github.com/johnperry-math/AoC2023/blob/master/More_Detailed_Comparison.md

- TL;DR
    - The author re‑implemented all Advent of Code 2023 solutions in Ada and Rust to compare idioms. Ada favors high‑level types (subranges, non‑zero arrays, enums as indices) and exceptions; Rust leans on UTF‑8 iterators, Result/Option, traits/derive, const generics, and cargo‑driven testing. Performance was mixed: Rust had fastest releases; Ada sometimes won by expressing numeric precision (digits) the compiler mapped to efficient types; Rust needed crates. Feature gaps trade off contracts/range types vs pattern‑matching/macros/ownership. HN debated ecosystem dominance, specs, concurrency, and string semantics.

- Comment pulse
    - Ada-like subranges and units are valued → fewer bugs; Nim and modern C++ emulate them, but they’re not standard.
    - Ecosystem/tooling decide real projects → Rust’s crates, IDEs, and community dominate — counterpoint: Ferrocene’s donated spec pushes Rust toward Ada-like standardization.
    - Rust concurrency is built-in via threads → async/Tokio optional; cancellation ergonomics vary by model and crate.

- LLM perspective
    - View: AoC highlights Ada’s declarative types vs Rust’s iterator/trait ecosystems; both enforce safety differently.
    - Impact: Choice shifts by domain: embedded/critical value Ada’s contracts; networked systems benefit from Rust’s crates and diagnostics.
    - Watch next: Align benches: enable overflow checks everywhere; track Rust formal-spec progress, Ada tooling (alire) speed, and const‑generic ergonomics.
