# Privacy and Security Risks in the eSIM Ecosystem [pdf]

- Score: 254 | [HN](https://news.ycombinator.com/item?id=45329127) | Link: https://www.usenix.org/system/files/usenixsecurity25-motallebighomi.pdf

- TL;DR
  - Researchers instrumented travel eSIMs and found: traffic is often home-routed via foreign cores (e.g., China Mobile), shifting jurisdiction and exposing metadata; some profiles silently open data channels or fetch SMS via proactive STK; reseller dashboards can read identifiers, message users, geolocate devices, and even assign static public IPs; and deletion can fail, causing lock-in. HN debates TLS-is-enough vs metadata/latency/geo-blocking risks, and suggests mitigations like VPN/WireGuard or sticking with physical/programmable SIMs.

- Comment pulse
  - Instrumented eSIMs → sysmoEUICC1 + SIMtrace2 expose proactive STK data/SMS otherwise hidden in soldered eUICCs.
  - Foreign home routing seems benign under TLS → critics note metadata, censorship, DNS limits, and geo-blocking still leak/control behavior — counterpoint: most users won't care.
  - Long-haul paths degrade UX → higher latency, wrong geolocation, blocked sites; users mitigate with always-on WireGuard/Tor, but UDP often de-prioritized.

- LLM perspective
  - View: Risks stem from HRR, opaque resellers, and permissive APIs/STK, not eSIM crypto or specs.
  - Impact: Travelers and IoT fleets face jurisdictional exposure, silent profile communications, and unexpected inbound reachability via public IPs.
  - Watch next: Require routing-mode disclosure, SM-DP+ jurisdiction labeling, per-line DNS/VPN controls, reseller certification, private-by-default IPs, and audited profile deletion semantics.
