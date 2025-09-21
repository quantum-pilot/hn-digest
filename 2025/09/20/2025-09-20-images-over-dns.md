# Images over DNS

- Score: 152 | [HN](https://news.ycombinator.com/item?id=45312515) | Link: https://dgl.cx/2025/09/images-over-dns

- TL;DR
  The post shows you can serve binary images via DNS TXT records far beyond 255 bytes: the cap is the DNS message size (≈1.2 KB over UDP; up to 64 KB over TCP). A demo uses Google Public DNS’s JSON API, packing raw binary into a single long TXT to avoid base64 overhead and caching reordering. HN discusses CDN-like resolver caching, security/exfiltration risks and enterprise defenses, and abuse/economics when DNS is “free,” plus protocol caveats around multi-record responses and 64 KB per-message limits.

- Comment pulse
  - Free DNS egress invites abuse → customers tunnel payloads to dodge transfer fees, creating DoS-like load on shared resolvers — counterpoint: meter/limit excessive DNS queries.
  - TXT as CDN works, but chunking is brittle → resolver caching and reordering can scramble multi-record content; single very long records avoid ordering issues.
  - DNS is a covert channel → port 53 often open; orgs lock to internal resolvers, NGFWs detect tunneling, yet captive portals and mobile still leak.

- LLM perspective
  - View: Clever demo but fragile; resolvers, DoH/DoT gateways, and JSON parsing constraints limit practicality for production delivery.
  - Impact: Expect resolver rate limits on large TCP TXT and DNS egress billing; tighter enterprise controls on DoH/DoT and IP-cert access.
  - Watch next: Measure cache amplification, record reordering across resolvers, and whether browsers curb JSON DoH for oversized TXT payloads.
