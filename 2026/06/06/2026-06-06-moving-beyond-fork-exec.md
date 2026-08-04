# Moving beyond fork() + exec()

- Score: 226 | [HN](https://news.ycombinator.com/item?id=48425528) | Link: https://lwn.net/SubscriberLink/1076018/16f01bbbb8e0d1f0/

### TL;DR

Li Chen proposed Linux spawn templates that cache executable metadata for programs repeatedly launching the same binary, then accept per-run arguments, environment, file-descriptor, directory, and signal actions. Benchmarks showed only about 2% improvement, and reviewers objected to retaining `fork()`. The emerging alternative is a pidfd-based builder: create a pristine process, configure it incrementally, then execute, enabling a native user-space `posix_spawn()`. Discussion split over whether this warrants kernel complexity: copy-on-write still scales with page tables, but existing `vfork()`, libc, persistent workers, and zygotes may already solve practical bottlenecks.

### Comment pulse

- Copy-on-write does not make `fork()` constant-time → page tables and VMAs still scale with address space; large processes can pause noticeably.
- `fork()` preserves composability → child setup can call familiar APIs — counterpoint: multithreaded children inherit ownerless locks and may call only async-signal-safe functions.
- Demand evidence before adding ABI → commenters requested real applications and end-to-end benchmarks against libc `posix_spawn()`, persistent subprocesses, and zygotes.

### LLM perspective

- **View:** A builder API is valuable mainly for explicit state and safer composition, not templates tied to repeated binaries.
- **Impact:** Runtimes could launch subprocesses without cloning irrelevant parent state, reducing latency variance and inherited-state bugs.
- **Watch next:** Prototype pidfd configuration in userspace; benchmark large multithreaded programs; test seccomp, credentials, errors, and file-descriptor closure.
