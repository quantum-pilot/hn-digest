# FastCGI: 30 years old and still the better protocol for reverse proxies

- Score: 224 | [HN](https://news.ycombinator.com/item?id=47950510) | Link: https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies

### TL;DR

The article argues that proxy-to-backend HTTP creates avoidable security ambiguity. HTTP/1.1’s self-described framing lets parsers disagree, enabling request smuggling; proxy-added identity or TLS facts also share a header namespace with attacker input. FastCGI instead frames records explicitly and prefixes client headers, structurally separating them from trusted parameters such as `REMOTE_ADDR`. It can serve long-running daemons over TCP or Unix sockets and is supported by major proxies. Tradeoffs include no WebSockets, weak debugging tooling, and occasionally lower throughput.

### Comment pulse

- HTTP appealed because one protocol simplified development, deployment, and routing — counterpoint: specialized interfaces may be easier to constrain and audit.
- Decoded `PATH_INFO` cannot faithfully represent encoded slashes, which matters when applications require exact URL semantics.
- WAS separates control and raw body pipes, promising cancellation and zero-copy operations but lacking FastCGI’s ecosystem support.

### LLM perspective

- Prefer boundary clarity over peak throughput when security-sensitive metadata crosses tiers.
- A staged trial can compare observability, streaming needs, cancellation, and failure handling.
- End-to-end HTTP/2 is an alternative when replacing the backend protocol is impractical.
