# I’ve banned query strings

- Score: 235 | [HN](https://news.ycombinator.com/item?id=48076173) | Link: https://chrismorgan.info/no-query-strings

### TL;DR
The author dislikes third parties appending tracking parameters (e.g., `?ref=…`, `utm_*`) to his URLs, seeing it as user-hostile and a violation of his address space. Since his site doesn’t use query strings, he now blanket‑rejects any request that includes them, returning 414 “URI Too Long” as a deliberate, slightly comic protest. He muses about weird URLs like `/?` and hits Caddy edge cases. HN discusses URL standards, status codes, tracking, privacy, and legitimate uses of query parameters.

---

### Comment pulse
- Query strings are part of the URL, not a side channel → specs allow 404/other errors for unexpected params; older PHP/CGI sites even routed entirely via queries.  
- Tracking/query params in shared links harm privacy and UX → bypass Referer controls, leak tokens, bloat copied URLs — counterpoint: servers could silently ignore or strip them instead.  
- Error semantics debated → 400, 403, 414, even 418 all arguably valid; highlights that HTTP lacks clear guidance for “bad or unwanted query parameters.”

---

### LLM perspective
- View: Treating query strings as strictly as paths is spec‑correct but intentionally hostile; it’s a protest, not a general best practice.  
- Impact: Personal sites can signal anti‑tracking values; large services must still support queries for search, filters, pagination, and APIs.  
- Watch next: Better browser tools for stripping tracker params, standard conventions for ignorable parameters, and serverside middlewares that sanitize inbound/outbound URLs.
