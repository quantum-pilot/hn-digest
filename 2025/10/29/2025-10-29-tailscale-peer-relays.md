# Tailscale Peer Relays

- Score: 354 | [HN](https://news.ycombinator.com/item?id=45749017) | Link: https://tailscale.com/blog/peer-relays-beta

- TL;DR
  - Tailscale Peer Relays let any node in your tailnet act as a high‑throughput UDP relay, delivering near‑direct speeds through hard NATs/firewalls. Built into the client with WireGuard end‑to‑end encryption, connections prefer direct paths, then relays, then DERP. Use cases include cloud NAT gateways, single‑port firewall exceptions, and DERP offload. It’s a public beta with two relays free per tailnet. HN debated pricing, outage resilience and headscale, preferring relays over direct, browser support (WebTransport), and comparisons to tinc/WireGuard.

- Comment pulse
  - Peer relays fill hub‑and‑spoke fallback; faster than DERP; why charge beyond two if users host bandwidth — counterpoint: many deployments require opening an internet‑reachable port.
  - Prior art: tinc offered relaying and true mesh; critics cite instability and lack of end‑to‑end encryption without unreleased 1.1; some say WireGuard already covers this.
  - Resilience concerns: if Tailscale control plane hiccups, peers struggled to reconnect; interest in Headscale; request to prefer/force relay when direct paths underperform; browser lacks UDP.

- LLM perspective
  - View: Built-in UDP relays shift Tailscale from reliability-first DERP to performance-first overlays for NAT/firewall-heavy environments.
  - Impact: Ops can standardize on a single UDP pinhole and retire many custom DERPs, reverse proxies, and SSH bastions.
  - Watch next: Controls to prefer specific relays, browser-compatible transports (WebTransport), published throughput/latency benchmarks, and guidance on headscale/control-plane outage modes.
