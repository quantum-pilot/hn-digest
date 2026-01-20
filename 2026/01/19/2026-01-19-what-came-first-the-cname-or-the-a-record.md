# What came first: the CNAME or the A record?

- Score: 246 | [HN](https://news.ycombinator.com/item?id=46681611) | Link: https://blog.cloudflare.com/cname-a-record-order-dns-standards/

### TL;DR

Cloudflare’s 1.1.1.1 resolver briefly broke DNS lookups worldwide after a memory-optimization change altered the order of CNAME and A records in responses. Some widely-used stub resolvers (notably glibc’s getaddrinfo and Cisco switch firmware) implicitly relied on CNAMEs appearing first and in-chain order, treating other responses as failures or even rebooting. RFC 1034’s vague wording on answer ordering left room for Cloudflare’s interpretation, but operational reality didn’t. They reverted, vowed to keep CNAMEs first, and proposed a clarifying IETF spec.

---

### Comment pulse

- RFC 1034 is clear, CNAMEs must preface answers → Cloudflare misread “possibly preface”, under-tested a critical change, and keeps breaking the Internet.  
- Others: ambiguity is real → examples saying answer order is “not significant” justify Cloudflare’s view, showing why post‑1997 normative MUST/SHOULD language matters.  
- Side discussion: DNS implementations routinely bend RFCs (CNAME with TXT, SERVFAIL semantics), causing cache-dependent behavior and hard-to-diagnose outages beyond this specific incident.

---

### LLM perspective

- Ambiguous core protocols plus massive deployment create brittle de-facto requirements; behavior, not text, ultimately defines standards.  
- Resolver and stub authors should assume arbitrary RR ordering, build index-based parsers, and test against diverse real-world servers and clients.  
- Track the ordered-answer IETF draft, glibc resolver updates, and vendor advisories from router/switch makers relying on legacy ordering.
