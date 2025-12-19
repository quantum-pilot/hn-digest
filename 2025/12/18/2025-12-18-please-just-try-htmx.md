# Please just try HTMX

- Score: 416 | [HN](https://news.ycombinator.com/item?id=46312973) | Link: http://pleasejusttryhtmx.com/

### TL;DR
The article argues that most web apps sit between plain HTML and full SPA complexity, and that htmx is a pragmatic “middle path”: HTML attributes trigger HTTP requests, servers return HTML fragments, and htmx swaps them into the DOM—often eliminating custom JavaScript and heavy build pipelines. A real-world React-to-htmx rewrite reportedly cut code, dependencies, and load times dramatically. The author stresses htmx isn’t for Google-Docs-level apps, but is extremely effective for CRUD-style, form-and-table SaaS and internal tools.

---

### Comment pulse
- HTMX creator: prefers nuanced, non-hyperbolic framing; htmx shines when enhancing traditional server-rendered apps, but requires good backend patterns and partial rendering discipline.  
- Scaling/complexity concerns: more server work, multiple HTML fragments per endpoint, immature best practices, weaker LLM support—counterpoint: simple, single-purpose endpoints and optimistic UI keep htmx architectures manageable.  
- Architecture divide: some love strict JSON API + SPA separation and reject SSR; others report productive Python/Rails + htmx stacks and point to real, non-trivial apps.

---

### LLM perspective
- View: HTMX reframes “frontend” as hypermedia composition, which reduces complexity for CRUD apps but clashes with SPA-first habits and tooling.  
- Impact: Strong option for small teams, intranets, and Rails/Django-style shops that feel over-served by React-class frameworks.  
- Watch next: Better htmx docs, patterns, and examples at scale; benchmarks on server/bandwidth cost; integrations with mainstream frameworks and AI tooling.
