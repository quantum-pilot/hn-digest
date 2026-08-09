# Python 3.15's JIT is now back on track

- Score: 228 | [HN](https://news.ycombinator.com/item?id=47416486) | Link: https://fidget-spinner.github.io/posts/jit-on-track.html

### TL;DR

CPython 3.15’s alpha JIT now beats its comparison interpreters by preliminary geometric means of 11–12% on macOS AArch64 and 5–6% on x86-64 Linux, reaching modest roadmap targets early despite individual results spanning a 20% slowdown to more than 100% speedup. Progress came from community-sized tasks, trace recording with compact dual dispatch, and reference-count elimination after Faster CPython lost its main sponsor. HN welcomed the recovery but wanted clearer architecture documentation, free-threading support, and guidance on Python features such as arbitrary-precision integers and `__del__` that obstruct optimization.

### Comment pulse

- Readers asked whether avoiding JIT-hostile features could unlock faster paths when their absence is provable.
- Python 2-to-3 debate resurfaced: some wished ABI breaks enabled deeper work — counterpoint: text semantics already imposed enormous migration costs.
- Microsoft reportedly moved sponsored staff elsewhere; commenters said Arm now funds several contributors.

### LLM perspective

- **View:** Reduced bus-factor risk may outlast any single optimization because performance work now has more maintainers.
- **Impact:** Most users receive moderate automatic gains; workload-specific regressions make benchmark selection decisive.
- **Watch next:** Free-threaded results, profiler support, release defaults, benchmark variance, and sustained infrastructure funding.
