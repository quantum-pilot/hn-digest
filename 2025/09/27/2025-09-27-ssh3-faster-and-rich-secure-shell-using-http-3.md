# SSH3: Faster and rich secure shell using HTTP/3

- Score: 307 | [HN](https://news.ycombinator.com/item?id=45395991) | Link: https://github.com/francoismichel/ssh3

### TL;DR

SSH3 is an experimental remote-terminal protocol running SSH's connection layer over HTTP/3 and QUIC. It claims three round trips to establish a session versus five to seven for SSHv2, while active keystroke latency remains unchanged. Features include UDP forwarding, X.509 server certificates, OpenID Connect authentication, agent forwarding, proxy jumps, and secret URL paths that reduce discovery but do not replace authentication. Its maintainers explicitly advise against production deployment pending security review and expect to rename it “Remote Terminals over HTTP/3.”

### Comment pulse

- Readers saw reduced setup latency, UDP tunnels, and avoiding multiplexed head-of-line blocking as the strongest potential benefits.
- Others prefer battle-tested SSH and dislike more application protocols moving onto HTTP, though firewall traversal motivates that trend.

### LLM perspective

- View: QUIC adds credible transport capabilities, but the SSH3 name overstates continuity and maturity.
- Impact: Remote-access users may gain faster setup and UDP forwarding only after accepting new infrastructure and trust assumptions.
- Watch next: Independent cryptographic review, protocol standardization, production hardening, interoperability, and latency benchmarks.
