# GNU Artanis – A fast web application framework for Scheme

- Score: 260 | [HN](https://news.ycombinator.com/item?id=45031673) | Link: https://artanis.dev/index.html

- TL;DR
  - GNU Artanis is a lightweight, Guile/Scheme web framework with its own async server (delimited continuations), JSON/XML, WebSockets, templating, caching, static files, and DB support via guile-dbi (MySQL/SQLite/PostgreSQL). Minimal routes make “hello world” trivial; it’s dual-licensed GPL/LGPL. HN reports successful production use and adequate performance, plus easy escape hatches to Guile’s server. Discussion centers on nicer macro-based routing, unclear CSRF/XSS protections, and why Guile remains niche (tooling, docs, packaging, typing trends). Name nod: “Artanis” is “Sinatra” backwards; site praised.

- Comment pulse
  - Macro-based route bindings improve ergonomics → bind path segments to variables directly; can still parse ':who' in strings — counterpoint: string routes are simpler.
  - Used in production → fast enough and flexible; Guile server makes bypassing the framework easy; security docs unclear (CSRF/XSS unanswered).
  - Guile stays niche → weak tooling, beginner docs, packaging; sparse stdlib and lack of static typing momentum hinder adoption.

- LLM perspective
  - View: Practical, minimal web stack for Guile; good ergonomics, but security primitives and tooling need tightening.
  - Impact: Targets Scheme tinkerers and small production apps; lowers barrier to Guile-based services without deep framework lock-in.
  - Watch next: Clarify CSRF/XSS story, publish load benchmarks, release LSP/debugging aids, and simplify library distribution beyond Guix/tarballs.
