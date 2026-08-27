# Show HN: Why write code if the LLM can just do the thing? (web app experiment)

- Score: 191 | [HN](https://news.ycombinator.com/item?id=45783640) | Link: https://github.com/samrolken/nokode

### TL;DR

nokode tests a web server with no fixed application logic: each request asks an LLM to use SQLite, generate an HTTP response, or update persistent feedback. It produced a usable contact manager with schemas, parameterized queries, forms, validation, JSON APIs, and persistence, but every request took 30–60 seconds, cost up to five cents, forgot prior design choices, and sometimes generated broken SQL. Commenters saw an intriguing intent interface, yet argued that code remains valuable as deterministic, efficient memory rather than merely implementation overhead.

### Comment pulse

- A proposed hybrid would let the model write durable handlers, treating direct inference as a cache miss and code as memory.
- Critics rejected unpredictable interfaces and orders-of-magnitude higher compute costs.
- Supporters valued the experiment as a glimpse of richer adaptive outputs, not a practical replacement for conventional apps.

### LLM perspective

- View: The experiment removes application code only by recomputing behavior, exposing determinism as code's essential compression benefit.
- Impact: Intent-driven prototypes become easier, while production users bear latency, cost, inconsistency, and reliability penalties.
- Watch next: Handler caching, sandboxing, schema safety, deterministic replay, per-request cost, latency, and design-memory retention.
