# How to Get a North Korea / Antarctica VPS

- Score: 198 | [HN](https://news.ycombinator.com/item?id=45922850) | Link: https://blog.lyc8503.net/en/post/asn-5-worldwide-servers/

- TL;DR
  - The post shows how to “move” IP geolocation: subdivide an IPv6 allocation, set WHOIS country, submit corrections to MaxMind/IPinfo, then let Cloudflare WARP mint a matching IPv4 that most sites accept. Expect weeks of lag; geofeeds help at scale; block probes to prevent reversion. HN notes active-measurement vendors (ping/traceroute) can still infer real regions; IPinfo explains its ProbeNet-first approach with fallbacks that adversaries exploit. Side notes: Chinese platforms mandate GeoIP display; past “North Korea hosting” stunts echo this.

- Comment pulse
  - Database edits work, but latency/traceroute expose true region; faking Seychelles from Europe via ICMP delay is brittle — counterpoint: blocking probes and geofeeds reduce detection.
  - IPinfo: primary active measurements via ProbeNet (1,200 PoPs) using ping+traceroute; falls back to ASN data for unrouted ranges, enabling occasional spoofed locations.
  - Context: China mandates GeoIP-origin display on platforms, boosting WARP script use; past “TPB hosted in North Korea” headlines show long-running geolocation theater.

- LLM perspective
  - View: This exploits GeoIP’s trust chain and update lag rather than altering physical topology or routing.
  - Impact: Region gating, fraud scoring, and analytics can be gamed; vendors will weight active measurements and provenance signals more.
  - Watch next: IPinfo’s tweaks, stricter geofeed verification, Cloudflare WARP update cadence, and services flagging WARP/Cloudflare ranges.
