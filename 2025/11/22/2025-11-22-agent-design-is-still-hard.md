# Agent design is still hard

- Score: 333 | [HN](https://news.ycombinator.com/item?id=46013935) | Link: https://lucumr.pocoo.org/2025/11/21/agents-are-hard/

### TL;DR

Armin Ronacher reports that production agents still resist clean, provider-neutral abstractions. Model-specific caching, tools, errors, and reinforcement led his team to prefer native SDKs and a manually controlled loop. Their design reinforces objectives after tool calls, isolates noisy failures, and uses a shared virtual filesystem so inference and code tools exchange artifacts without dead ends. Explicit output tools remain hard to steer, token price poorly predicts total cost, and evaluation is the largest unresolved problem because real execution state is difficult to reproduce.

### Comment pulse

- Handwritten loops often beat broad SDKs → extra boilerplate can be easier than debugging leaky provider abstractions.
- Fast model evolution shortens pattern lifetimes → waiting can avoid expensive work — counterpoint: participation creates reusable understanding.
- Existing coding agents provide a strong baseline → bespoke systems must justify capability loss and maintenance burden.

### LLM perspective

- View: The stable primitive is a tool-using loop; nearly everything around it remains task- and provider-specific.
- Impact: Teams should budget for harness engineering, observability, and evaluation rather than treating SDK selection as the architecture.
- Watch next: Compare native and unified SDKs on cache cost, tool reliability, failure recovery, and reproducible evals.
