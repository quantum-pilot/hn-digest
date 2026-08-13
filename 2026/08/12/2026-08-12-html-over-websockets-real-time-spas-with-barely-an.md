# HTML over WebSockets: real-time SPAs with barely any JavaScript

- Score: 201 | [HN](https://news.ycombinator.com/item?id=49275335) | Link: https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/

### TL;DR

The proposal builds real-time applications by rendering HTML on the server and sending fragments and events through a WebSocket, leaving only minimal client JavaScript to place updates. Compared with client-heavy SPAs, it promises one rendering language, no separate API or duplicated state, straightforward broadcasts, and indexable initial HTML. Costs include per-client server state, harder horizontal scaling, reconnect and offline complexity, and sensitivity to latency. The author recommends WebSockets for truly bidirectional products, SSE for push-only interfaces, and HTTP for ordinary request-response work; commenters favored that use-case distinction.

### Comment pulse

- Critics said SSE plus fetch covers most applications with simpler semantics, while others noted SSE connection limits and browser quirks.
- Readers connected the pattern to LiveView and Blazor, stressing that perceived responsiveness depends more on network distance than transport novelty.

### LLM perspective

- View: WebSockets do not remove complexity; they relocate state to the server and can simplify products with genuinely bidirectional interaction.
- Impact: Small teams may ship realtime interfaces with less client code, trading browser complexity for connection management and server-side scaling.
- Watch next: Benchmark WebSockets against SSE and HTTP under realistic latency, reconnection, multi-tab, broadcast, and horizontal-scaling loads.
