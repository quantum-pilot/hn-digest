# Moving beyond fork() + exec()

- Score: 226 | [HN](https://news.ycombinator.com/item?id=48425528) | Link: https://lwn.net/SubscriberLink/1076018/16f01bbbb8e0d1f0/

- TL;DR  
    - Jonathan Corbet describes Li Chen’s proposed Linux “spawn templates” syscall: cache exec metadata for an executable, then spawn instances with argument/env/action descriptors, trimming fork+exec overhead by ~2%. Reviewers instead want a new primitive that creates a pristine, configurable process, probably via pidfds, enabling a first-class, fast posix_spawn in userspace. HN discussion questions whether kernel changes beat libc/userland solutions, explores io_uring-based configuration, and highlights tradeoffs around security filtering, multithreaded vfork behavior, and language runtimes bypassing libc.

- Comment pulse  
    - posix_spawn already mitigates fork/exec costs → glibc and GLib use it with vfork+CLONE_VM to avoid COW on low-memory systems, though its actions API is restrictive.  
    - io_uring as process-config engine → advocates want action lists in a ring for speed; others reject it over missing seccomp integration and bespoke BPF-only filtering.  
    - New spawn syscalls seem minor → some argue exec dominates; prefer worker pools/zygotes and libc posix_spawn — counterpoint: others hit multithreaded vfork scalability issues.

- LLM perspective  
    - View: A pidfd-based, builder-style spawn primitive that libcs wrap would reconcile performance, safety, and multi-language consistency.  
    - Impact: High-churn process launchers, sandboxes, and language runtimes gain predictable semantics and fewer fork-related edge cases under load.  
    - Watch next: benchmarks from apps using userspace empty-process prototypes versus kernel APIs, and agreement on a minimal spawn feature set.
