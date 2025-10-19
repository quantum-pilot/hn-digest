# Flowistry: An IDE plugin for Rust that focuses on relevant code

- Score: 155 | [HN](https://news.ycombinator.com/item?id=45627692) | Link: https://github.com/willcrichton/flowistry

- TL;DR
    - Flowistry is a VSCode plugin for Rust that performs information-flow analysis over MIR to fade out code irrelevant to a selected variable/expression. It enables “focus mode” for large functions, with mark/select commands. Known limits: incomplete interior mutability handling (Arc/Mutex, RefCell), single-function scope (closures/async separate), potential over-inclusion from type-based effects, and Rust 1.73 MSRV. HN frames it as program slicing, noting Rust’s ownership makes it feasible, questioning rust-analyzer integration, and flagging challenges around back-references and interior mutability.

- Comment pulse
    - Flowistry is program slicing for Rust → shows transitive dependencies/uses; great for large functions. — counterpoint: Without ownership, other languages’ slices are less sound.
    - Why not rust-analyzer integration → RA lacks MIR/borrow-checker data; Flowistry depends on rustc internals, so it must run as a separate tool.
    - Interior mutability limits matter for back-references → Rc/RefCell patterns hide aliasing across lifetimes; static, cross-function checks and diagnostics remain difficult.

- LLM perspective
    - View: A practical, MIR-backed slicer that turns Rust’s ownership into actionable code comprehension and safer refactoring.
    - Impact: Maintainers of huge Rust functions, security auditors, and toolbuilders get sharper dependency maps and fewer irrelevant lines to read.
    - Watch next: Handle interior mutability aliasing, cross-function/async analysis, publish performance on large crates, and explore stable rustc APIs.
