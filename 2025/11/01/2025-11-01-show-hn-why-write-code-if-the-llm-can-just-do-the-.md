# Show HN: Why write code if the LLM can just do the thing? (web app experiment)

- Score: 191 | [HN](https://news.ycombinator.com/item?id=45783640) | Link: https://github.com/samrolken/nokode

- TL;DR
    - An experiment replaces app logic with an LLM plus three tools (SQL, HTTP response, feedback memory). Given only request paths, it built a working CRUD contact manager: inferred schema, safe parameterized SQL, HTML/JSON, and implemented user feedback. But each request took 30–60s, cost $0.01–$0.05, forgot designs, and occasionally hallucinated errors. HN applauds the provocation yet debates determinism and energy cost; proposals include “code as consistency cache,” adding persistent state to stabilize UX, and using LLMs for intent/prototyping while conventional code serves fast paths.

- Comment pulse
    - Use code as 'memory' to cache LLM outputs → Handlers serve later requests fast and consistent; feedback updates code; LLM-only path is a cache miss.
    - Users need deterministic behavior → Shifting UIs/schemas disorient; saved settings or temp=0 can enforce stability — counterpoint: richer, app-like LLM interactions may justify flexibility.
    - LLM serving is inefficient → Tokens cost cents and GFLOPs; use for prototypes/intent, then replace hot paths with conventional code; investors may ignore efficiency.

- LLM perspective
    - View: Use LLM as intent interpreter; generate and persist code/UI/state to turn stochastic planning into cached, deterministic execution.
    - Impact: Teams move from CRUD to tools, guardrails, prompts, and eval harnesses; faster MVPs, fewer engineers on repetitive layers.
    - Watch next: Latency/cost benchmarks, deterministic rendering techniques, code-as-cache prototypes, sandboxed self-updates gated by tests and human-in-the-loop approval.
