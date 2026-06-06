# Mullvad exit IPs are surprisingly identifying

- Score: 559 | [HN](https://news.ycombinator.com/item?id=48143880) | Link: https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/

- TL;DR  
The post discovers that Mullvad’s “random” exit IP per server is actually a deterministic function of your WireGuard key: for each server, you get an IP at essentially the same percentile position within that server’s IP pool. Observing your IPs on multiple Mullvad servers lets an attacker estimate an underlying seed and narrow you to a small fraction of Mullvad users, enabling cross-site / cross-time correlation from logs. Mullvad acknowledges partly unintended behavior and is already testing a mitigation, while users debate realistic VPN threat models.

- Comment pulse  
- Mullvad/partner response → Some behavior intended (stable IPs for UX), some not; patch rolling out; recommend WireGuard key rotation; criticize lack of prior disclosure.  
- Risk interpretation → Finding eases cross-server correlation but doesn’t directly reveal identities; critics say “intel-agency design” is overblown—counterpoint: still a meaningful fingerprinting regression.  
- Threat models → Split between “VPN = privacy, not anonymity; Tor for that” and “commercial VPNs do market quasi-anonymity, so this weakness matters.”

- LLM perspective  
- View: Deterministic mappings from long-lived keys to network properties easily become stealth identifiers; privacy tools must treat “convenient determinism” as suspect.  
- Impact: VPNs, proxy services, and CDNs should audit any per-user randomness (IPs, ports, routes) for cross-context correlation risks.  
- Watch next: Mullvad’s final fix, third-party validation, and whether other VPNs using seeded RNGs show similar fingerprinting patterns.
