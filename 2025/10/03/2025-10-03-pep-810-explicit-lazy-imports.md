# PEP 810 – Explicit lazy imports

- Score: 245 | [HN](https://news.ycombinator.com/item?id=45466086) | Link: https://pep-previews--4622.org.readthedocs.build/pep-0810/

TL;DR
- PEP 810 adds an explicit soft keyword, lazy, for module-level imports (lazy import x; lazy from x import y). It binds a proxy and loads on first use, deferring errors and side effects. Star imports and imports inside functions/classes/try/with are excluded. Controls include a global mode, a filter API, and a __lazy_modules__ migration hook. Claimed wins: faster startup for CLIs/tests and lower baseline memory. HN favors the opt‑in, local design but debates verbosity, tooling, and prior PEP 690’s rejection context.

Comment pulse
- CLI/plugin ecosystems need this → heavy deps block --help; parse args first, then import — counterpoint: global hacks can cause unpredictable pauses.
- Opt‑in beats prior global proposal → avoids dual-mode complexity and aligns with Cinder experience.
- Concern: noisy syntax everywhere → prefer module- or project-level config; caller should decide laziness; optional features rarely overrun codebases.

LLM perspective
- View: Pragmatic, explicit mechanism that preserves predictability while unlocking measurable startup and memory wins.
- Impact: Biggest gains for CLIs, test runners, data stacks with heavy deps, and plugin-heavy apps.
- Watch next: Steering Council decision, formatter/linter updates, real-world benchmarks and shared lazy-import filter recipes.
