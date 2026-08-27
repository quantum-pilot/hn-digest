# Julia 1.12 highlights

- Score: 166 | [HN](https://news.ycombinator.com/item?id=45519263) | Link: https://julialang.org/blog/2025/10/julia-1.12-highlights/

### TL;DR

Julia 1.12 adds experimental trimming for smaller, faster-starting compiled applications; world-age support for redefining constants and structs; compilation and dispatch tracing; improved threading defaults and CPU-affinity handling; task metrics; atomic-reference syntax; package workspaces and executable apps; real LLVM pointer types; and reproducible test RNG state. HN welcomed smoother Revise workflows, apps, and trimming, but users described an uneven ecosystem: strong numerical performance and production successes coexist with missing glue libraries, package bugs, maintenance gaps, compilation overhead, and competition from Python and Rust.

### Comment pulse

- Scientific computing remains Julia’s strongest niche → expressive mathematics, multiple dispatch, interactivity, and attainable performance serve long-running numerical workloads.
- Ecosystem maturity varies → excellent specialist packages coexist with missing infrastructure, abandoned maintenance, subtle bugs, and uncertain production trust.
- Trimming is promising but constrained → safe builds require statically inferable reachable code, limiting immediate use in dynamic programs.

### LLM perspective

- View: Version 1.12 improves both interactive development and deployment, attacking two longstanding sources of friction.
- Impact: Researchers and package authors gain better diagnostics, reproducibility, container behavior, monorepos, and command-line distribution.
- Watch next: Measure trimmed real applications, BOLT builds, startup latency, Revise integration, ecosystem reliability, and app adoption.
