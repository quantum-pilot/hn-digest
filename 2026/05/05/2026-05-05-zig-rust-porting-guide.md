# Zig → Rust porting guide

- Score: 698 | [HN](https://news.ycombinator.com/item?id=48016880) | Link: https://github.com/oven-sh/bun/commit/46d3bc29f270fa881dd5730ef1549e88407701a5

## TL;DR

Bun added a very detailed “Zig → Rust porting guide” for an experiment: auto‑translating its Zig core to Rust (Phase A) using Claude, then hand-fixing it later. The doc pins down file layout, crate mapping, pointer/allocator lifetimes, error types, strings, collections, and JSC GC rules so ports stay behaviorally identical and reviewable, even if they don’t compile yet. HN discussion centers on whether this enormous AI‑assisted rewrite is sensible engineering R&D or unreviewable “vibe coding,” especially post‑Anthropic acquisition.

---

## Comment pulse

- Bun maintainer: this is exploratory, may be thrown away; goal is to compare Rust vs Zig on tests, performance, and maintainability—overreaction fueled by assumptions.  
- Skeptics: 700k+ line AI diff is effectively unreviewable; worry about regressions, open bugs, and LLM nondeterminism vs past deterministic C→Go tools.  
- Optimists: LLMs excel at mechanical rewrites when architecture and tests exist; Rust could eliminate many Bun segfaults—counterpoint: success hinges on disciplined validation and review.

---

## LLM perspective

- View: This guide exemplifies “LLM as compiler front‑end”: humans supply strict semantics, models do the rote translation.  
- Impact: If successful, large legacy systems can be migrated across languages faster, shifting effort to specs, tests, and audits.  
- Watch next: Per‑crate test parity, perf benchmarks Zig vs Rust, tooling to replay commits or auto‑diff semantics rather than just code.
