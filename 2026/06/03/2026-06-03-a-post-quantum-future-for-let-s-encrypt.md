# A Post-Quantum Future for Let's Encrypt

- Score: 213 | [HN](https://news.ycombinator.com/item?id=48385114) | Link: https://letsencrypt.org/2026/06/03/pq-certs

### TL;DR

Let’s Encrypt plans to make Merkle Tree Certificates its route to post-quantum web authentication, targeting staging in late 2026 and production readiness in 2027. MTCs batch certificates under one post-quantum signature, move signed landmarks outside handshakes, and make transparency intrinsic, keeping common handshakes smaller than today’s PKI. Current certificates do not change; operators should prioritize hybrid X25519MLKEM768 key exchange against harvest-now-decrypt-later attacks. HN welcomed avoiding permanently bloated ML-DSA handshakes but questioned landmark synchronization, stale-client fallbacks, non-browser support, and whether quantum risk is truly near-term.

### Comment pulse

- Migration tradeoff → MTCs remove legacy PKI cruft but also discard battle-tested tooling, making ecosystem integration a substantial engineering project.
- Distribution risk → Browsers can obtain landmarks from vendors; curl-like clients lack an obvious trusted distributor and may rely on larger standalone certificates.
- Urgency → Hybrid migration offers cheap insurance against harvest-now-decrypt-later risk — counterpoint: skeptics expect cryptographically relevant quantum computers to remain distant.

### LLM perspective

- **View:** MTCs trade byte-heavy stateless verification for smaller handshakes backed by continuously distributed, authenticated state.
- **Impact:** ACME-client maintainers must absorb protocol changes spanning issuance, revocation, transparency, and certificate selection before administrators see benefits.
- **Watch next:** PLANTS standardization, ACME drafts, root-program requirements, revocation design, fallback frequency, and whether production remains on track for 2027.
