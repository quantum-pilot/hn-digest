# What came first: the CNAME or the A record?

- Score: 246 | [HN](https://news.ycombinator.com/item?id=46681611) | Link: https://blog.cloudflare.com/cname-a-record-order-dns-standards/

### TL;DR

Cloudflare says a memory-saving change reversed cached DNS answer order, placing CNAMEs after address records and causing 1.1.1.1 failures on January 8 until rollback. Sequential clients such as glibc ignored early address records; three Cisco switch models reportedly entered reboot loops, while set-based systemd-resolved worked. The postmortem argues RFC 1034 is ambiguous across RRset ordering, answer sections, and CNAME chains, yet adopts CNAME-first ordering permanently and proposes an Internet-Draft. HN largely read the preface wording as a requirement, faulted missing compatibility tests, and invoked Hyrum’s Law.

### Comment pulse

- Specification reading → many see optional CNAME presence but mandatory leading position — counterpoint: other RFC examples imply broader reorderability.
- Operational accountability → critics say a month-long test phase should have covered glibc and gradual rollout before changing established wire behavior.
- Compatibility reality → common server implementations preserved ordering for decades, making an underspecified convention effectively contractual.

### LLM perspective

- View: Protocol ambiguity explains divergence, but widespread dependency makes preserving established order the safer contract.
- Impact: Resolver operators need interoperability tests spanning legacy stubs and embedded devices, not only compliant modern clients.
- Watch next: Track IETF consensus, glibc behavior, Cisco remediation, ordered-chain test vectors, and Cloudflare rollout safeguards.
