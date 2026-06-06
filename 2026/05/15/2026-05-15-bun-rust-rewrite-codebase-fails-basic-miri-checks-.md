# Bun Rust rewrite: "codebase fails basic miri checks, allows for UB in safe rust"

- Score: 352 | [HN](https://news.ycombinator.com/item?id=48150900) | Link: https://github.com/oven-sh/bun/issues/30719

### TL;DR
Bun’s AI-assisted Zig→Rust rewrite shipped a core bug: a “safe” `PathString::init` erased lifetimes, letting callers create dangling `&[u8]` and thus undefined behavior in safe Rust. Miri immediately flags it; a maintainer reproduces, marks the function (and a similar iterator) `unsafe`, audits ~70 call sites, and adds tests to keep them unsafe. HN debates whether this kind of unsafe-heavy, AI-generated port is acceptable, the lack of early miri/CI guardrails, and what it implies for trust in Bun under Anthropic.

---

### Comment pulse
- Deterministic translators (zig translate-c, c2rust) → still emit verbose, pointer-emulating unsafe Rust and preserve C’s bugs—counterpoint: at least their behavior is predictable and auditable.  
- Trust erosion → people drawn to Bun’s Zig/Andrew Kelley “taste” see the AI-heavy Rust port as Anthropic experimenting on users, not building a dependable tool.  
- Early-port tolerance → UB in unsafe wrappers is expected during translation, but exposing it via safe APIs and merging to main without miri is seen as a process failure.

---

### LLM perspective
- View: AI ports are viable only with strict constraints: predeclared unsafe boundaries, mandatory miri, and human review of every changed unsafe block.  
- Impact: Maintainers will need clearer AI-usage policies; users will increasingly judge projects on how they manage unsafe and automated code.  
- Watch next: Bun’s CI for miri/clippy, a systematic unsafe audit, and whether they publish a candid postmortem and updated contribution guidelines.
