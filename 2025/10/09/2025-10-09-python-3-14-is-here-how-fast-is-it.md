# Python 3.14 is here. How fast is it?

- Score: 357 | [HN](https://news.ycombinator.com/item?id=45524702) | Link: https://blog.miguelgrinberg.com/post/python-3-14-is-here-how-fast-is-it

### TL;DR

Two deliberately narrow pure-Python benchmarks on Linux and macOS found CPython 3.14 faster than earlier CPython releases: about 27% over 3.13 for recursive Fibonacci and roughly 22% for bubble sort. The experimental JIT provided little consistent benefit. Free-threaded 3.14 remained slower for single-threaded work but ran four independent CPU-heavy threads about three times faster than standard CPython for Fibonacci and twice as fast for sorting. PyPy dominated these scripts. The author cautions that tiny integer-heavy tests excluding native dependencies do not represent typical applications.

### Comment pulse

- Readers requested broader workloads involving strings, dictionaries, web frameworks, NumPy, asyncio, and alternative runtimes.
- Benchmark-method discussion emphasized using established timing tools and avoiding measurement inside tight loops.

### LLM perspective

- View: The strongest result is improved free-threaded scaling, not the immature JIT or cross-language leaderboard.
- Impact: CPU-bound threaded programs may finally benefit from ordinary threads, subject to extension compatibility and workload testing.
- Watch next: Real applications, native-extension readiness, memory overhead, JIT maturity, and repeated statistically robust measurements.
