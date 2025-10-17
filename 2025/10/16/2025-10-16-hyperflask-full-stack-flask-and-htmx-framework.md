# Hyperflask – Full stack Flask and Htmx framework

- Score: 273 | [HN](https://news.ycombinator.com/item?id=45604673) | Link: https://hyperflask.dev/

TL;DR
- Hyperflask is a beta, batteries‑included Flask-based framework that marries server-driven UI with HTMX, file‑based routing, and a component system. It ships with Tailwind/DaisyUI, containerized dev/prod, and utilities for email, background jobs, SSE, i18n, auth, and static or hybrid builds. HN welcomed the Flask+HTMX approach but debated components-as-macros and single-file pages, Flask vs FastAPI for async, HTMX’s suitability for complex client state, the absence of Django-like admin, and the project’s ORM choice and depth of HTMX integration.

Comment pulse
- HTMX forces complex state into URLs → critics say; supporters use sessions/localstorage/backend state; fit depends on scope — counterpoint: hypermedia handles realtime and multiplayer.
- Flask vs FastAPI → some want async and choose FastAPI + Jinja + HTMX; others like simple, single-file pages; components may duplicate Jinja macros.
- Ecosystem gaps → missing Django-like admin; Flask-Admin exists but thin; questions about ORM choice over SQLAlchemy and desire for tighter built‑in HTMX utilities.

LLM perspective
- View: Ambitious consolidation of Flask tooling for server-driven apps; productive defaults, but abstractions and sync-first Flask may constrain advanced cases.
- Impact: Appeals to Python teams avoiding SPAs; best for CRUD dashboards and SaaS MVPs, less for heavy client-state or high-concurrency async.
- Watch next: Clarify ORM decision, admin roadmap, HTMX helpers, and async story; ship multi-zone state examples; publish deployment guides and performance baselines.
