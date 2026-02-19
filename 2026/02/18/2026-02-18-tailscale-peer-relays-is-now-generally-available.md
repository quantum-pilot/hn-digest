# Tailscale Peer Relays is now generally available

- Score: 296 | [HN](https://news.ycombinator.com/item?id=47063005) | Link: https://tailscale.com/blog/peer-relays-ga

- TL;DR  
  Tailscale Peer Relays are now GA, letting any node in your tailnet act as a high‑throughput UDP relay when direct WireGuard paths fail. GA adds better multi-client throughput, static IP:port endpoints for strict cloud/firewalled networks, and Prometheus/Grafana metrics plus CLI diagnostics. HN discussion praises lower latency for remote desktops and gaming, while debating Tailscale’s partly closed-source clients, business-model durability, and whether FOSS/self-hosted meshes remain preferable despite Tailscale’s ease of use.

- Comment pulse  
  - Freedom/control over VPN stack > raw performance → some distrust Tailscale’s proprietary GUIs and app-store dependency—counterpoint: maintainers note daemons/CLI are open and GUIs-only closed.  
  - Revenue model seen as freemium funnel → generous free tier hooks developers; teams later buy per-user business plans with features like SSH, serve/funnel, support.  
  - Early users report big gains → example: NAT‑ed remote desktop dropped from 16→10 ms and tripled bandwidth using a router as peer relay.

- LLM perspective  
  - View: Peer Relays move Tailscale from simple VPN client to tunable overlay you can co-locate with existing infrastructure and controls.  
  - Impact: Cloud-heavy orgs with nasty NATs gain reliable, low-latency fallback paths without operating bespoke DERP or full mesh VPN infrastructure.  
  - Watch next: independent benchmarks vs DERP, autoscaling peer-relay pools from metrics, and pressure from NetBird/Headscale/Tinc on openness and self-hosting options.
