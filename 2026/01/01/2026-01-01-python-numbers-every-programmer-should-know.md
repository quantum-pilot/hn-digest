# Python numbers every programmer should know

- Score: 258 | [HN](https://news.ycombinator.com/item?id=46454470) | Link: https://mkennedy.codes/posts/python-numbers-every-programmer-should-know/

### TL;DR

Benchmarks on CPython 3.14.2 and an M4 Pro map common operations from nanoseconds to milliseconds and quantify Python’s object overhead. Highlights include 22 ns dictionary lookups, 29 ns list appends, 9 μs file opens, 104 ms FastAPI imports, 28-byte integers, and regular five-attribute objects exceeding three times the size of slotted versions. HN debated whether such constants guide useful optimization or distract from algorithms, profiling, and moving hot paths into native extensions; results remain machine- and workload-specific.

### Comment pulse

- Knowing relative costs helps rescue mature Python systems → inefficient hot loops may matter more than language replacement.
- Profile before memorizing constants → real bottlenecks usually involve algorithms, I/O, imports, or production-specific workloads.
- Crossing Python’s ceiling has established remedies → C, Rust, Cython, JITs, and optimized libraries preserve higher-level scaffolding.

### LLM perspective

- View: The table is most useful as an intuition reset and experiment checklist, not a portable performance contract.
- Impact: Developers can prioritize data structures, import latency, serialization, and object density before undertaking rewrites.
- Watch next: Reproduce suspicious measurements, particularly database deletion and framework latency, across platforms and Python versions.
