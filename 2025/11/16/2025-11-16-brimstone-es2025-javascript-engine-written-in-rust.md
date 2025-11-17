# Brimstone: ES2025 JavaScript engine written in Rust

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45944337) | Link: https://github.com/Hans-Halverson/brimstone

- TL;DR
  - Brimstone is a from-scratch JavaScript engine in Rust with a V8-Ignition–style bytecode VM, custom GC/RegExp/parser, and >97% test262 compliance. It targets ES2024 plus recent TC39 stage-4 features (missing SharedArrayBuffer/Atomics), isn’t production-ready, and leans on ICU4X for Unicode. HN highlighted its small release binary (~6.3 MB) versus Boa’s (~23 MB), largely due to ICU data choices, and benchmarks showing Brimstone often outpacing Boa despite being a mostly solo effort. Debate surfaced over “written in Rust” labeling and the engine’s “very unsafe” GC.

- Comment pulse
  - Brimstone 6.3 MB vs Boa 23 MB → Boa embeds ICU tables; Unicode data dominates size; build flags also matter — counterpoint: feature parity/hardening can increase size.
  - “Written in Rust” matters → signals ecosystem fit and fewer bug classes; discoverability — counterpoint: Rust isn’t magic, Brimstone’s GC uses significant unsafe.
  - Benchmarks → Brimstone nears Boa’s feature set and is often faster, sometimes ~2× on microbenches; impressive for a one-person, three-year project.

- LLM perspective
  - View: Promising Rust-native JS engine for embedding where V8/SpiderMonkey are heavy; unsafe GC warrants audits.
  - Impact: Rust apps, tooling, and WASI runtimes get a smaller, single-binary JS option.
  - Watch next: Ship Atomics/SharedArrayBuffer; upstream Unicode property sets to ICU4X; publish reproducible cross-engine perf and memory benchmarks.
