# Stop Using JWTs

- Score: 212 | [HN](https://news.ycombinator.com/item?id=48558147) | Link: https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452

### TL;DR

The gist argues against JWTs specifically as browser login sessions: long-lived self-contained tokens are hard to revoke, secure deployments regain server-side state, and opaque session IDs in Secure, HttpOnly cookies are simpler and more flexible. It recommends PASETO for short-lived signed tokens and warns against storing credentials in localStorage. HN largely accepted the session critique but rejected the blanket title, citing short-lived, audience-bound, asymmetrically signed JWTs for SSO and service-to-service authorization. Debate centered on whether revocation lists preserve efficiency or merely reinvent session lookups.

### Comment pulse

- Revocation erodes statelessness → if every request checks nonce or user state, an indexed session lookup often offers equivalent cost with simpler semantics.
- Bounded revocation can still scale → expired tokens leave the denylist, so its dataset may remain far smaller than all active sessions.
- Implementation quality matters → modern libraries fixed many algorithm-confusion defaults — counterpoint: JOSE’s broad surface still makes secure configuration harder.

### LLM perspective

- **View:** Token format is secondary; lifecycle design—issuance, storage, scope, rotation, revocation, and expiry—determines authentication safety.
- **Impact:** Monoliths usually gain little from self-contained sessions; distributed services may gain verifiable delegation without central checks.
- **Watch next:** Audit token audiences, accepted algorithms, browser storage, maximum lifetimes, logout guarantees, signing-key rotation, and library defaults.
