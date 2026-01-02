# Python numbers every programmer should know

- Score: 258 | [HN](https://news.ycombinator.com/item?id=46454470) | Link: https://mkennedy.codes/posts/python-numbers-every-programmer-should-know/

### TL;DR
This piece systematically benchmarks Python latency and memory costs for core operations, collections, JSON libs, web frameworks, I/O, DBs, and async. It shows most in-process primitives are tens of nanoseconds (attribute read, dict/set lookup, list append, function call), while imports, file I/O, databases, and asyncio introduce microseconds to milliseconds of overhead. Memory overhead is substantial (ints ~28 B, empty list 56 B, regular instances ~3× `__slots__`). Alternatives like `orjson`/`msgspec` and lightweight ASGI frameworks are significantly faster. HN debates whether such micro-benchmarks are practically useful versus focusing on algorithms, profiling, and language choice.

---

### Comment pulse
- Knowing these costs helps fix sloppy hot loops and keep large Python systems viable → big shops (Instagram, Dropbox, OpenAI) prove Python can scale—counterpoint: when this matters, Python often isn’t the right tool.  
- Critics: absolute ns/byte figures are less useful than time/space complexity and profiling → optimize algorithms first, then drop hot paths to C/Rust or Cython if needed.  
- Some argue Python survives thanks to fast C extensions and is “surprisingly slow” at basics → others accept overhead as tradeoff for productivity and cheap hardware.

---

### LLM perspective
- View: Treat these numbers as intuition-builders and relative ratios, not rules; combine with profiling and algorithmic thinking.  
- Impact: Python backend devs, library authors, data engineers, and tool builders making tradeoffs around JSON, async, and storage.  
- Watch next: Re-benchmark on future CPython releases, alternative interpreters, and under real workloads (networked DBs, multi-process, containerized environments).
