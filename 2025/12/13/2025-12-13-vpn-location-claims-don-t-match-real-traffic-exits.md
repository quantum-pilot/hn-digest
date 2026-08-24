# VPN location claims don't match real traffic exits

- Score: 197 | [HN](https://news.ycombinator.com/item?id=46257339) | Link: https://ipinfo.io/blog/vpn-location-mismatch-report

### TL;DR

IPinfo tested 150,000 VPN exits across 20 providers and 137 advertised countries using latency from 1,200-plus probes. Seventeen providers had country mismatches; 38 advertised countries never produced a stable local exit, while IVPN, Mullvad, and Windscribe matched every tested location. Bahamas endpoints landed in the United States and Somalia labels in France or Britain. The company argues virtual locations can improve cost, performance, or safety, but require disclosure. HN questioned measurement gaming, provider transparency, and whether geolocation should represent physical routing or user intent.

### Comment pulse

- Mullvad earned praise, but a commenter separated honest location marketing from broader privacy or censorship resistance.
- Latency spoofing seemed possible through added delay — counterpoint: multipoint sampling still reveals the consistently nearest region unless manipulation is location-aware.
- A competing geolocation operator said many providers disclose virtual endpoints and argued customers sometimes value requested country over physical server location.

### LLM perspective

- View: The study measures routing reality, not complete VPN quality, and its author sells the measurement-based alternative it recommends.
- Impact: Mislabeling can distort safety, compliance, fraud, and access decisions even when regional IP addresses still unblock content.
- Watch next: Independent replication, protocol coverage, disclosure labels, route changes, adversarial latency tests, and provider responses.
