# A tale about fixing eBPF spinlock issues in the Linux kernel

- Score: 155 | [HN](https://news.ycombinator.com/item?id=47420388) | Link: https://rovarma.com/articles/a-tale-about-fixing-ebpf-spinlock-issues-in-the-linux-kernel/

### TL;DR
Superluminal’s Linux profiler was intermittently freezing entire systems on recent Fedora kernels. The authors tracked it to eBPF programs for context switches and high‑rate sampling both calling `bpf_ringbuf_reserve`, which uses a new “resilient queued spinlock” (rqspinlock). A series of subtle rqspinlock bugs meant recursive and cross‑CPU lock contention under NMIs was either misdetected or only checked after long delays, causing 1–250 ms stalls. Kernel maintainers implemented several fixes (in 6.19, backported to 6.17/6.18), and Superluminal added a workaround for older kernels.

---

### Comment pulse
- It’s Superluminal’s bug for “taking a lock in an interrupt handler” → rebuttal: eBPF code only calls helpers; locking is internal and should be verifier‑guarded — counterpoint: rqspinlock’s semantics still complicate reasoning about lock failures.
- eBPF sandboxing concern → rqspinlock lets misbehaving eBPF avoid hard deadlocks but can still cause transient DoS; correctness depends heavily on kernel helper behavior.
- Why unnoticed so long? → rqspinlock ringbuffer usage is new (≥6.15) and only certain high‑frequency, context‑switch+ringbuf workloads (like CPU profilers) trigger it.

---

### LLM perspective
- View: eBPF exposes kernel internals via “safe” helpers, so even tiny locking bugs can surface as user‑visible freezes.
- Impact: profiling/observability tools on newer kernels must assume helpers can fail under rare contention and handle NULL/timeout paths.
- Watch next: more systematic stress tests combining NMIs, tracepoints, and helpers; clearer per‑helper context guarantees in docs and the verifier.
