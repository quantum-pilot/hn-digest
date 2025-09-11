# Performance Improvements in .NET 10

- Score: 161 | [HN](https://news.ycombinator.com/item?id=45197608) | Link: https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-10/

TL;DR
.NET 10’s speedups come from many micro-optimizations that compound. The JIT now stack-allocates more closures and arrays via deeper escape analysis, devirtualizes array interface calls and guarded generics, and removes numerous bounds checks (e.g., Log2 tables, index-from-end). LINQ and iterator-heavy paths get notably faster, with fewer allocations and smaller codegen—often without app changes. HN reactions: meaningful real-world wins (smaller boxes, lower CPU), lively GC vs Rust-style ownership debate, and a reminder that profiling and end-to-end benchmarks still matter.

Comment pulse
- GC-backed C# rivals Rust/C++ when hotspots use arenas/manual buffers → productivity first, optimize locally — counterpoint: opaque compiler optimizations force profiling; explicit ownership is simpler.
- Upgrades cut infrastructure costs → teams report 10–20% CPU drops per major; memory reductions enable smaller instances; Kestrel/framework work offloads more.
- LINQ and iterator paths see 10–300× gains → but allocation behavior is harder to intuit; rely on BenchmarkDotNet and tooling.

LLM perspective
- View: .NET chips away at abstraction penalties by erasing closures/arrays and devirtualizing interfaces, narrowing the GC vs ownership tradeoff.
- Impact: Text formatting, LINQ-heavy pipelines, and collection iteration get faster; services can downsize VMs or pack more containers.
- Watch next: broader Span<T> APIs, Native AOT adoption, ARM64 SIMD parity, and end-to-end benchmarks quantifying P95/P99 improvements.
