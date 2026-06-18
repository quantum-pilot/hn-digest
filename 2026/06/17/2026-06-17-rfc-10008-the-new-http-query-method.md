# RFC 10008: The new HTTP Query Method

- Score: 310 | [HN](https://news.ycombinator.com/item?id=48568502) | Link: https://www.rfc-editor.org/info/rfc10008/

### TL;DR
RFC 10008 defines a new HTTP method, `QUERY`: like `GET`, it is explicitly safe and idempotent, but like `POST` it carries its parameters in the request body. This targets large or complex queries that don’t fit cleanly in a URL, while preserving caching, retries, conditional requests, and content negotiation. Servers can expose “equivalent resources” via `Location`/`Content-Location` so later `GET`s can reuse results. HN discussion focuses on caching semantics, HTML form support, and why not just allow `GET` with a body.

---

### Comment pulse
- QUERY caching feels over-engineered → cache key must include the body, which is unbounded and user-controlled — counterpoint: URLs already allow unbounded queries; caches can hash bodies.  
- HTML forms with `method="query"` could avoid POST resubmit warnings → would better reflect safe/idempotent semantics, though POST–Redirect–GET already mitigates some UX issues.  
- Why not GET with a body? → infrastructure and Fetch APIs often drop/disallow GET bodies; a new verb avoids long-standing interoperability and caching edge cases.

---

### LLM perspective
- View: QUERY is mainly for APIs with complex, read-only filters where URLs become unwieldy or sensitive.  
- Impact: HTTP servers, proxies, and libraries must update method registries, caching logic, and CORS handling to recognize QUERY.  
- Watch next: browser/Fetch and HTML form support, CDN/proxy caching guidance, and framework-level patterns for equivalent-resource URIs.
