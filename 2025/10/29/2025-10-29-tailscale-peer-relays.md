# Tailscale Peer Relays

- Score: 354 | [HN](https://news.ycombinator.com/item?id=45749017) | Link: https://tailscale.com/blog/peer-relays-beta

### TL;DR

Tailscale introduced peer relays in public beta, letting a tailnet node relay encrypted traffic for peers that cannot connect directly. The client prefers direct paths, then a customer-hosted peer relay, then DERP. One UDP port enables deployment near cloud or private resources, potentially improving throughput while preserving end-to-end WireGuard encryption. Two relays are free, with more tied to paid scaling. Tailscale acknowledges incomplete visibility and debugging tools, and browser clients cannot use the native-UDP path. Performance claims come from Tailscale and early partners.

### Comment pulse

- Readers compared the feature with hub-and-spoke VPNs, self-hosted DERP and Tinc.
- Pricing beyond two relays drew criticism because customers provide the relay infrastructure and bandwidth.

### LLM perspective

- View: Relay placement is a practical middle path when NAT traversal fails but managed relay geography is poor.
- Impact: Organizations gain more predictable paths without surrendering encryption, at the cost of operating another network component.
- Watch next: Production telemetry, forced-path controls, failure diagnosis and pricing will determine operational usefulness.
