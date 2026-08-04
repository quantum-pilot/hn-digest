# Incremental – A library for incremental computations

- Score: 325 | [HN](https://news.ycombinator.com/item?id=48987822) | Link: https://github.com/janestreet/incremental

### TL;DR

Jane Street’s OCaml library builds dependency graphs for computations whose outputs update efficiently when inputs change, avoiding full recomputation. Its stated uses include spreadsheet-scale calculations, responsive GUI views, and derived data that remains synchronized with sources. Hacker News connected the approach to JavaScript signals, Rust’s Salsa, build systems, financial pricing engines, materialized views, and differential dataflow. Commenters cautioned that incremental computation and functional reactive programming overlap but differ: the former can derive delta-aware work, while reactive systems may simply invalidate and recompute affected nodes.

### Comment pulse

- The pattern spans ecosystems → signals, build systems, IDEs, SQL view maintenance, and dataflow engines all propagate changes through tracked dependencies.
- Implementation choices shape cost → height-based scheduling, complex-object updates, invalidation granularity, and arena allocation trade recomputation against memory and garbage collection.
- Domain-specific success can create institutional drag → Goldman’s pricing system minimized expensive differentiation but accumulated proprietary tooling and steep onboarding costs.

### LLM perspective

- **View:** Incrementality is cached dependency management with correctness obligations: speed comes from proving which prior work remains valid.
- **Impact:** Applications with localized changes and expensive recomputation gain most; rapidly changing dense graphs may erase the advantage.
- **Watch next:** Benchmark update locality, propagation depth, memory per dependency edge, scheduling overhead, complex-object handling, and onboarding complexity.
