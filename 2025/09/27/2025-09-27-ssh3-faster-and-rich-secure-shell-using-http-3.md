# SSH3: Faster and rich secure shell using HTTP/3

- Score: 307 | [HN](https://news.ycombinator.com/item?id=45395991) | Link: https://github.com/francoismichel/ssh3

- TL;DR
  - SSH3 reimagines SSH’s connection protocol over HTTP/3’s Extended CONNECT using QUIC+TLS 1.3. It cuts setup to ~3 RTTs (from 5–7), keeps interactive latency unchanged, and adds UDP port forwarding, X.509 server auth, OAuth2/OpenID Connect logins, and “hidden” URLs to resist scanning. It’s an experimental prototype, not production-ready. HN debates the name, sees benefits from QUIC multiplexing and UDP (especially over VPNs/high latency), and questions the broader trend of “HTTP-everything” versus trusting battle-tested SSH.

- Comment pulse
  - Faster setup, less head‑of‑line blocking via QUIC streams; avoids TCP‑over‑TCP on VPNs/high latency — counterpoint: interactive latency unchanged, setup speed rarely bothers some.
  - Skepticism about replacing battle‑tested SSH; project is experimental. Still, features like UDP forwarding and OAuth/OIDC SSO entice; mosh suggested for better roaming UX.
  - HTTP/3 layering seen as pragmatic to bypass middleboxes and censorship; QUIC is general transport — counterpoint: feels like kludge; not really ‘hypertext’ anymore.

- LLM perspective
  - View: Reuse of QUIC/TLS/HTTP auth is sensible; biggest gains are multiplexing, SSO, and traversal, not raw interactive speed.
  - Impact: If standardized, could simplify enterprise SSH with SSO, reduce port‑scan noise, and make port‑forward‑heavy workflows more resilient on flaky links.
  - Watch next: Independent security audits, interop strategy with OpenSSH, reverse forwarding support, and benchmarks over satellite/VPN; track IETF progress and industry interest.
