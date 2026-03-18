# Python 3.15's JIT is now back on track

- Score: 228 | [HN](https://news.ycombinator.com/item?id=47416486) | Link: https://fidget-spinner.github.io/posts/jit-on-track.html

## TL;DR
Python 3.15’s revived JIT has already beaten its original goals: around 11–12% faster than the tail-calling interpreter on macOS AArch64 and 5–6% on x86‑64 Linux, with some benchmarks over 2× faster. The turnaround came from community stewardship after funding cuts, systematic “mega-issues” that made JIT work approachable, and two key bets: a new tracing “dual dispatch” frontend and large-scale reference-count elimination. Discussion centers on trade-offs between compatibility and performance, JIT-hostile Python features, funding, and the need for deeper technical docs.

## Comment pulse
- Python 2→3 should’ve broken ABI harder → more room for internals like JITs to evolve freely—counterpoint: ecosystem migration costs and user hostility made that impractical.  
- Certain features impede JITs → `__del__`, arbitrary-precision ints, CPython C API, and GC visibility complicate optimizations; documenting “JIT-unfriendly” constructs could guide library authors.  
- Funding story matters → Faster CPython layoffs (Microsoft) and ARM hiring show JIT work’s value, but contributors still crave clearer high-level docs and explanations of tracing design.  

## LLM perspective
- View: This is a proof that a heavyweight runtime can gain real JIT wins via incremental, community-structured engineering, not just moonshot rewrites.  
- Impact: Python users on 3.15+ get free speedups; library authors may start caring about “JIT-friendliness” of APIs and patterns.  
- Watch next: Free-threading integration, profiler/debugger support for JITted code, and explicit guidance on features that disable or degrade JIT optimizations.
