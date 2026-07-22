# Incremental – A library for incremental computations

- Score: 325 | [HN](https://news.ycombinator.com/item?id=48987822) | Link: https://github.com/janestreet/incremental

## TL;DR
- Incremental is an OCaml library for self-adjusting computations: you define a dependency graph of derived values, and it recomputes only affected nodes when inputs change. It targets spreadsheet-like calculations, GUIs, and keeping derived data synchronized. Hacker News discussion connects it to modern “signals” in JavaScript frameworks, Rust libraries like Salsa, and dataflow systems such as Differential Dataflow and Noria, plus long-standing financial-pricing engines. Overall theme: incremental computation is a general pattern behind many reactive and build-like systems.

## Comment pulse
- Signals-style reactive graphs → Incremental resembles JavaScript signals and Rust libraries like Leptos/Salsa; algorithms differ in scheduling, dependency tracking, and handling of object updates.  
- Incremental vs FRP → commenters distinguish delta-based incremental computation from classic FRP, and liken Incremental to build systems like tup or JetBrains Noria’s engine.  
- Financial and data systems → similar graphs power Goldman pricing engines, Differential Dataflow, DBSP, Materialize, and Clojure’s Javelin; powerful but can produce opaque, hard-to-onboard stacks.  

## LLM perspective
- View: Incremental exemplifies treating programs as dependency graphs, enabling principled partial recomputation instead of ad-hoc caches and invalidation flags.  
- Impact: Strongest payoff in UIs, analytics pipelines, build systems, and finance where workloads are repetitive, stateful, and latency-sensitive.  
- Watch next: standardization of signals, ergonomic Rust/TypeScript libraries, and better visualization/debugging tools to keep large incremental graphs understandable.
