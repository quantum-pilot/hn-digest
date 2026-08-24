# When internal hostnames are leaked to the clown

- Score: 448 | [HN](https://news.ycombinator.com/item?id=46895972) | Link: https://rachelbythebay.com/w/2026/02/03/badnas/

### TL;DR

A NAS owner assigned an internal hostname beneath a wildcard-certified domain kept only in a laptop hosts file. Public wildcard DNS pointed the zone to a monitoring server, which then observed a GCP machine repeatedly connecting with that private hostname in SNI. The author traced the leak to the NAS browser interface sending client-side stack traces to Sentry, after which a cloud service connected back without requesting content. Commenters ruled out certificate transparency, suspected automated metadata fetching, and warned that internal names are not secrets.

### Comment pulse

- A wildcard certificate would not expose the leaf hostname; the supplied behavior instead implicates browser telemetry carrying the current origin.
- Sentry’s unexplained callback could enable attacker-directed scanning—counterpoint: commenters speculated it may merely fetch metadata such as favicons.
- Mitigations included trusted firmware, outbound DNS blocking, uBlock, a reverse proxy with restrictive CSP, private CAs, and opaque non-sensitive naming.

### LLM perspective

- View: Telemetry exports context; origins, paths, traces, and identifiers can reveal topology even when internal services remain unreachable.
- Impact: Home and enterprise devices can disclose naming conventions or sensitive projects; callback systems may become unwitting network scanners.
- Watch next: Vendor behavior, callback purpose, trace payloads, retention, consent, CSP effectiveness, target validation, and demonstrated scanning reach.
