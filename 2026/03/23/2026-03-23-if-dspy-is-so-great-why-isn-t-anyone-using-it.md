# If DSPy is so great, why isn't anyone using it?

- Score: 198 | [HN](https://news.ycombinator.com/item?id=47490365) | Link: https://skylarbpayne.com/posts/dspy-engineering-patterns/

### TL;DR

DSPy packages LLM applications as typed signatures, composable modules, evaluation pipelines, and optimizers that can tune prompts or examples and recompile for different models. The essay argues teams avoid it because its abstractions feel unfamiliar, then gradually rebuild inferior versions through prompt stores, retries, RAG, schemas, evals, and provider adapters. HN commenters say most listed practices are ordinary engineering available in lighter tools; the real differentiator—optimization—depends on costly, representative datasets and automated metrics, which are hardest precisely for open-ended agent and chat tasks.

### Comment pulse

- Python-only adoption can require a separate service for stacks written primarily in TypeScript or other languages.
- External prompt editing offers rapid iteration — counterpoint: it can resemble changing production code without deployment controls.
- Traditional classifiers may beat LLMs on latency and cost, though commenters disputed whether older NER handles messy references adequately.

### LLM perspective

- **View:** DSPy pays off when a stable metric makes automated search more valuable than manual tuning.
- **Impact:** Teams without mature eval data inherit framework complexity before optimization benefits.
- **Watch next:** Optimizer ablations, total eval cost, cross-model transfer, non-Python support, and production observability.
