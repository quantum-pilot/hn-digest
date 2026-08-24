# Kimi Released Kimi K2.5, Open-Source Visual SOTA-Agentic Model

- Score: 453 | [HN](https://news.ycombinator.com/item?id=46775961) | Link: https://www.kimi.com/blog/kimi-k2-5.html

### TL;DR

Moonshot AI describes Kimi K2.5 as a native multimodal, open-source model trained on about 15 trillion mixed visual and text tokens. It targets coding with visual context, document production, scientific reasoning, and long-form office work. A beta swarm mode dynamically creates up to 100 subagents and coordinates as many as 1,500 tool calls; Parallel-Agent Reinforcement Learning rewards useful concurrency while discouraging idle spawning. Moonshot reports execution speedups of up to 4.5×, but commenters questioned hardware requirements, tool-call economics, licensing conditions, and whether swarm capabilities are actually open.

### Comment pulse

- The posted model has one trillion parameters with 32 billion active, making home deployment impractical even at 4-bit precision.
- Enthusiasts celebrated strong Chinese open releases — counterpoint: skeptics questioned usage, business motives, and safety implications.
- Autonomous orchestration impressed readers, but 1,500 tool calls raised cost concerns and questions about model-versus-service implementation.

### LLM perspective

- View: Training the orchestrator, rather than hand-coding agent roles, is the release’s most distinctive idea.
- Impact: Parallel decomposition could shorten broad research tasks, but infrastructure costs concentrate practical access among hosted providers.
- Watch next: Independent benchmarks, exact weight coverage, license interpretation, swarm pricing, tool efficiency, and reproducible latency gains.
