# Show HN: Whosthere: A LAN discovery tool with a modern TUI, written in Go

- Score: 188 | [HN](https://news.ycombinator.com/item?id=46731432) | Link: https://github.com/ramonvermeulen/whosthere

### TL;DR
Whosthere is a LAN discovery tool with a keyboard‑driven TUI, written in Go, that finds devices without needing root. It combines mDNS, SSDP, and ARP‑cache–based discovery, enriches results with OUI vendor data, offers optional port scanning, theming, and a daemon mode with an HTTP API. HN discussion compares it to nmap and popular GUI scanners, praising its UX and unprivileged design while requesting better hostname resolution, reverse DNS, interface flags, configurable scan parameters, and potential IDS‑style logging.

---

### Comment pulse
- nmap already does fast, scriptable discovery → critics see feature overlap; others note Whosthere’s TUI, unprivileged focus, and daemon API offer different ergonomics and integration—counterpoint: hostname coverage lags.
- Feedback wishlist → better hostname/reverse DNS resolution, per‑interface CLI flag, configurable scan interval, and logging of new arrivals to act as a minimal IDS.
- Tool landscape framing → users mention Advanced IP Scanner, Angry IP Scanner, and Discovery.app as benchmarks for host/hostname detection, especially on Bonjour‑heavy Apple networks.

---

### LLM perspective
- View: This is nmap‑inspired but optimized for continuous, visual LAN awareness rather than one‑off security scans.
- Impact: Most useful for homelab admins and small offices wanting always‑on, low‑privilege network visibility.
- Watch next: Add Windows support, improve name resolution, expose richer HTTP/JSON for dashboards, and benchmark vs nmap/Advanced IP Scanner on diverse networks.
