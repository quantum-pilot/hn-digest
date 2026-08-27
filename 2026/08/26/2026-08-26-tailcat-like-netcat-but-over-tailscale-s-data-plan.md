# Tailcat – Like netcat, but over Tailscale’s data plane

- Score: 462 | [HN](https://news.ycombinator.com/item?id=49452990) | Link: https://github.com/tailscale/tailcat

### TL;DR

Tailcat repackages Tailscale’s open-source data plane as a netcat-like Go library and CLI without accounts, root access, routing changes, DNS configuration, or Tailscale’s control plane. A server shares a token containing its WireGuard key and DERP rendezvous information; peers connect encrypted through DERP, then attempt direct UDP hole punching. It supports byte pipes, port forwarding, SSH, SOCKS, exit nodes, persistent keys, DNS-published tokens, custom relays, and client allowlists. HN compared it with Iroh and welcomed simpler peer-to-peer experimentation.

### Comment pulse

- Trivial encrypted connectivity enables playful applications → a Minecraft transport demo appeared immediately, suggesting broader self-hosted and ad-hoc collaboration uses.
- Tailcat retains Tailscale’s distinctive network machinery → magicsock, DERP rendezvous, NAT traversal, WireGuard, and gVisor netstack replace its centralized coordination.
- Broader IPv6 could remove much of the need → until then, automatic hole punching plus relay fallback makes peer-to-peer usable behind NAT.

### LLM perspective

- View: Tailcat’s contribution is packaging mature traversal machinery into a shareable capability token, not inventing another encrypted transport.
- Impact: Developers can embed temporary peer connectivity without privileged installation or account infrastructure, while assuming key-management and relay responsibilities.
- Watch next: Track wire-format stability, DERP-map changes, abuse controls, browser token lowercasing, performance limits, and adoption beyond demos.
