# Rewrite Bun in Rust has been merged

- Score: 465 | [HN](https://news.ycombinator.com/item?id=48132488) | Link: https://github.com/oven-sh/bun/pull/30412

- TL;DR  
    - Bun’s core has been rewritten from Zig to Rust and merged behind a canary flag. Architecture and features stay roughly the same, but binaries are smaller, benchmarks are neutral-to-faster, and many historical memory bugs should become compile‑time errors or automatic cleanups. The rewrite used Anthropic’s Claude and extensive unsafe Rust, sparking debate on how “one week” the port really was, how much was prepped in advance, and whether a deterministic Zig→Rust transpiler would have been better.

- Comment pulse  
    - AI rewrite hype is overstated → Porting guide, pointer types and Anthropic timing suggest prep and spin — counterpoint: guide is small vs 1M LOC.  
    - 1M+ Rust LOC alarms some → Bun bundles runtime, bundler, test runner, package manager and DB clients, so codebase predates port; size isn’t surprising.  
    - Heavy unsafe Rust worries people → ~10k unsafe blocks across 700+ files undercut safety gains; some advocate building a Zig→Rust transpiler instead.

- LLM perspective  
    - View: This is an early, high-profile case study of LLM-assisted large-scale refactoring of a production systems codebase.  
    - Impact: Tool vendors and infra teams may copy the workflow—porting legacy C/Zig/Go into Rust while preserving architecture and tests.  
    - Watch next: Reproductions, fuzzing parity tests, and metrics on bug rates, performance regressions, and long‑term maintenance costs vs Zig.
