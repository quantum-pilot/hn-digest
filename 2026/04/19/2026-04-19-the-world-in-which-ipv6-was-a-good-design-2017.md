# The world in which IPv6 was a good design (2017)

- Score: 206 | [HN](https://news.ycombinator.com/item?id=47821429) | Link: https://apenwarr.ca/log/20170810

### TL;DR
- The article is a narrative history of networking arguing that IPv6’s design only fully makes sense in a hypothetical clean‑slate world. Without Ethernet buses, MACs, broadcasts, ARP, DHCP, and mobile devices, IPv6 could have replaced layer‑2 entirely with simple, hardware‑friendly routing and vast address space. Reality kept all that legacy, plus TCP/UDP’s IP‑bound “4‑tuple,” so mobility relies on huge bridged LANs instead. The author suggests QUIC‑style connection IDs as a path to real mobile IP; HN debates IPv6’s quality and necessity.

### Comment pulse
- IPv6 is a solid design → proposed “better” schemes usually recreate IPv6 features already examined; main practical gripe is long, awkward human-readable addresses.  
- IPv6 critics: vendor-driven 1990s design misses built‑in identity, authentication, and encrypted-by-default transport; they want a new, security- and identity-centric L3 — counterpoint: that’s above IP.  
- Operational pain points: coexistence of SLAAC and DHCPv6 confuses deployments; Android’s DHCPv6 refusal and multicast/ARP quirks complicate supposedly simpler IPv6 LANs.

### LLM perspective
- View: The essay highlights that protocol elegance usually loses to backwards compatibility and incremental hacks in large, heterogeneous infrastructures.  
- Impact: Expect IPv4, IPv6, MACs, bridging, and QUIC-like overlays to coexist indefinitely; operators will keep layering rather than replacing.  
- Watch next: Practical, roaming-friendly QUIC deployments and identity-centric overlays (e.g., WireGuard-style meshes) may gradually sidestep today’s address and mobility limitations.
