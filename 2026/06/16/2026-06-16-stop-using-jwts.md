# Stop Using JWTs

- Score: 212 | [HN](https://news.ycombinator.com/item?id=48558147) | Link: https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452

- TL;DR  
  Author argues JWTs are the wrong tool for keeping users logged in. The spec targets very short‑lived tokens, libraries have had serious pitfalls, and revocation is awkward, so “stateless” browser auth collapses back into stateful complexity. Plain server‑side sessions with HTTP‑only cookies and opaque IDs are simpler and safer. JWT‑style tokens remain useful for short‑lived, one‑time authorization (e.g., SSO hops, internal services) and can be replaced by PASETO. HN comments mostly agree but defend careful JWT use in backends.

- Comment pulse  
  - Critique’s scope: many insist it applies to browser login sessions; they note large providers use JWT successfully for SSO and service‑to‑service auth.  
  - Pro‑JWT: revocation lists plus expiry keep state small; per‑user min_issued_at enables “logout all” cheaply — counterpoint: DB lookups erase any stateless benefit.  
  - Security debate: some demand concrete exploits before calling JWT “untrusted”; others argue standards can be high‑risk even without an AWS‑level break.

- LLM perspective  
  - View: Treat JWT purely as an internal delegation artifact; never expose it directly to browsers or mobile clients.  
  - Impact: Teams can centralize auth in one service and still keep per‑request identity cheap in distributed backends.  
  - Watch next: Library authors adding opinionated, safe defaults for cookie sessions, revocation, and PASETO, reducing temptation to hand‑roll JWT schemes.
