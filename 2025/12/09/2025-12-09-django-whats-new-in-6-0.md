# Django: what’s new in 6.0

- Score: 120 | [HN](https://news.ycombinator.com/item?id=46210240) | Link: https://adamj.eu/tech/2025/12/03/django-whats-new-6.0/

### TL;DR
Django 6.0 (“mosaic”) focuses on first-class background tasks, safer security defaults, and smoother developer ergonomics. It adds template partials for reusable in-file template fragments, a core Tasks framework with a standard @task API, and built‑in CSP middleware with nonce support. Email delivery now uses Python’s modern email API, with cleaner semantics and keyword-only parameters. ORM, shell, and template niceties (automatic field refresh, universal StringAgg, BigAutoField default, forloop.length, querystring improvements) round out a release aimed at long-term maintainability.

### Comment pulse
- New Tasks framework excites users tired of Celery’s complexity → standard @task API plus pluggable backends; some prefer single‑backend libraries like django‑rq for simplicity.  
- Template partials praised as bringing React‑like reuse to Django templates → better composition and locality—counterpoint: includes already existed and React’s power is stateful components.  
- Some Brits wince at security term “nonce” → discussion on conflicting meanings; others argue professionals should rely on technical context, not regional slang connotations.

### LLM perspective
- View: Django 6.0 mostly standardizes long‑standing community patterns (tasks, CSP, email), reducing reliance on divergent third‑party ecosystems.  
- Impact: Upgrades from 5.x are relatively low‑risk but unlock safer defaults; teams should plan CSP rollout and task‑runner selection deliberately.  
- Watch next: official production task backend, widespread adoption of template partials and CSP nonces, and enforcement of keyword‑only email APIs.
