# 200 Milliseconds

- Score: 322 | [HN](https://news.ycombinator.com/item?id=49132992) | Link: https://200ms.thenodebook.com

### TL;DR

An interactive explainer follows a hypothetical checkout from a San Francisco touchpad to a Node.js service and PostgreSQL in Virginia, then back to painted pixels in 211.4 ms. It decomposes browser policy checks, DNS, TCP/TLS handshakes, routing, kernel receive paths, Node’s event loop, durable database writes, and display refresh. Its thesis is that distance and cold-connection setup dominate latency; a reused socket falls near 95 ms. HN admired the presentation but challenged its exact timings, terminology, mobile layout, and conspicuously AI-like prose.

### Comment pulse

- The visual method works → readers liked seeing normally invisible layers advance against one clock, despite dense text and sparse screen use.
- “Exact” timings looked fictional → commenters disputed one-millisecond input handling, six-crossing framing, and a 211.4-ms budget with negligible host overhead.
- Perception depends on context → 200 ms is noticeable, yet can feel fast for purchasing; some products deliberately expose a reassuring delay.

### LLM perspective

- View: The page is strongest as a systems map, not as a reproducible latency trace.
- Impact: Beginners gain vocabulary and causal structure; experts must separate illustrative constants from protocol guarantees.
- Watch next: Corrected timing assumptions, clearer data-color semantics, responsive layout fixes, and measured traces across devices.
