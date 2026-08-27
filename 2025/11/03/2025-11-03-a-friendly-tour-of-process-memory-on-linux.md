# A friendly tour of process memory on Linux

- Score: 187 | [HN](https://news.ycombinator.com/item?id=45805539) | Link: https://www.0xkato.xyz/linux-process-memory/

### TL;DR

This Linux memory tour connects virtual address spaces to the mechanisms developers encounter in practice: VMAs, page tables, lazy `mmap` allocation, page faults, copy-on-write after `fork`, and protection changes through `mprotect`. It also explains observability through `/proc` interfaces, huge-page tradeoffs, userspace dirty tracking, TLB effects, and Page Table Isolation. The central lesson is that mappings describe permitted address ranges, while physical pages and translations often appear only when accessed; different invalid accesses can consequently produce `SIGSEGV` or `SIGBUS`.

### Comment pulse

- Readers praised the compact explainer and requested more similarly scoped systems articles.
- Discussion split between appreciating virtual memory’s isolation and performance benefits and lamenting its accumulated complexity.

### LLM perspective

- View: The article succeeds by tracing one memory access across abstractions instead of cataloguing isolated kernel features.
- Impact: That model helps developers interpret faults, sharing, resident memory, and misleading allocation measurements.
- Watch next: How huge pages and userspace fault handling change latency under real workloads.
