# I switched from Htmx to Datastar

- Score: 293 | [HN](https://news.ycombinator.com/item?id=45536000) | Link: https://everydaysuperpowers.dev/articles/why-i-switched-from-htmx-to-datastar/

- TL;DR
  - An HTMX+Alpine user switched to Datastar to avoid cross-library sync bugs and heavy client attributes. Datastar centralizes update logic on the server, pushes realtime via SSE, and encourages re-rendering components (or whole pages) over client state. HN debates the trade-off: simpler client vs more backend responsibility, “immediate-mode” scalability, accessibility semantics, and Datastar’s open‑core “Pro” model. Demos suggest strong realtime on cheap VPSs; some remain wary of licensing and long‑term direction.

- Comment pulse
  - HTML-driven HTMX vs server-driven Datastar → fewer client attributes, but backend must know targets and state — counterpoint: simpler client can be faster.
  - Immediate-mode re-rendering touted → demos handle realtime on $5 VPS, with adaptive rendering and backpressure; simplicity praised, scalability for complex UIs questioned.
  - Open-core shift worries developers → some see ‘Pro’ features/paywall as bait-and-switch; others argue sustainability, MIT-licensed older versions remain forkable.

- LLM perspective
  - View: Datastar suits backend-owned state and SSE; HTMX suits HTML-locality and thin servers.
  - Impact: Shifts complexity to server teams; favors server templates, SSE infra, and componentized HTML over client frameworks.
  - Watch next: Benchmarks: SSE throughput vs polling; guidance on immediate-mode vs patching; clear OSS/Pro boundaries, migration paths, and accessibility best practices.
