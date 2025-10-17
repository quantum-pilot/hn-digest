# Why I Chose Elixir Phoenix over Rails, Laravel, and Next.js

- Score: 234 | [HN](https://news.ycombinator.com/item?id=45605291) | Link: https://akarshc.com/post/phoenix-for-my-project.html

TL;DR
- The author chose Phoenix LiveView for a single-language monolith with server‑driven UI over WebSockets, background jobs via Oban, and BEAM’s concurrency/fault‑tolerance—avoiding split frontend/backend stacks. Rails/Laravel/Next.js can do similar things but felt slower to assemble solo. HN agrees Phoenix offers excellent DX and real‑time ergonomics; Rails fans counter with Solid Queue/Cable and Hotwire Native. Oban vs Solid Queue and persistent‑socket hosting favor Phoenix for high concurrency, while Rails still excels at rapid CRUD. Some push back on “optimal” framing and Next.js churn.

Comment pulse
- Phoenix DX is cleaner; Livewire lags; Next.js churny → slots, composition, and router changes derail integrations — counterpoint: Livewire 4 is adding slots soon.
- Rails already ships jobs and websockets → Solid Queue and Solid Cable cover background work and real‑time; Hotwire Native enables mobile.
- Operational edge favors Phoenix at scale → Oban ergonomics and BEAM processes simplify concurrency; hosting many persistent sockets easier (e.g., Gigalixir vs Heroku routers).

LLM perspective
- View: Server-driven UI stacks are converging; choice hinges on infra comfort, team size, and real-time load patterns.
- Impact: Monoliths with first-class sockets/jobs reduce cognitive overhead and glue code, especially for solo devs and small teams.
- Watch next: Measure: concurrent connection limits, job retry UX, router stability; track Livewire 4, Hotwire Native roadmaps, Next.js API stabilization.
