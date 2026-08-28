# Fil's Unbelievable Garbage Collector

- Score: 598 | [HN](https://news.ycombinator.com/item?id=45133938) | Link: https://fil-c.org/fugc

### TL;DR

Fil-C’s FUGC is described as a parallel, concurrent, accurate, non-moving collector that avoids global stop-the-world pauses. Compiler-inserted pollchecks and asynchronous soft handshakes scan roots, while a Dijkstra store barrier and repeated stack scans reach a marking fixpoint without a load barrier. Newly allocated objects are pre-marked, and SIMD bitvectors make sweeping a claimed small share of collection time. FUGC also integrates explicit `free`, finalizer queues, weak references, and weak maps, promising traps for use-after-free and double-free while reclaiming allocations omitted by manual code.

### Comment pulse

- Readers see potential for running existing C software more safely, particularly code unlikely to be rewritten.
- Questions center on overhead, embedded and 32-bit constraints, predictable memory use, and practical production experience.

### LLM perspective

- View: FUGC’s significance is combining managed reclamation with C-compatible explicit-free semantics and capability safety.
- Impact: It could preserve mature C code while trading some performance and platform reach for stronger temporal guarantees.
- Watch next: Independent benchmarks, real deployments, architecture support, and evidence that concurrency remains robust under diverse workloads.
