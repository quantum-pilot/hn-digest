# RIP pthread_cancel

- Score: 136 | [HN](https://news.ycombinator.com/item?id=45233713) | Link: https://eissing.org/icing/posts/rip_pthread_cancel/

### TL;DR

Curl added `pthread_cancel()` in version 8.16.0 to stop worker threads blocked in `getaddrinfo()`, avoiding either a blocking join or accumulating detached threads. It was quickly removed after cancellation exposed a glibc memory leak: `getaddrinfo()` can allocate address results, then hit a cancellation point while opening `/etc/gai.conf`, abandoning those allocations. Curl will instead tolerate eventual waits, while applications can choose c-ares for nonblocking resolution with different capabilities. The episode illustrates why safe, portable DNS cancellation remains difficult.

### Comment pulse

- Commenters wanted standardized asynchronous resolution or timeouts, while noting portability, NSS integration, and system-policy complications.
- Some blamed missing cleanup in glibc; others argued forced thread cancellation is intrinsically hazardous in C.

### LLM perspective

- View: Cancellation that bypasses ordinary error paths makes correctness depend on every hidden callee’s cleanup discipline.
- Impact: Curl trades bounded responsiveness for predictable memory behavior unless applications select an alternate resolver.
- Watch next: Glibc cleanup changes, portable async DNS APIs, c-ares tradeoffs, and cancellation behavior across libc implementations.
