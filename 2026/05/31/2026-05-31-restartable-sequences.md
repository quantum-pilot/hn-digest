# Restartable Sequences

- Score: 174 | [HN](https://news.ycombinator.com/item?id=48346019) | Link: https://justine.lol/rseq/

### TL;DR
Restartable sequences (rseq) are a Linux 4.18+ feature that lets user space define tiny, per‑CPU critical sections which the kernel either executes to completion or aborts and restarts if a thread is preempted or migrated. That gives you per‑CPU data structures without locks, atomics, or pinning threads, enabling huge speedups on many‑core CPUs (e.g., tens‑of‑x for malloc, orders‑of‑magnitude for simple counters). Today it’s Linux‑only, assembly-heavy, and used mainly in allocators, but it’s a strong candidate for future language/runtime integration.

---

### Comment pulse
- rseq semantics → You mark a short instruction range; if preempted inside it, the kernel jumps to an abort handler, guaranteeing the final write never happened.
- Per‑CPU in user space → rseq effectively exposes per‑CPU synchronization: you safely use per‑CPU sharded structures from user space without scheduler control—counterpoint: still limited to specific “single-commit” patterns.
- Ecosystem and tone → There’s a maintained C library (librseq) so most users need no assembly; some readers dislike the article’s “buy a huge workstation or be a dinosaur” framing.

---

### LLM perspective
- View: rseq is niche but powerful, ideal for allocators, work-stealing queues, and hot per‑CPU caches on high-core-count servers.
- Impact: Primarily affects libc, language runtimes, and high-performance infra (DBs, brokers); application developers benefit indirectly via faster libraries.
- Watch next: Wider OS support, stable C/C++ intrinsics, language-level constructs, and rigorous benchmarks comparing rseq designs to atomics and fine-grained locks.
