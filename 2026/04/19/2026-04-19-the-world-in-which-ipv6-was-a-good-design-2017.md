# The world in which IPv6 was a good design (2017)

- Score: 206 | [HN](https://news.ycombinator.com/item?id=47821429) | Link: https://apenwarr.ca/log/20170810

### TL;DR

The essay argues IPv6 looks overcomplicated because its design assumed networking could discard Ethernet-era baggage: buses, MAC addresses, broadcasts, ARP, DHCP, and layer-2 bridging would yield to point-to-point links, routable addresses, multicast, and hardware-friendly headers. Legacy compatibility instead preserved every old layer, so IPv6 added machinery without realizing the intended simplification. Its larger omission was mobility: TCP and UDP identify sessions partly by IP address, breaking connections when devices move. Address-independent session identifiers, as enabled by QUIC-like transports, could solve roaming without requiring IPv6.

### Comment pulse

- Defenders say proposed replacements repeatedly rediscover IPv6 features, often ignoring alternatives its design process already evaluated.
- Critics argue 1990s assumptions underweight modern security, identity, mobility, and operator usability.
- NAT stretched IPv4 enough to obscure urgency — counterpoint: apparent continuity does not eliminate architectural scarcity or complexity.

### LLM perspective

- Migrations cannot fund simplification unless old layers actually retire.
- Separating endpoint identity from location makes sessions resilient across network changes.
- Watch connection migration, encrypted naming, and IPv6-only deployments for reductions in legacy dependencies.
