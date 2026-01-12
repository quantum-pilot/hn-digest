# 2026 is the year of self-hosting

- Score: 140 | [HN](https://news.ycombinator.com/item?id=46580326) | Link: https://fulghum.io/self-hosting

### TL;DR
A home server used to mean endless yak‑shaving; now cheap mini PCs, easy overlay networking (e.g., Tailscale), and CLI LLM agents make it approachable and fun. The author runs passwords, photos, media, automation, and reading apps on a $379 box with containers, a reverse proxy, and lightweight monitoring, delegating most setup and maintenance to Claude Code. HN broadly agrees self‑hosting is more accessible, but debates security models, reliance on closed LLMs, and whether co‑op hosted services might be a better societal fix.

### Comment pulse
- Self‑hosting is empowering but niche → some prefer member‑owned cooperative SaaS to align incentives and avoid personal ops burden.  
- Biggest unlock is networking → Tailscale/overlay VPNs hide services from the internet; others prefer DIY WireGuard or even many well‑hardened open ports — counterpoint: CGNAT makes overlays practical.  
- Internet is a constant attack surface → veterans stress probes, DDoS and email deliverability; recommend 443‑only frontends, VPN‑gated admin, and careful reverse‑proxy setups, with LLMs useful mainly for scripts/debugging.

### LLM perspective
- View: Terminal-native agents make “describe the stack, get a working deployment” realistic for single-user servers.  
- Impact: Prosumer users may peel away from some SaaS (photos, password managers, bookmarking), but not from email or collaboration suites.  
- Watch next: Locally hosted/open agents, better security-aware prompts, and turnkey “LLM + mini PC + overlay VPN” bundles will test how mainstream this becomes.
