# Clojure Hosted on Go

- Score: 194 | [HN](https://news.ycombinator.com/item?id=48578326) | Link: https://github.com/glojurelang/glojure

### TL;DR

Glojure is an early-stage, tree-walk Clojure interpreter hosted on Go, making Go and Glojure values usable in either direction. Version 0.3.0, requiring Go 1.24, offers a REPL, script and expression execution, embeddability inside Go programs, concurrency, and access to many standard-library packages; generated package maps expose more APIs. It runs a substantial transformed subset of core Clojure, but still lacks features, speed, stable compatibility, and tooling. HN response was enthusiastic but centered on maturity, REPL behavior, and ecosystem stewardship.

### Comment pulse

- Go is an attractive host → commenters valued its runtime, toolchain, and ecosystem, and pointed to Lisette as another language targeting them.
- REPL behavior drew scrutiny → readers contrasted direct interpretation with Go compile-and-run loops that often make interactive evaluation slow.
- Dialect progress matters → commenters asked how far parity advanced since 2024 and noted both original and forked repositories remain synchronized.

### LLM perspective

- **View:** Its strongest niche is embeddable scripting for Go applications that want Lisp expressiveness without adopting the JVM.
- **Impact:** Go developers gain REPL-driven extensibility; Clojure users trade mature libraries and performance for native host interoperability.
- **Watch next:** Benchmark startup, REPL latency, call overhead, concurrency, memory use, core-library coverage, and package-map ergonomics before production adoption.
