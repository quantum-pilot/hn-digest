# RipGrep musl binaries occasionally segfault during very-large searches

- Score: 244 | [HN](https://news.ycombinator.com/item?id=49133889) | Link: https://github.com/BurntSushi/ripgrep/issues/3494

### TL;DR

Static musl builds of ripgrep 15.1 and 15.2 intermittently segfaulted during repeated, highly concurrent searches over a 20GiB tree containing 1.8 million files; glibc builds did not reproduce it. The crash surfaced inside musl’s allocator during opendir, but investigation pointed deeper to Linux 7.0 direct page-table reclaim using an out-of-range address for TLB operations. A one-line kernel patch changed addr back to start and generated follow-up commits, although rebooting erased the reporter’s reproduction state before a clean A/B test. HN debated allocator exposure and criticized a verbose AI-assisted analysis.

### Comment pulse

- The libc correlation may be incidental → musl exposes single fresh pages more directly, widening a kernel race that other allocators could also encounter.
- AI aided reproduction but hurt communication → its generated tree was useful — counterpoint: the long analysis apparently missed the exact kernel line.
- Scale revealed a rare state → 24-core concurrency and cached 1.8-million-file traversal stressed page-table behavior that vanished after reboot.

### LLM perspective

- **View:** A crash location identifies the victim, not necessarily the faulty layer; allocator assertions can expose kernel memory-management corruption.
- **Impact:** Users of static musl binaries face rare failures; kernel maintainers gain a focused TLB-reclaim regression candidate.
- **Watch next:** Reproduce across machines, kernels, allocators, and reboots; A/B the patch, rule out hardware, and add a stress test.
