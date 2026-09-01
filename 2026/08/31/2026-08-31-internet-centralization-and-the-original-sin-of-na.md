# Internet centralization and the original sin of NAT

- Score: 213 | [HN](https://news.ycombinator.com/item?id=49504905) | Link: https://dreamstation.systems/personal/ntppost.html

### TL;DR

The author argues NAT, introduced to stretch scarce IPv4 addresses, broke the Internet's simple end-to-end model: outbound connections work, but unsolicited inbound traffic lacks a destination mapping. Port forwarding, UPnP, STUN, TURN, and ICE partially compensate, while CGNAT can remove user control entirely. This friction normalized cloud-mediated client-server products and made self-hosting harder; incomplete IPv6 adoption has not reversed it. Commenters agreed CGNAT restricts users but disputed NAT as the primary cause, citing usability, smartphones, reliability, security, and hosting overhead.

### Comment pulse

- NAT made ordinary devices poor public endpoints → relays and centralized services became the easiest reliable default.
- Managed services solve availability, backups, updates, and abuse → direct reachability alone would not make self-hosting mainstream.
- NAT is not a firewall → stateful filtering can protect globally addressed devices without rewriting addresses.

### LLM perspective

- View: NAT did not create centralization alone, but it made peer-to-peer design structurally and culturally more expensive.
- Impact: Users surrender control and portability when residential connectivity requires third-party rendezvous or relay infrastructure.
- Watch next: Track residential IPv6, inbound-firewall defaults, CGNAT opt-outs, peer-to-peer success rates, and router usability.
