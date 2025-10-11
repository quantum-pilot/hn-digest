# Datastar: Lightweight hypermedia framework for building interactive web apps

- Score: 208 | [HN](https://news.ycombinator.com/item?id=45536618) | Link: https://data-star.dev/

- TL;DR
    - Datastar is a 10.75 KiB hypermedia framework pairing server-rendered HTML and SSE to drive reactive UIs via data-* attributes, shifting state to the backend and often avoiding user JS. It touts real-time collaboration and “bring your own backend,” with demos like One Billion Checkboxes. HN debates its paid Pro tier: critics cite hidden upsell, feature gating, and potential lock-in; supporters argue 95% is open, Pro optional, and SSR-first simplicity is the draw.

- Comment pulse
    - Realtime/collab claims → Demos ran on $5 VPS; adaptive rendering and scroll backpressure — counterpoint: backend scalability, not Datastar, mainly explains HN survival.
    - Pro tier criticized → Gates features, perceived vendor lock‑in risk, and no interactive Pro examples to evaluate before purchase.
    - Defense and pragmatics → Most sites won’t need Pro; missing attributes can be replaced with small custom JS; geo-pricing desired but hard; $5 support unrealistic.

- LLM perspective
    - View: Sits between htmx and full SPAs; favors backend orchestration over client frameworks; resembles Phoenix LiveView in philosophy.
    - Impact: Suits SSR-first stacks and strong backends; weaker for offline-first, heavy client computation, or WebSocket-specific patterns.
    - Watch next: Load benchmarks, memory footprint, SSE reconnect behavior; clear Pro feature matrix with demos; community plugins, forks, or governance.
