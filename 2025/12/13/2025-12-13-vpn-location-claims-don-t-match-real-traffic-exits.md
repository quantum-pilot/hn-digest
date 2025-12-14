# VPN location claims don't match real traffic exits

- Score: 197 | [HN](https://news.ycombinator.com/item?id=46257339) | Link: https://ipinfo.io/blog/vpn-location-mismatch-report

TL;DR  
In tests of 150k exit IPs from 20 major VPNs, IPinfo found 17 providers routinely route traffic from different countries than advertised, especially “exotic” locations like Bahamas or Somalia, which often exit in US or Western Europe. Only three smaller providers fully matched their marketing. Article argues virtual locations can be technically reasonable but become deceptive without clear labelling, and legacy IP databases often repeat these fictions. HN discussion centers on trustworthy VPNs, RTT-based detection limits, and growing VPN blocking.

Comment pulse  
- Many users need country IPs for bureaucracy and media → residential-style access beats commercial VPNs; workarounds include Tailscale on a friend’s network or roaming SIMs.  
- Mullvad, Windscribe, IVPN seen as rare honest players → consistently match locations and work behind censorship like China, unlike big “streaming” VPN brands.  
- Probe latency triangulation can uncover real exits → adding uniform delay or faking routes might evade it—counterpoint: multiple global probes still reveal relative proximity patterns.

LLM perspective  
- View: VPNs should expose “virtual vs physical” per location; IP databases should tag both claimed country and measured exit separately.  
- Impact: Mislocated VPN exits mislead fraud systems, regulators and at-risk users who assume, e.g., “Somalia” implies local jurisdiction and surveillance.  
- Watch next: Independent replications of latency-based mapping, plus pressure from browsers and app stores for standardized VPN transparency labels.
