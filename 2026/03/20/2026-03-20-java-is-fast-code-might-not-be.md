# Java is fast, code might not be

- Score: 183 | [HN](https://news.ycombinator.com/item?id=47454384) | Link: https://jvogel.me/posts/2026/java-is-fast-your-code-might-not-be/

## TL;DR
An AWS engineer shows that Java itself is fast, but common coding patterns quietly kill performance. Profiling a demo order service and fixing eight issues—string concatenation in loops, nested streams, hot-path String.format, autoboxing, exceptions as control flow, broad synchronization, recreating heavy utilities, and virtual-thread pinning—cut latency from 1,198ms to 239ms, 5x throughput, and far less heap/GC. HN agrees algorithmic complexity matters, but debates database vs CPU bottlenecks and how much Java’s design nudges developers toward these footguns.

## Comment pulse
- Many say main bottlenecks are DB/external calls → batching queries, using SQL directly beats loop tweaks — counterpoint: app CPU/heap gains still compound across fleets.  
- Discussion blames Java’s String/format APIs for steering into slow patterns → lack of compile-time formatting, ropes; others compare Zig/Rust/D’s faster compile-time format strings.  
- Several call synchronized a design mistake encouraging coarse locks; prefer actor-style or lock-free designs, occasional ReentrantLock — nitpickers favor arrays/primitives over maps for fixed ranges.  

## LLM perspective
- View: Treat JVM as fast; systematically profile to remove accidental O(n²), boxing, and contention in actual hotspots.  
- Impact: Teams can often cut CPU, memory, and GC overhead enough to downsize fleets or defer hardware upgrades.  
- Watch next: Part 2’s flame graphs, Java 24’s pinning fixes, and tooling that auto-detects these patterns in CI.
