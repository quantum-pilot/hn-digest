# A most elegant TCP hole punching algorithm

- Score: 205 | [HN](https://news.ycombinator.com/item?id=47384032) | Link: https://robertsdotpm.github.io/cryptography/tcp_hole_punching.html

### TL;DR

The proposed test harness strips TCP hole punching down to one shared input: the peer’s WAN IP. Both hosts quantize local time into a common bucket, deterministically derive 16 candidate ports, open reusable nonblocking sockets, and repeatedly send SYNs. If several connections succeed, the numerically greater WAN IP elects one by sending a single-byte marker. This avoids signaling infrastructure and makes experiments easy, but works only when clocks align and both NATs preserve source ports; randomized mappings and CG-NAT sharply reduce coverage.

### Comment pulse

- Readers question how often consumer NATs preserve ports — counterpoint: the author explicitly sacrifices coverage for a simple experimental harness.
- pfSense and some carrier setups reportedly randomize ports or even egress IPs, defeating deterministic coordination.
- Several commenters prefer standardized mapping behavior or IPv6 over increasingly elaborate traversal techniques.

### LLM perspective

- **View:** Its elegance is pedagogical: isolate the punching mechanism by deliberately excluding robust discovery and negotiation.
- **Impact:** Useful for controlled tests, but unsuitable as a general peer-to-peer connectivity layer.
- **Watch next:** Publish success rates across home routers, enterprise firewalls, CG-NATs, clock skew, and operating systems.
