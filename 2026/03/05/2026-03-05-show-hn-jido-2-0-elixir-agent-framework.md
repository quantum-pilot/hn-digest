# Show HN: Jido 2.0, Elixir Agent Framework

- Score: 229 | [HN](https://news.ycombinator.com/item?id=47263036) | Link: https://jido.run/blog/jido-2-0-is-here

### TL;DR

Jido 2.0 rebuilds the Elixir agent framework around a smaller, BEAM-native core: agents are data, cmd/2 is a pure transition function, and side effects become directives executed by supervised AgentServers. Direct and finite-state strategies work without models; Jido AI adds six reasoning strategies and ReqLLM’s 11-provider, 665-plus-model client. Separate action and CloudEvents-based signal packages supply tools, workflows, routing, and dispatch, while Ash integration exposes authorized resource actions. Commenters welcomed the testability and concurrency model but emphasized checkpointing agent state across node failures and rolling deployments.

### Comment pulse

- Pure state won the strongest praise → serializable checkpoints can let another node resume an agent after failure or deployment.
- The creator keeps the core model-free → established agent architecture should work before LLM reasoning is added as a strategy.
- Interest remains tempered by ecosystem maturity → early adopters like BEAM’s fit but still compare available integrations and operational tooling.

### LLM perspective

- **View:** Separating deterministic transitions from probabilistic reasoning makes agent behavior easier to test and recover.
- **Impact:** Elixir teams gain a shared runtime for conventional workflows and model-driven agents.
- **Watch next:** Production failure recovery, checkpoint adapters, ecosystem adoption, and operational benchmarks versus Python or TypeScript frameworks.
