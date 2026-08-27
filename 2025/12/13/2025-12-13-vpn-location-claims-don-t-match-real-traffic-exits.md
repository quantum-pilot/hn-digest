# VPN location claims don't match real traffic exits

- Score: 197 | [HN](https://news.ycombinator.com/item?id=46257339) | Link: https://ipinfo.io/blog/vpn-location-mismatch-report

### TL;DR

IPinfo says active latency and routing measurements of roughly 150,000 exit IPs across 20 VPNs found country mismatches for 17 providers and 38 claimed countries with no measured local exit. Mullvad, IVPN, and Windscribe matched every tested announced location. The vendor argues virtual servers can be sensible but require explicit disclosure because physical jurisdiction matters. A competing geolocation operator challenged the framing, saying many providers label virtual locations and customers may want intended location rather than server location.

### Comment pulse

- Physical exit location matters for government access and jurisdiction-sensitive use → residential endpoints remain scarce, costly, or questionable.
- Mullvad, IVPN, and Windscribe earned trust → counterpoint: this study tests location marketing, not overall privacy or security.
- Latency triangulation invites evasion questions → added delay may confuse measurement, though multi-region comparisons preserve relative proximity signals.

### LLM perspective

- View: “Location” conflates physical infrastructure, assigned IP identity, user intent, and content-unblocking behavior.
- Impact: Compliance and risk systems need separate fields for claimed, registered, and measured geography.
- Watch next: Seek independent replication, provider disclosures, protocol coverage, and repeated measurements as exit fleets change.
