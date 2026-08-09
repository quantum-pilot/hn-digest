# AWS engineer reports PostgreSQL perf halved by Linux 7.0, fix may not be easy

- Score: 389 | [HN](https://news.ycombinator.com/item?id=47644864) | Link: https://www.phoronix.com/news/Linux-7.0-AWS-PostgreSQL-Drop

### TL;DR

PostgreSQL throughput on a 96-core Graviton4 system fell to roughly 51% under a near-final Linux 7.0 kernel, with profiles showing far more userspace spinlock time. An AWS engineer bisected the regression to scheduler changes removing the old PREEMPT_NONE behavior and proposed restoring it as default. Kernel maintainers instead pointed PostgreSQL toward Linux 7.0’s new, opt-in RSEQ time-slice extension. Commenters stressed the regression was architecture- and workload-dependent, absent in one 96-core AMD test, and potentially obscured by huge pages.

### Comment pulse

- PostgreSQL developers call same-release opt-in remediation unacceptable → kernel maintainers prefer userspace adaptation over restoring removed scheduling behavior.
- With huge pages, contention became unmeasurable → the 100GB, 4KB-page setup may overstate typical production exposure.
- Containers cannot select host preemption semantics → distro defaults could propagate the regression across many tenants.

### LLM perspective

- **View:** A 49% regression in a flagship database warrants compatibility-first handling even if the replacement mechanism is technically cleaner.
- **Impact:** Ubuntu 26.04 operators on high-core ARM could inherit severe throughput loss without kernel or PostgreSQL changes.
- **Watch next:** Final Linux 7.0 decision, cross-architecture benchmarks, RSEQ enablement, huge-page results, and distro backports.
