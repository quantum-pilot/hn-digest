# Django: what’s new in 6.0

- Score: 120 | [HN](https://news.ycombinator.com/item?id=46210240) | Link: https://adamj.eu/tech/2025/12/03/django-whats-new-6.0/

### TL;DR

Django 6.0 adds four headline capabilities: reusable template partials, a standard API for defining and enqueuing background tasks, built-in Content Security Policy middleware with nonce support, and migration to Python’s modern email API. The task framework ships without a production backend, leaving execution to compatible packages. Other improvements refresh database-generated fields after saves, generalize StringAgg across databases, default primary keys to BigAutoField, and expand shell imports and template utilities. Commenters focused on how partials differ from includes and whether task backends should stay specialized.

### Comment pulse

- Template partials keep reusable fragments near their context and support isolated HTMX responses; critics noted React components also encapsulate state.
- Task enthusiasm was tempered by backend experience: commenters preferred narrowly focused runners and debated Celery versus Django-Q2.

### LLM perspective

- View: This release standardizes integration seams more than it replaces mature third-party systems.
- Impact: Package authors gain common contracts for fragments, tasks, and CSP-aware markup across Django projects.
- Watch next: Production task backends, migration friction, CSP adoption, email edge cases, and partials’ effect on HTMX architectures.
