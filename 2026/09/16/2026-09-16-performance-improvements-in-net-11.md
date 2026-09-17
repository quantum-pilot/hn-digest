# Performance Improvements in .NET 11

- Score: 304 | [HN](https://news.ycombinator.com/item?id=49711424) | Link: https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-11/

### TL;DR

Microsoft catalogs hundreds of measured .NET 11 optimizations across JIT deabstraction, bounds checks, vectorization, garbage collection, threading, numerics, text, collections, I/O, networking, JSON, diagnostics, and cryptography. A major opt-in feature, runtime async, moves eligible async lowering from the C# compiler into the runtime and JIT, enabling fewer intermediate tasks and smaller binaries while targeting behavioral compatibility; Microsoft says some paths still regress and advises measurement. Commenters praised the engineering depth and focused particularly on runtime async, while disagreeing about the article’s prose.

### Comment pulse

- Layered optimization compounds → removing allocations, checks, indirections, syscalls, and instructions across common paths can benefit unchanged applications.
- Runtime async is the standout → JIT-visible suspension state may fuse direct await chains and reduce generated machinery.
- Technical depth won praise → readers valued reproducible benchmarks and explanations, though some disliked the lengthy style.

### LLM perspective

- View: The release emphasizes accumulated platform-wide efficiency rather than one universal headline speedup.
- Impact: Existing workloads may improve after upgrading, but microbenchmark gains require application-level confirmation.
- Watch next: Measure runtime-async compatibility, regressions, allocation reductions, binary size, and whether it becomes default in .NET 12.
