# A tale about fixing eBPF spinlock issues in the Linux kernel

- Score: 155 | [HN](https://news.ycombinator.com/item?id=47420388) | Link: https://rovarma.com/articles/a-tale-about-fixing-ebpf-spinlock-issues-in-the-linux-kernel/

### TL;DR

Superluminal traced 250-millisecond Fedora freezes to two verified eBPF programs reserving the same ring buffer from context-switch and high-frequency sampling paths. A non-maskable interrupt could land after `rqspinlock` acquisition but before its held-lock record, defeating recursive-deadlock detection and forcing the full timeout. Moving bookkeeping before acquisition removed that stall; immediate deadlock checks and slow-path changes then fixed remaining 1–26 millisecond delays caused by deferred checks and NMI starvation. Fixes shipped in Linux 6.19 and were backported to 6.17–6.18. HN praised the diagnosis but debated kernel versus caller responsibility.

### Comment pulse

- One critique blamed interrupt-context locking → the pattern is traditionally unsafe — counterpoint: Superluminal called a verifier-approved helper whose internal lock was undocumented.
- The minimized reproducer proved broad relevance → ordinary ring-buffer reserve-and-discard calls triggered the bug without the profiler’s larger codebase.
- Readers valued the deep dive → it connected visible freezes to MCS queues, recursive detection, timeout timing, and NMI scheduling.

### LLM perspective

- **View:** A verifier-backed API must either reject unsafe contexts or make its documented failure path safe under them.
- **Impact:** High-frequency eBPF profilers gain stable ring-buffer behavior on fixed kernels and a workaround for older releases.
- **Watch next:** Backport adoption, regressions under extreme NMI rates, verifier restrictions, and similar helper functions hiding interrupt-sensitive locks.
