# Bonsai: Janestreet's UI Library

- Score: 384 | [HN](https://news.ycombinator.com/item?id=49152842) | Link: https://github.com/janestreet/bonsai

### TL;DR

Bonsai is Jane Street’s OCaml framework for reactive interfaces, used across most of its internal web applications. It models components as composable functional state machines and applies incremental computation to state and business logic, not only rendering. Bonsai_web targets browsers, Bonsai_term targets terminals, and built-in expect tests manipulate UI elements while showing DOM diffs. Shared OCaml types across frontend and backend aid large-codebase maintenance. HN framed it as an incremental distributed-state-machine toolkit, while debating JavaScript ecosystem integration, visual polish, and alternatives such as Melange, Phoenix, and Scala.js.

### Comment pulse

- Incrementality is the core distinction → Bonsai composes state and recomputation independently, extending optimization beyond component rerenders.
- One language improves type continuity → OCaml can span client and server, but integration with JavaScript libraries may require ecosystem trade-offs.
- Testing impressed more than styling → deterministic DOM diffs support browserless development, while some readers found the public examples visually rough.

### LLM perspective

- View: Bonsai is best understood as a state-machine framework with web rendering attached.
- Impact: OCaml teams gain reusable business logic and strong tests across browser and terminal interfaces.
- Watch next: External adoption, documentation maturity, JavaScript interop, and performance comparisons on large live datasets.
