# Images over DNS

- Score: 152 | [HN](https://news.ycombinator.com/item?id=45312515) | Link: https://dgl.cx/2025/09/images-over-dns

### TL;DR

A demonstration serves AVIF images inside DNS TXT records, exploiting the fact that the 255-byte limit applies to each character-string, not the whole record. UDP payloads are roughly 1,232 bytes, but ordinary DNS-over-TCP framing permits messages near 64KB. A custom Go server returns raw binary, while Google Public DNS’s JSON API enables browser retrieval with special parsing. HN discussion celebrates the hack but emphasizes tunneling, firewall bypass, cache abuse, data exfiltration, and denial-of-service risks.

### Comment pulse

- DNS can become an unpriced transport → one cloud operator recalls customers causing shared operational pain to avoid transfer fees.
- Port 53 is a security boundary → defenders recommend forcing clients through monitored corporate resolvers.
- Larger transfers remain possible → commenters discuss multiple records or TCP messages, though each DNS message stays size-limited.

### LLM perspective

- View: Protocol flexibility creates both delightful demonstrations and channels that network policy may overlook.
- Impact: Operators need behavioral limits and resolver visibility, not assumptions that DNS carries only tiny metadata.
- Watch next: Browser tunneling detections, resolver size limits, TTL enforcement, and IP-certificate-driven bypass techniques.
