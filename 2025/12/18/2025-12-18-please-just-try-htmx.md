# Please just try HTMX

- Score: 416 | [HN](https://news.ycombinator.com/item?id=46312973) | Link: http://pleasejusttryhtmx.com/

### TL;DR

The author presents HTMX as a middle path between full-page HTML and JavaScript-heavy frameworks: HTML attributes issue requests, servers return fragments, and the library swaps them into the page. A cited React-to-Django migration reports much less code, fewer dependencies, faster builds, and faster loads, but involved a content-focused application. The pitch explicitly excludes collaborative editors, offline-first software, heavy computation, and genuinely complex client state. Commenters supplied both successful production examples and reports of fragment orchestration becoming difficult at scale.

### Comment pulse

- HTMX’s creator urged a calmer, tradeoff-driven assessment and also recommended the competing hypermedia library Unpoly.
- Critics wanted credible boundary cases, extensibility guidance, and measurements of server processing and bandwidth costs.
- One startup plans to replace HTMX with React; others said single-purpose endpoints avoid the reported complexity.

### LLM perspective

- View: HTMX is compelling when server-rendered fragments match the domain, not as a universal React replacement.
- Impact: Teams can reduce frontend machinery, but may shift complexity into endpoint design, rendering, and partial-update coordination.
- Watch next: Evaluate one representative workflow, including errors and multi-region updates, before committing an entire application.
