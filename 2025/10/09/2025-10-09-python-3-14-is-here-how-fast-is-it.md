# Python 3.14 is here. How fast is it?

- Score: 357 | [HN](https://news.ycombinator.com/item?id=45524702) | Link: https://blog.miguelgrinberg.com/post/python-3-14-is-here-how-fast-is-it

- TL;DR
  - Miguel Grinberg reruns his pure-Python benchmarks and finds CPython 3.14 is the fastest CPython yet. Single-threaded: ~27% faster than 3.13 on recursive Fibonacci; smaller gains on bubble sort. JIT yields negligible or mixed improvements; free-threading (no GIL) is slightly slower single-threaded but 2–3x faster on 4-thread CPU-bound workloads. PyPy is still dramatically faster (5–18x), with Rust far ahead and Node also beating CPython. HN debates benchmark realism, timing methodology, and the path to a GIL-less ecosystem.

- Comment pulse
  - Benchmark realism → Tight loops underweight strings/dicts and I/O; propose FastAPI or NumPy cases — counterpoint: scope was pure-Python CPU, author stated limits.
  - Methodology → Don’t time inside loops; use timeit to reduce jitter and average many runs.
  - Ecosystem/GIL → PyPy’s speed highlights divergence; free-threading needs C-FFI readiness; JIT is early and may trail PyPy for a while.

- LLM perspective
  - View: Upgrade to 3.14 for pure-Python CPU gains; use free-threading only for CPU-bound multi-threading.
  - Impact: C extension authors must harden nogil support; adoption hinges on ecosystem readiness.
  - Watch next: JIT wins on hot loops/strings/dicts, FT stability timelines, and standardized multi-core benchmarks beyond recursion/sorts.
