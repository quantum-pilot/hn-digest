# A story about bypassing air Canada's in-flight network restrictions

- Score: 170 | [HN](https://news.ycombinator.com/item?id=45536325) | Link: https://ramsayleung.github.io/en/post/2025/a_story_about_bypassing_air_canadas_in-flight_network_restrictions/

- TL;DR
  - On an Air Canada flight offering free “texting-only” Wi‑Fi, the author bypassed restrictions by running a TLS proxy on port 53 (DNS) via Xray, exploiting permissive UDP/TCP DNS to arbitrary servers. Traffic proxied through a local SOCKS5 worked; a DNS‑tunnel was outlined as a fallback for stricter inspection. Performance remained poor due to bandwidth limits. HN discussion centers on proper reachability testing, whether throttling makes such bypasses impractical, and the legality/ethics of evading paid tiers.

- Comment pulse
  - Ping failures ≠ IP blocked → ICMP often filtered; verify reachability with the exact protocol (TCP/TLS/SNI) you intend.
  - Likely QoS/throttling on port 53 → DNS passes but bulk data is rate-limited; paid plans also slow.— counterpoint: Starlink-equipped flights reported acceptable speeds.
  - Jurisdiction and ToS uncertainty → international flights complicate applicable law; others suggest MAC spoofing to assume a paid device’s authorization.

- LLM perspective
  - View: DNS egress is a recurring weak point in captive portals; port-based rules fail without content verification.
  - Impact: Airlines will add DNS DPI, rate limits, or DoH/DoT blocks; proxy tools adapt with obfuscation and domain fronting.
  - Watch next: Measure port-53 throughput caps, detect TLS-on-53 fingerprints, and track Starlink deployments’ policy changes and published enforcement logs.
