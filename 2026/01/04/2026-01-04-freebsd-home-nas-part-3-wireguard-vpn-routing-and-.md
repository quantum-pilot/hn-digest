# FreeBSD Home NAS, part 3: WireGuard VPN, routing, and Linux peers

- Score: 137 | [HN](https://news.ycombinator.com/item?id=46487120) | Link: https://rtfm.co.ua/en/freebsd-home-nas-part-3-wireguard-vpn-linux-peer-and-routing/

### TL;DR

Part three of a FreeBSD 14.3 NAS series connects an office LAN and home Arch Linux laptop through WireGuard without routing general internet traffic. The guide loads FreeBSD’s WireGuard module, enables forwarding, uses Packet Filter’s default-deny rules, creates peer keys and AllowedIPs, forwards UDP through a TP-Link router, and verifies handshakes and SSH. Static routes on the office laptop then make both LANs mutually reachable through the NAS. Commenters compared WireGuard’s small, quiet attack surface with OpenVPN’s stronger DNS, multi-WAN, administration, and DCO support.

### Comment pulse

- Friendly vanity keys aid identification—counterpoint: short prefixes should not become a substitute for authenticated key management.
- OpenVPN advocates valued automatic DNS changes, multiple endpoints, mature administration, and kernel acceleration for larger or unstable deployments.
- WireGuard supporters preferred silent unauthenticated ports, kernel integration, and simplicity for a small homelab with manually managed peers.

### LLM perspective

- View: Most complexity lies in routes and firewall policy, confirming that WireGuard supplies transport rather than full VPN orchestration.
- Impact: The NAS becomes a trusted gateway joining private networks, increasing both convenience and the consequences of configuration mistakes.
- Watch next: Reconcile shown 51820/51830 ports, test restart persistence, restrict peer privileges, and verify return routes after address changes.
