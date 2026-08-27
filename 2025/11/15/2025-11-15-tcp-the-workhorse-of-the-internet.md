# TCP, the workhorse of the internet

- Score: 271 | [HN](https://news.ycombinator.com/item?id=45935503) | Link: https://cefboud.com/posts/tcp-deep-dive-internals/

### TL;DR

The tutorial explains how TCP turns unreliable IP delivery into an ordered, bidirectional byte stream assigned to applications through ports. Receiver windows prevent buffer overflow; congestion control backs off before networks collapse; sequence numbers, cumulative acknowledgments, retransmissions, and checksums recover loss, reordering, duplication, and corruption. C examples build an echo server and minimal HTTP/1.1 service, then inspect headers and socket queues. Commenters add that modern extensions address window and loss limitations, while SCTP and QUIC support multiple independent streams and other tradeoffs.

### Comment pulse

- Congestion-control algorithms are endpoint implementations, not fixed wire-protocol behavior, enabling continued experimentation without redesigning TCP.
- Raw IP protocols can traverse routers, but NAT, firewalls, and middleboxes often constrain unfamiliar traffic.

### LLM perspective

- View: TCP's longevity comes from a stable wire contract paired with adaptable endpoint algorithms.
- Impact: Applications inherit reliable streams, but single-stream ordering and middlebox behavior shape newer transports.
- Watch next: QUIC adoption, congestion-control fairness, bufferbloat mitigation, multipath support, and encrypted transport evolution.
