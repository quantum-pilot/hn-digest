# Scala 3 slowed us down?

- Score: 161 | [HN](https://news.ycombinator.com/item?id=46182202) | Link: https://kmaliszewski9.github.io/scala/2025/12/07/scala3-slowdown.html

### TL;DR

A Scala 2.13-to-3.7.3 migration passed tests and ordinary load checks, yet production throughput fell hours later under fine-grained, heterogeneous Kafka workloads. Profiling showed decoding and JIT compilation consuming CPU because an old Quicklens bug made chained evaluations expensive under Scala 3; upgrading the library restored parity. The author’s lesson is to benchmark realistic hotspots and scrutinize metaprogramming-heavy dependencies during language upgrades. Commenters praised the debugging, debated Scala 3’s direction, and disagreed whether keeping older dependencies was prudent.

### Comment pulse

- Dependency strategy divides teams → minimal upgrade scope reduces simultaneous change — counterpoint: stale releases can retain already-fixed compatibility defects.
- Broader Scala criticism felt misplaced → some blamed language governance and complexity, while others said the diagnosis vindicated careful profiling.

### LLM perspective

- View: Cross-version compatibility is behavioral, not merely syntactic; green tests cannot certify throughput.
- Impact: Performance-sensitive JVM teams need workload-shape benchmarks in staged language migrations.
- Watch next: Track allocation, generated code size, JIT time, and dependency versions across representative payload mixes.
