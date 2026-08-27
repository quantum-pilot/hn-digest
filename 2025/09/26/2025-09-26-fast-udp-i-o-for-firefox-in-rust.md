# Fast UDP I/O for Firefox in Rust

- Score: 301 | [HN](https://news.ycombinator.com/item?id=45387462) | Link: https://max-inden.de/post/fast-udp-io-in-firefox/

### TL;DR

Mozilla replaced Firefox's aging NSPR-based QUIC UDP path with a memory-safe Rust implementation built on quinn-udp. Modern batching and segmentation-offload APIs reduced per-datagram overhead, taking extreme CPU-bound benchmarks from below 1 Gbit/s to 4 Gbit/s and enabling Explicit Congestion Notification. Platform reality constrained deployment: Linux supports GSO and GRO well, undocumented macOS batching was withheld, Windows URO and USO caused failures or loss, and old Android versions required compatibility work. The new stack is rolling out broadly, with some optimizations disabled.

### Comment pulse

- Readers welcomed measured throughput gains and potential CPU or battery savings rather than modernization claims alone.
- Others argued 4 Gbit/s remains low and requested fuller hardware, packet-size, QUIC, encryption, and utilization context.

### LLM perspective

- View: The largest achievement is portable modernization with safe fallbacks, not one headline throughput number.
- Impact: Firefox users gain more efficient HTTP/3 while maintainers inherit fewer legacy APIs and shared Quinn improvements.
- Watch next: Windows driver fixes, real-device power measurements, Cloudflare regressions, ECN rollout, and representative benchmarks.
