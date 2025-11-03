# URLs are state containers

- Score: 311 | [HN](https://news.ycombinator.com/item?id=45789474) | Link: https://alfy.blog/2025/10/31/your-url-is-your-state.html

- TL;DR
  Article argues URLs are first-class state containers: encode filters, pagination, view modes for shareability, deep links, history, caching. Use paths for hierarchy, queries for options, fragments for client navigation. Implement with URLSearchParams, popstate, pushState vs replaceState, debounced updates; omit defaults. Avoid secrets, transient/huge state, opaque names, and length-limit traps; treat URLs as contracts with versioning. HN agrees on UX gains and back-button sanity, notes history/autocomplete clutter and auth edges, suggests migrations and compact encodings (e.g., rison), and calls for better URL literacy.

- Comment pulse
  - Favor URL state for shareability/back-button → better UX; dev slower; migrate old URLs to avoid breakage — counterpoint: bloats history/autocomplete; consider replaceState or query params.
  - URL becomes contract → requires versioning and stability; avoid leaking internals and sensitive data; auth flows complicate reproducibility.
  - Need compact, consistent encoding → use patterns or libraries (e.g., rison); keep defaults out; don’t base64 huge JSON.

- LLM perspective
  - View: Design URLs as a minimal, stable state schema; synchronize via router; add a decoder/encoder with migrations.
  - Impact: Better shareability, deep links, and tests; increased effort in naming, versioning, and history/back-button QA.
  - Watch next: Define defaults, length limits, and privacy rules; add v= param; evaluate rison/qs; measure URL parse errors and history churn.
