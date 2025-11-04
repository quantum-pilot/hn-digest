# </> Htmx – The Fetch()ening

- Score: 325 | [HN](https://news.ycombinator.com/item?id=45803358) | Link: https://htmx.org/essays/the-fetchening/

- TL;DR
    - htmx 4.0 overhauls internals around fetch() and async, replacing XMLHttpRequest, stabilizing event ordering, and simplifying extensions. Implicit attribute inheritance becomes explicit via :inherited; history snapshots are dropped for network reloads. New core features: streaming responses/SSE, DOM morphing swaps, a <partial> tag, queued view transitions, and standardized hx-on. Core APIs mostly unchanged; 2.x supported indefinitely, with extensions to emulate legacy behavior and a slow rollout (alpha now; GA 2026). HN jokes about skipping 3.0, praises no-pressure upgrades, and questions :inherited naming and “no-JS” ergonomics.

- Comment pulse
    - Skipping 3.0 is funny → avoids breaking a promise, but may confuse users; a straight 3.0 might be clearer.
    - Perpetual 2.x support and slow migration → reduces churn and risk for production apps.
    - ':inherited' modifier feels wrong → 'inherit'/'heritable' suggested; naming clarity matters — counterpoint: author is open to alternatives and feedback.

- LLM perspective
    - View: Switching to fetch() and explicit inheritance simplifies internals; ditching local history trades speed for reliability.
    - Impact: Extension authors must adapt to new event model; backends can leverage streaming and partials; fewer client-side footguns.
    - Watch next: Publish migration guides, event mappings, benchmarks for history latency; decide ':inherited' naming; examples of SSE, morph swaps, transition queue.
