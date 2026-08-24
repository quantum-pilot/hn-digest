# Things Unix can do atomically (2010)

- Score: 243 | [HN](https://news.ycombinator.com/item?id=46909468) | Link: https://rcrowley.org/2010/01/06/things-unix-can-do-atomically.html

### TL;DR

This 2010 catalog shows how POSIX-like kernels provide atomic building blocks for thread-safe and multiprocess programs without wrapping every operation in application locks. Path-based tools include atomic same-filesystem rename, hard or symbolic link creation, exclusive file creation, and mkdir; file descriptors add advisory region locks and leases, while shared mappings and compiler atomics cover memory. Commenters added Linux’s newer atomic path exchange and portable link-based locking but challenged mmap/msync guidance, NFS assumptions, and cross-Unix portability.

### Comment pulse

- renameat2 with RENAME_EXCHANGE atomically swaps paths on Linux—counterpoint: coreutils support remains uneven and the primitive is not generic Unix.
- Hard-link creation supports visible portable-ish locks; one reader reported even NFS honoring it, despite the article’s broader local-filesystem warning.
- Readers disputed mmap/msync: shared mappings already expose writes, durability differs by platform, and confusing visibility with disk persistence can lose data.

### LLM perspective

- View: Kernel atomicity is valuable only when its exact scope, failure mode, filesystem, and portability guarantees are documented.
- Impact: Developers can remove redundant mutexes and simplify coordination, but mistaken assumptions create rare corruption and recovery failures.
- Watch next: POSIX guarantees, filesystem behavior, crash durability, network mounts, platform tests, C atomics, and rename variants.
