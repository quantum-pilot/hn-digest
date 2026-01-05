# FreeBSD Home NAS, part 3: WireGuard VPN, routing, and Linux peers

- Score: 137 | [HN](https://news.ycombinator.com/item?id=46487120) | Link: https://rtfm.co.ua/en/freebsd-home-nas-part-3-wireguard-vpn-linux-peer-and-routing/

### TL;DR
- The author is building a home FreeBSD 14.3 NAS and in this part wires up secure connectivity between an “office” LAN (192.168.0.0/24) and a home LAN (192.168.100.0/24) using WireGuard instead of OpenVPN.  
- They install WireGuard on FreeBSD, enable IP forwarding, and craft PF rules so VPN clients (10.8.0.0/24) can reach both LANs.  
- An Arch Linux laptop acts as a WireGuard peer via DDNS and router port‑forwarding, then static routes and extra PF rules allow full cross‑LAN SSH and ping between both laptops through the NAS.

---

### Comment pulse
- Vanity public keys for fun → `wireguard-vanity-key` brute‑forces keys with a chosen prefix for more recognizable WireGuard identities.  
- OpenVPN still competitive → DCO kernel mode plus AES‑NI can outperform WireGuard and handles DDNS changes and multi‑WAN more gracefully.  
- OpenVPN for hostile networks → running it on 443 behind `sslh` lets VPN traffic blend with HTTPS in locked‑down environments—counterpoint: WireGuard can also be obfuscated but needs tooling.

---

### LLM perspective
- View: Turn this walkthrough into Ansible or shell scripts so recreating or restoring the setup becomes one command.  
- Impact: Homelabbers gain a reproducible, auditable site‑to‑site VPN bridging Linux and FreeBSD with explicit routing and firewall controls.  
- Watch next: Add IPv6, revoke/rotate WireGuard keys automatically, and integrate metrics/logging for PF and WireGuard into Prometheus/Grafana.
