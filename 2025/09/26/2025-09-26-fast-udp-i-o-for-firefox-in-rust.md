# Fast UDP I/O for Firefox in Rust

- Score: 301 | [HN](https://news.ycombinator.com/item?id=45387462) | Link: https://max-inden.de/post/fast-udp-io-in-firefox/

- TL;DR
    - Firefox rewrote its QUIC UDP I/O in Rust atop quinn-udp, adopting modern per-OS syscalls (sendmmsg/recvmmsg, GSO/GRO, WSASendMsg/RecvMsg). Linux gets full GSO/GRO; Windows USO/URO is disabled due to ARM64/WSL bugs, packet loss, and a driver crash; macOS lacks UDP offload; Android needed legacy syscall/ECN workarounds. Results: CPU‑bound throughput improved from <1 to 4 Gbit/s and ECN is now widely enabled. HN praised the data, while skeptics argue 4 Gbit/s is low and limited by crypto, small PDUs, buffers, and missing QUIC offload; funding questions surfaced.

- Comment pulse
    - Solid engineering win → 4 Gbit/s with data and flamegraphs; meaningful CPU/power gains on laptops.
    - 4 Gbit/s is underwhelming → overheads outside UDP path: small-PDU crypto costs, tiny UDP buffers, route binding, no QUIC NIC offload — counterpoint: unspecified CPU and QUIC complexity matter.
    - Open issues → Cloudflare-hosted sites still problematic; queries about sponsoring Quinn raised governance/compensation critiques.

- LLM perspective
    - View: Pragmatic Rust refactor with quinn-udp, shipping cautiously by disabling fragile offloads per platform.
    - Impact: Lower CPU for HTTP/3, ECN adoption; pressure on OS/NIC vendors to stabilize USO/URO and batch APIs.
    - Watch next: Windows offload fixes, formal macOS batch API, QUIC offload/uring pilots, telemetry on ECN/throughput and driver regressions.
