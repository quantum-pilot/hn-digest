# I switched from Htmx to Datastar

- Score: 293 | [HN](https://news.ycombinator.com/item?id=45536000) | Link: https://everydaysuperpowers.dev/articles/why-i-switched-from-htmx-to-datastar/

### TL;DR

The author switched from HTMX plus AlpineJS to Datastar after struggling to synchronize the two libraries. Datastar combines client-side reactivity with server-directed HTML updates, often reducing front-end attributes and allowing one response to patch multiple components over Server-Sent Events. The author favors keeping authoritative state and update decisions on the server, re-rendering components freely, and reserving web components for local behavior. Commenters counter that the apparent client simplicity moves knowledge to the backend and question its scaling and Pro licensing tradeoffs.

### Comment pulse

- Readers framed the choice as HTML-driven HTMX versus server-driven Datastar, not an unconditional reduction in complexity.
- Several challenged redundant HTMX examples and inaccessible clickable `span` elements used in the comparison.

### LLM perspective

- View: Datastar's real advantage is a unified server-driven model, not merely fewer HTML attributes.
- Impact: It can simplify synchronized interfaces while increasing backend responsibility and round-trip sensitivity.
- Watch next: Teams should test latency, failure recovery, and paid-feature needs against their actual interaction patterns.
