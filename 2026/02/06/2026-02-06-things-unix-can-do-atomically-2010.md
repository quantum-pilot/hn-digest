# Things Unix can do atomically (2010)

- Score: 243 | [HN](https://news.ycombinator.com/item?id=46909468) | Link: https://rcrowley.org/2010/01/06/things-unix-can-do-atomically.html

### TL;DR
The article catalogues filesystem and memory operations that Unix-like kernels guarantee to be atomic: renaming paths, creating links, mkdir, `open(O_CREAT|O_EXCL)`, file locks/leases with `fcntl`, shared `mmap`, and CPU-level atomic instructions. These primitives let you build inter-process/thread synchronization and locking without user-space mutexes, as long as you stay on a local filesystem and respect POSIX semantics. HN discussion adds newer tricks (`renameat2` exchanges), highlights portability gaps, and questions the correctness and clarity of the `mmap`/`msync` advice.

---

### Comment pulse
- Hard-link creation as a lock → `link()`/`ln` failing with `EEXIST` gives a simple, visible lock; even NFS often preserves this atomicity.  
- Atomic path swap with `mv --exchange` → `renameat2(RENAME_EXCHANGE)` is powerful but Linux-only and poorly deployed—counterpoint: the post’s scope is “Unix”, not Linux.  
- Portability and semantics worry people → POSIX locking seen as broken; `mmap`/`msync` behavior and durability are OS-specific and have caused real-world data-loss bugs.

---

### LLM perspective
- View: Prefer simple atomic filesystem operations as building blocks; keep higher-level locking minimal and clearly documented.  
- Impact: Systems programmers, DB authors, and ops gain safer deployment, locking, and coordination primitives with fewer race-prone mutexes.  
- Watch next: Standardization and wider deployment of `renameat2`-style exchanges; clearer, tested cross-OS semantics for `mmap`/`msync` and file locking.
