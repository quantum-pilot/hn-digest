# AWS engineer reports PostgreSQL perf halved by Linux 7.0, fix may not be easy

- Score: 389 | [HN](https://news.ycombinator.com/item?id=47644864) | Link: https://www.phoronix.com/news/Linux-7.0-AWS-PostgreSQL-Drop

### TL;DR
An AWS engineer found PostgreSQL throughput drops to about half on Linux 7.0 running on a 96‑core Graviton4 (ARM) server, traced to new kernel preemption-mode simplifications that increase time spent in a userspace spinlock. A proposed patch to restore PREEMPT_NONE as default may be rejected; kernel maintainer Peter Zijlstra instead suggests PostgreSQL adopt the new Restartable Sequences time-slice extension added in 7.0. The thread raises bigger questions about kernel–userspace responsibilities, legacy locking designs, and LTS releases shipping with such regressions.

---

### Comment pulse
- Kernel regression responsibility → Andres Freund argues major regressions shouldn’t require apps to adopt a brand‑new, default‑off kernel feature introduced in the same release.
- Userspace spinlocks critique → Commenters say spinlocks without rseq are fragile; Postgres devs note futex-based replacements have portability and performance costs, mitigated somewhat by huge pages.
- Deployment risk → Some claim “nobody sensible runs latest kernels” → counterpoint: 7.0 will back Ubuntu 26.04 LTS and containers inherit the host kernel, so many will.

---

### LLM perspective
- View: This is a classic ABI-stability vs. performance-evolution clash, sharpened by a flagship workload (PostgreSQL) on large ARM servers.
- Impact: Cloud providers, distro maintainers, and DB teams must coordinate kernel configuration, preemption mode, and locking primitives more tightly.
- Watch next: Whether Linux 7.0 reintroduces PREEMPT_NONE options, Postgres adopts rseq, and other high-core-count workloads report similar regressions.
