# What I love about Django

- Score: 131 | [HN](https://news.ycombinator.com/item?id=49193673) | Link: https://buttondown.com/blog/what-i-love-about-django

### TL;DR

Buttondown’s founder credits Django’s durable leverage to nearly invisible abstractions: request/response middleware, lightly inherited models, and stable migrations. Buttondown adds UUIDs, typed public IDs, validation, change hooks, provenance, and soft deletion through an abstract base model; it isolates behaviors into action modules, standardizes function-based views, and tests real rows with pytest. The team avoids signals, class-based views, modular apps, admin, forms, and server-rendered frontends, instead hydrating Vue from Django-seeded data. HN praised stability but warned that Active Record queries, lazy loading, and cross-app traversal invite hidden coupling and N+1 failures.

### Comment pulse

- Django’s slow, compatible evolution lets decade-old applications upgrade without rewrites, a benefit users notice mainly after switching frameworks.
- ORM critics prefer service or selector layers because model access everywhere enables exploding joins, N+1 queries, and brittle string-based cross-boundary references.
- Flexibility drew praise — counterpoint: Rails users argued comparable substitutions exist and excessive customization can itself destroy framework coherence.

### LLM perspective

- View: Django’s value is optional structure: teams can retain boring defaults while replacing pieces only after concrete pressure emerges.
- Impact: Long-lived products spend fewer innovation tokens, but architecture discipline must constrain ORM convenience before implicit queries spread.
- Watch next: Compare upgrade cost, query regressions, test speed, service-layer boundaries, single-file ergonomics, and ORM use outside full Django applications.
