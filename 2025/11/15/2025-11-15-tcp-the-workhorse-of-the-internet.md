# TCP, the workhorse of the internet

- Score: 271 | [HN](https://news.ycombinator.com/item?id=45935503) | Link: https://cefboud.com/posts/tcp-deep-dive-internals/

- TL;DR
  - Accessible deep dive into why TCP sits above IP: ports, reliability, ordering, flow and congestion control (post‑collapse backoff), and full-duplex streams. Walkthrough C examples (echo, tiny HTTP/1.1), then decode TCP headers, sequence/ack logic, handshake/teardown, windows, and checksums. HN discussion says TCP nailed the abstraction; historic limits fixed by window scaling and SACK, while QUIC/SCTP add multiplexing. Congestion control lives in endpoints, not on-wire. Debates cover TCP security and RSTs, single-connection pipelining (e.g., DNS), and sending raw IP amid NAT/DPI.

- Comment pulse
  - TCP got the abstraction right; early limits (16‑bit window, coarse loss recovery, head‑of‑line) were patched; QUIC/SCTP add multiplexing—counterpoint: disciplined single-connection pipelining suffices for DNS.
  - Congestion control isn’t on the wire; endpoints choose algorithms (Reno, Vegas, CUBIC, BBR) to handle buffers, RTTs, fairness; many courses misteach this.
  - Routers move L3 packets regardless of L4; raw IP works, but NAT/DPI often block; TCP RST injection can kill flows—counterpoint: QUIC’s authenticated transport resists injection.

- LLM perspective
  - View: TCP remains the stable baseline; QUIC pragmatically layers reliability, security, and multiplexing over UDP for most new application protocols.
  - Impact: Developers simplify transport by targeting HTTP/3/QUIC; operators must treat UDP as first‑class; middleboxes that ossified around TCP/HTTP/1.1 become liabilities.
  - Watch next: Real‑world BBRv3 vs CUBIC vs QUIC on high‑BDP paths (5G, Starlink); SCTP/QUIC multistreaming ergonomics; firewall/NAT policies that still penalize UDP.
