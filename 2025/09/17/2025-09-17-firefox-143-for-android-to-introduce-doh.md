# Firefox 143 for Android to introduce DoH

- Score: 201 | [HN](https://news.ycombinator.com/item?id=45275444) | Link: https://blog.mozilla.org/en/firefox/dns-android/

- TL;DR
  - Firefox 143 for Android adds opt-in DNS-over-HTTPS. Mozilla says 2025 optimizations with CIRA/Akamai make DoH 61% faster (75th percentile) and within ~1–2 ms of native DNS, enabling privacy without slowdowns. Android users can enable “Increased Protection” now; default-on may follow by region after testing. HN debates browser DoH versus Android’s Private DNS: inconsistent OS support, resolver substitution, and VPN leaks versus concerns about centralization and loss of LAN DNS filtering. Adblocking tangents highlight Firefox extensions, Brave’s efficiency, and router-level Pi-hole/AdGuard.

- Comment pulse
  - Browser-level DoH → Covers older Androids, avoids resolver substitution, offers vetted TRR and hard-fail control — counterpoint: Private DNS exists; duplication feels unnecessary.
  - Centralization vs self-hosted → Big resolvers add contracts and transparency; self-hosted via WireGuard keeps data local but risks unique-DNS fingerprinting across devices.
  - Ad blocking trade-offs → Firefox + uBO on Android, Orion/Brave alternatives; DNS-level Pi-hole/AdGuard save battery but lose per-site filtering when browser uses DoH.

- LLM perspective
  - View: Browser DoH plus TRR and hard-fail meaningfully reduces on-path tampering; default-off respects Android diversity and enterprise/network constraints.
  - Impact: Mobile Firefox gains desktop parity; DNS operators pressured on latency; OS vendors nudged to improve Private DNS controls.
  - Watch next: Benchmarks across regions (p50/p95), DoOH/ODoH rollout, default-on timelines, and a hard-fail UI to prevent silent fallback to system DNS.
