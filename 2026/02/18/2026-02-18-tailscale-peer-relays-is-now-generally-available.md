# Tailscale Peer Relays is now generally available

- Score: 296 | [HN](https://news.ycombinator.com/item?id=47063005) | Link: https://tailscale.com/blog/peer-relays-ga

### TL;DR

Tailscale has made Peer Relays generally available, letting customers run high-throughput UDP relays on any supported Tailscale node when firewalls, NAT, or cloud constraints prevent direct WireGuard paths. The release improves multi-client throughput through better interface selection, reduced lock contention, and multiple UDP sockets. Static IP-and-port advertisements support relays behind load balancers in restrictive clouds, sometimes replacing subnet routers while retaining mesh features. Relay paths now appear in Tailscale ping and expose packet and byte metrics for monitoring; the feature is included on every plan.

### Comment pulse

- Users report lower latency and tripled bandwidth for remote game streaming, while UDP avoids the head-of-line blocking associated with TCP-based DERP.
- Debate centers on control: critics dislike closed-source GUIs — counterpoint: others note open CLI clients and paid plans sustain development.
- Peer Relays simplify self-hosted fallback paths, but they serve trusted tailnets rather than general-public resource sharing.

### LLM perspective

- **View:** Peer Relays turn fallback connectivity into customer-owned capacity, but coordination and client distribution remain separate dependencies.
- **Impact:** Network teams inherit relay sizing, placement, firewall, and monitoring duties in exchange for predictable throughput.
- **Watch next:** Multi-client benchmarks, failover behavior, static-endpoint security, saturation alerts, and Headscale compatibility.
