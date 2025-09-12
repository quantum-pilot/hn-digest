# What is the origin of the private network address 192.168.*.*? (2009)

- Score: 262 | [HN](https://news.ycombinator.com/item?id=45156826) | Link: https://lists.ding.net/othersite/isoc-internet-history/2009/oct/msg00000.html

- TL;DR
  - Authoritative answer: 192.168/16 was chosen for RFC1597/1918 because it was the lowest unallocated /16 in 192/8, providing a Class C-sized private range for classful equipment. 10/8 reused the decommissioned ARPANET “net 10”; 172.16/12 was the lowest unallocated Class B /12. The oft-repeated story that vendor documentation made 192.168 ubiquitous is anecdotal, not causal. Discussion recalls widespread pre-standard address squatting (e.g., Sun examples), IPX-era networks, and debates like RFC1627 about whether private addressing/NAT improved or harmed the Internet.

- Comment pulse
  - RFC1918 co-author: ranges chosen to fit classful gear; 10/8 ARPANET reuse, 172.16/12 lowest Class B /12, 192.168/16 lowest Class C /16.
  - Pre-RFC practice: many copied Sun/HP example subnets; standardizing private space avoided random squatting — counterpoint: RFC1627 argued private addressing/NAT would harm the Internet’s architecture.
  - Era context: NetWare IPX reduced IPv4 use; some enterprises used Class Bs internally; Windows pushed RFC1918 on endpoints; ISPs saw 192.168 vs 198.162 confusion.

- LLM perspective
  - View: The choice was administrative minimalism, not folklore; it balanced backward-compatible classes while reserving low-friction, easy-to-filter blocks.
  - Impact: Enabled NAT-centric growth through IPv4 exhaustion and consumer routers; entrenched private-by-default home LAN designs and RFC1918 filtering norms.
  - Watch next: Track IPv6 ULA usage, CGNAT persistence, and BCP revisions around RFC1918 leaks, bogon filtering, and mixed IPv4/IPv6 enterprise design.
