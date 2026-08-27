# Django: what’s new in 6.0

- Score: 120 | [HN](https://news.ycombinator.com/item?id=46210240) | Link: https://adamj.eu/tech/2025/12/03/django-whats-new-6.0/

### TL;DR

Django 6.0’s major additions are reusable and independently renderable template partials, a standard API for background tasks, built-in Content Security Policy middleware with per-request nonces, and migration to Python’s modern email API. The task framework deliberately ships without a production backend, leaving execution to third-party packages such as django-tasks. Other improvements include refreshed database-generated fields after saves, cross-database `StringAgg`, larger default primary keys, richer shell imports, and template utilities. HN focused mainly on task backends and whether partials materially exceed includes.

### Comment pulse

- Template partials improve locality for htmx responses → counterpoint: includes already enabled reuse, while richer components also encapsulate state.
- A common task-definition API enables package interoperability → production queue and worker behavior remains backend-specific.
- Built-in CSP standardizes nonce-aware integrations → report-only rollout is prudent because strict policies can break existing sites.

### LLM perspective

- View: Version 6.0 standardizes extension points around recurring ecosystem solutions rather than replacing their operational machinery.
- Impact: Packages gain shared contracts for tasks and security while applications retain deployment choices.
- Watch next: Track production task backends, CSP adoption, partial tooling, upgrade regressions, and database-specific ORM behavior.
