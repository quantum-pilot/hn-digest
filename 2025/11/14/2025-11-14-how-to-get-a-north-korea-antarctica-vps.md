# How to Get a North Korea / Antarctica VPS

- Score: 198 | [HN](https://news.ycombinator.com/item?id=45922850) | Link: https://blog.lyc8503.net/en/post/asn-5-worldwide-servers/

### TL;DR

The author demonstrates that an IP address's database location can diverge from its physical server. They subdivided and announced an IPv6 block, changed registry country metadata, submitted correction requests, and waited for MaxMind and Cloudflare to classify it as North Korean. Cloudflare WARP then issued IPv4 addresses carrying that classification more consistently across services. The method exploits ambiguous geolocation rather than hosting in North Korea or Antarctica. Commenters and IPinfo staff explained how active ping, traceroute, routing, and other evidence can counter adversarial submissions.

### Comment pulse

- IP location is inferred, not intrinsic → registries, routing, operator claims, latency, and commercial databases can conflict.
- Active measurements resist spoofing → geographically distributed probes compare ping and traceroute paths, though coverage gaps force weaker fallbacks.
- Correction systems enable both maintenance and manipulation → operator-provided metadata is useful but not proof of physical presence.

### LLM perspective

- View: The experiment exposes geolocation as a negotiated confidence estimate mistakenly treated as a fact.
- Impact: Streaming controls, fraud scoring, discourse labels, and regional policy can misclassify users when databases accept adversarial metadata.
- Watch next: Compare providers' validation, correction safeguards, uncertainty reporting, and recovery after conflicting active measurements.
