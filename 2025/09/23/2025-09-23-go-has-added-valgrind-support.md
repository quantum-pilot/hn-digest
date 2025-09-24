# Go has added Valgrind support

- Score: 456 | [HN](https://news.ycombinator.com/item?id=45344708) | Link: https://go-review.googlesource.com/c/go/+/674077

- TL;DR
    - Go added experimental Valgrind support. The driving use-case is leveraging Valgrind’s uninitialized-memory tracking to test constant‑time cryptography (ctgrind-style) and to inspect runtime memory handling. HN discusses why timing-based checks are unreliable under OS noise, how branch counters help but don’t prove constant time, and Valgrind’s tradeoffs: strong bug-finding, big slowdown, limitations with multithreading, and noise that often needs suppression files. Also noted: quality commit messages and rsc’s continuing involvement today.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - Goal: use Valgrind init tracking to verify constant-time crypto → avoids noisy timing tests; branch counters help but don't cover microarchitectural leaks.
    - Approach: assembly stub emits Valgrind client requests → avoids cgo/headers, fits bootstrapped toolchain, minimal dependencies.
    - Valgrind finds leaks and subtle bugs → heavy slowdown; multithreading realism limited; warnings can flood—counterpoint: suppressions files tame noise, even for Python/C++ hybrids.

- LLM perspective
    - View: Valgrind hooks primarily harden Go’s crypto and expose runtime memory misuses beyond the race detector’s scope.
    - Impact: Maintainers and large services gain deeper tests; more packages may add valgrind test targets and shared suppression sets.
    - Watch next: official docs, CI guidance, overhead benchmarks; initial bug reports; constant-time dashboards comparing ctgrind results across architectures.
