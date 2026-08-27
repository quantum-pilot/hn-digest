# Scala 3 slowed us down?

- Score: 161 | [HN](https://news.ycombinator.com/item?id=46182202) | Link: https://kmaliszewski9.github.io/scala/2025/12/07/scala3-slowdown.html

### TL;DR

A Scala 2.13-to-3.7.3 migration passed tests and ordinary load checks, yet heterogeneous production traffic later cut per-instance throughput and increased Kafka lag. Profiling showed Quicklens decoding consuming nearly half the CPU while the JIT worked heavily. A previously fixed Quicklens bug made chained evaluation inefficient under Scala 3; upgrading the library restored performance parity. The lesson is not that Scala 3 is inherently slower, but that language migrations can change metaprogramming-heavy dependencies enough to require realistic workloads, hotspot profiling, and targeted benchmarks.

### Comment pulse

- Readers praised the debugging narrative but questioned why a migration retained a library version whose relevant fix dated to 2022.
- Discussion distinguished Scala 3’s mandatory `inline` behavior from Scala 2’s advisory annotation and its possible JIT costs.
- Others generalized the lesson: runtime upgrades expose stale dependency behavior that correctness tests rarely catch.

### LLM perspective

- View: Migration risk lives in the combined compiler-library-workload system, not merely source compatibility.
- Impact: Performance-sensitive teams need representative payload diversity before staged rollout completes.
- Watch next: Benchmark known hotspots and compare profiles before and after every dependency or compiler upgrade.
