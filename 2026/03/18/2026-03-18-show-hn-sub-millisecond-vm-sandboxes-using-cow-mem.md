# Show HN: Sub-millisecond VM sandboxes using CoW memory forking

- Score: 293 | [HN](https://news.ycombinator.com/item?id=47412569) | Link: https://github.com/adammiribyan/zeroboot

### TL;DR

Zeroboot is a working prototype that snapshots a preloaded Firecracker VM, then creates isolated KVM forks by privately mapping snapshot memory with copy-on-write and restoring CPU state. It reports 0.79 ms median spawn latency, 1.74 ms p99, about 265 KB incremental memory per sandbox, roughly 8 ms for Python fork-and-execute, and 1,000 forks in 815 ms. HN found the primitive promising for speculative agent execution but stressed that networking, files, terminals, image updates, and lifecycle management remain the harder product.

### Comment pulse

- Cloning a snapshot duplicates CSPRNG and ASLR state; the author said kernel entropy injection and userspace reseeding remain roadmap work.
- Stale base images and diverging state complicate updates, reproducibility, and long-lived workloads beyond the fast fork itself.
- Several readers preferred clean one-second boots for simplicity — counterpoint: speculative execution can materially benefit from sub-millisecond forks.

### LLM perspective

- **View:** The latency result validates a mechanism, not yet a complete sandbox service.
- **Impact:** Agent platforms could cheaply launch many candidate trajectories and discard losing branches.
- **Watch next:** Independent realistic-I/O benchmarks, adversarial isolation audits, and behavior under sustained memory pressure.
