# Show HN: Duck-UI – Browser-Based SQL IDE for DuckDB

- Score: 173 | [HN](https://news.ycombinator.com/item?id=45633453) | Link: https://demo.duckui.com

### TL;DR

Duck-UI is a browser-based SQL IDE for DuckDB that stores profiles locally and claims fully client-side, offline operation without sending data to servers. Commenters compared it with DuckDB's embedded UI: Duck-UI offers custom charts and privacy advantages, while the official interface has convenient automatic column graphs. Early Firefox testing found limits and bugs involving 200-row grids, value inspection, filter focus, menus, resizing, tooltips, and sidebar sizing. Discussion also highlighted DuckDB-WASM's potential for low-latency local analytical applications.

### Comment pulse

- Local execution is the differentiator → browser-side processing can protect data and continue without a hosted backend.
- Built-in UI sets expectations → automatic column summaries and large-result handling are features users already value.
- Detailed testing found polish gaps → the creator accepted nine concrete Firefox issues for review.

### LLM perspective

- View: A local analytical IDE is compelling when it combines privacy with the ergonomics users expect from desktop data tools.
- Impact: Analysts can inspect large local files without upload latency, server provisioning, or external data exposure.
- Watch next: Add virtualized rows, structured-value inspection, accessible chart tooltips, stable filters, and comparative performance tests.
