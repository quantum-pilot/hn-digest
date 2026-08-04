# Restartable Sequences

- Score: 174 | [HN](https://news.ycombinator.com/item?id=48346019) | Link: https://justine.lol/rseq/

### TL;DR

Linux restartable sequences let user-space code perform tiny per-CPU operations without mutexes or atomics. A thread publishes a critical-section descriptor in kernel-shared TLS; if preemption or CPU migration occurs before the final commit instruction, the kernel redirects execution to an abort handler for retry. The author demonstrates sharded counters and linked-list push/pop in x86-64 and ARM64 assembly, reporting dramatic multicore gains for Cosmopolitan malloc and counters. The tradeoffs are Linux-only support, handwritten assembly, careful data layout, and fallback strategies for portable software.

### Comment pulse

- Readers converged on a transactional model → per-CPU mutations commit with one final store; scheduler interruptions trigger retry before that store.
- Handwritten assembly is not mandatory → commenters highlighted maintained librseq helpers for common counters and linked-list operations.
- The expensive-workstation framing polarized readers → some saw elitism — counterpoint: others read sarcasm and noted discounted hardware or rentable test capacity.

### LLM perspective

- **View:** rseq is best treated as a specialized per-CPU primitive, not a general replacement for locks or transactional memory.
- **Impact:** Allocators and telemetry counters can reduce cacheline contention substantially on high-core Linux systems, provided access patterns fit.
- **Watch next:** Compiler or language support, wider librseq adoption, reproducible benchmarks, memory-reclamation techniques, and non-Linux equivalents.
