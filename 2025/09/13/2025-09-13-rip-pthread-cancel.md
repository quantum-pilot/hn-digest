# RIP pthread_cancel

- Score: 136 | [HN](https://news.ycombinator.com/item?id=45233713) | Link: https://eissing.org/icing/posts/rip_pthread_cancel/

- TL;DR
  - curl 8.16 briefly used pthread_cancel to stop resolver threads stuck in getaddrinfo, but glibc’s resolver can be canceled mid-/etc/gai.conf read, leaking memory. The team reverted and will tolerate occasional long waits or suggest c-ares for nonblocking DNS. HN debates POSIX’s lack of timeouts/async APIs; notes glibc’s getaddrinfo_a (timeouts) isn’t portable; some fault glibc for missing cleanup, others say pthread_cancel is unsafe by design. musl disables cancellation; a kernel-like EINTR-style “return error and unwind” approach is proposed.

- Comment pulse
  - Standard API lacks timeouts → POSIX evolves slowly; timeouts would break Unix symmetry; portable async exists only via nonstandard getaddrinfo_a or third-party resolvers.
  - glibc should clean up on cancel → getaddrinfo could register cleanup handlers; musl avoids leaks by disabling cancellation — counterpoint: cross-library cancel-safety is notoriously hard.
  - pthread_cancel is flawed → it bypasses normal unwinding; a kernel-like EINTR model returning errors would integrate with C error paths and be safer.

- LLM perspective
  - View: curl reverting pthread_cancel is prudent; rely on blocking getaddrinfo or pluggable async resolvers per platform.
  - Impact: Large clients should adopt c-ares/systemd-resolved backends; portability demands abstraction layers for DNS and timeouts.
  - Watch next: Track glibc getaddrinfo cleanup/cancel-safety fixes, wider getaddrinfo_a availability, or a POSIX proposal for timeout/async semantics.
