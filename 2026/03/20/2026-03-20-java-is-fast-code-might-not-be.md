# Java is fast, code might not be

- Score: 183 | [HN](https://news.ycombinator.com/item?id=47454384) | Link: https://jvogel.me/posts/2026/java-is-fast-your-code-might-not-be/

### TL;DR

Java’s runtime was not the bottleneck in a deliberately inefficient order service; eight common coding patterns were. Replacing looped string concatenation, repeated full-list streams, hot-path formatting, boxed primitives, exception-driven parsing, coarse synchronization, recreated utilities, and virtual-thread pinning lifted measured throughput from 85,000 to 419,000 orders per second. The same changes cut runtime from 1,198 to 239 milliseconds, heap use above 1 GB to 139 MB, and GC pauses from 19 to four. Commenters accepted the profiling lesson but stressed that databases and external services often dominate real systems.

### Comment pulse

- Several readers suggested a 24-element hour array instead of a concurrent map, plus caching timezone objects.
- Commenters caught a numeric-overflow parsing bug; the article was updated, reinforcing the value of testing alongside profiling.
- Some wanted Java to eliminate these footguns — counterpoint: others favored explicit code whose costs remain visible.

### LLM perspective

- **View:** “Fast language” claims matter less than the allocation and contention profile of actual code.
- **Impact:** Small hot-path fixes can multiply into substantial fleet-level latency and compute savings.
- **Watch next:** JDK changes that neutralize common footguns without obscuring performance behavior.
