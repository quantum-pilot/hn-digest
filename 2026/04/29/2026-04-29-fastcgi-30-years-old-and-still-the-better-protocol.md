# FastCGI: 30 years old and still the better protocol for reverse proxies

- Score: 224 | [HN](https://news.ycombinator.com/item?id=47950510) | Link: https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies

### TL;DR
- FastCGI is presented as a safer, more appropriate wire protocol than HTTP for reverse‑proxy–to–backend communication. HTTP/1.1’s ambiguous framing enables request desync/smuggling, and its header model can’t cleanly distinguish trusted proxy metadata (e.g., client IP) from attacker‑supplied headers. FastCGI fixes both with explicit record framing and structural separation of HTTP headers vs trusted parameters, yet remains easy to adopt via existing servers and Go’s stdlib. Downsides: no WebSockets, weaker tooling, and some unoptimized performance.

### Comment pulse
- HTTP as universal internal protocol won historically → simpler topologies, reuse of tooling, end‑to‑end‑style flexibility; critics say multiplexing gateways violate true end‑to‑end semantics.  
- FastCGI has URL/path quirks → CGI‑derived decoding loses encoded slashes; others propose WAS or custom HTTP streaming schemes to gain better framing and cancellation.  
- Plain CGI remains useful at small scale → easy per‑user extensibility with agents, though env‑based headers enable classics like httpoxy if misimplemented.

### LLM perspective
- View: FastCGI‑style separation could be standardized across newer protocols, giving HTTP/2+/3 backends safer metadata channels without bespoke conventions.  
- Impact: Security‑sensitive platforms, CDNs, and API gateways benefit most; smaller teams gain by reusing existing HTTP handlers with stricter backend wiring.  
- Watch next: Track benchmarks of optimized FastCGI implementations, emerging alternatives like WAS, and whether major frameworks ship first‑class non‑HTTP backend transports.
