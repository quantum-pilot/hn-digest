# Exit IP VPN servers mitigation rollout

- Score: 239 | [HN](https://news.ycombinator.com/item?id=48269580) | Link: https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout

### TL;DR
Mullvad is rolling out a mitigation against an “exit IP fingerprinting between VPN servers” issue and this page just lists which WireGuard exit servers are already fixed. The underlying vulnerability (described in a separate blog post) lets observers distinguish or correlate traffic across VPN infrastructure via IP behavior. HN discussion focuses on how Mullvad Browser and per-site IP rotation mitigate some risks, the danger of browser exploits deanonymizing users, and how VPNs actually source and geo-locate their exit IPs.

---

### Comment pulse
- The page is just a server list → readers want a clearer link to the technical blog; RFC5737 test IP ranges would’ve clarified examples.  
- Browser angle → Mullvad Browser’s proxies and per-site IPs sidestep this WireGuard-specific issue; but a single browser exploit can instantly reveal your real IP.  
- Exit IP sourcing → many VPNs use grey‑market IP providers and fake geolocation; free VPNs/extensions may even route traffic through other users’ connections.

---

### LLM perspective
- View: This tiny rollout page signals a real, infrastructure-level privacy flaw that required protocol and server-side changes, not marketing.  
- Impact: High‑risk users on Mullvad’s WireGuard exits benefit most; Tor-like usage still demands strong browser hardening and machine isolation.  
- Watch next: Independent tests for exit-IP fingerprinting, full server coverage, and browser tooling to verify uniform, non-unique fingerprint profiles.
