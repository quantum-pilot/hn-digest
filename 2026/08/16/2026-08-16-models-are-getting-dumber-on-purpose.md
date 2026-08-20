# Models Are Getting Dumber on Purpose

- Score: 334 | [HN](https://news.ycombinator.com/item?id=49322695) | Link: https://w4g1.dev/blog/models-are-getting-dumber-on-purpose

### TL;DR

The essay argues model makers deliberately exchange memorized facts for compact reasoning procedures: smaller mixture-of-experts and distilled models excel at math and code yet perform poorly on unaided recall. Runtime retrieval, tools, and local documentation would then supply current knowledge, making errors traceable and updates cheap while enabling frontier-like reasoning on consumer GPUs. Commenters challenged the facts-versus-procedures split, stale benchmark comparisons, hallucination theory, and speculative parameter accounting. Supporters liked modular local systems, but others said general knowledge aids transfer and specialization belongs in the harness.

### Comment pulse

- Retrieval makes sources inspectable—counterpoint: models can misread them, search is fallible, and weight-derived claims remain externally checkable.
- Pluggable domain modules appealed to local users, while critics said broad knowledge supplies abstractions that narrow specialists would lose.
- Several suspected machine authorship and considered the model and benchmark examples outdated, undermining the essay’s own freshness argument.

### LLM perspective

- View: The strongest case is freshness and provenance, not a proven architectural separation between stored facts and reasoning.
- Impact: Successful small local agents would shift cost and privacy tradeoffs toward retrieval quality and harness engineering.
- Watch next: Controlled parameter studies, updated recall tests, sourced-answer error rates, total memory, latency, and energy.
