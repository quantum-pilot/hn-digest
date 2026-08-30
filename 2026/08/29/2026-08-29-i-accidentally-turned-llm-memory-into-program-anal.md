# I accidentally turned LLM memory into program analysis

- Score: 285 | [HN](https://news.ycombinator.com/item?id=49485416) | Link: https://pwning.systems/posts/llm-memory-program-analysis/

### TL;DR

Lemmalog treats agent memory as maintained program-analysis state: an LLM extracts structured facts, while Datalog derives conclusions, tracks provenance, retracts dependencies, and records validity intervals. Hybrid retrieval preserves fuzzy source context. In the author's tests, it used far less query context and performed strongly on knowledge updates, temporal reasoning, and false premises, though PropMem remained better overall and inference or multi-session tasks exposed extraction losses. Commenters recognized a neuro-symbolic pattern, while warning that ontologies, quantifiers, and probabilistic extraction can drift.

### Comment pulse

- Move quickly from language into deterministic structure → repeated reasoning becomes reusable, inspectable state rather than recurring model work.
- Provenance and retractions reduce stale beliefs → every conclusion can expose supporting observations and disappear when support fails.
- Symbolic memory suits concrete facts → counterpoint: conditional, ambiguous, and opinion-based knowledge resists flattening into tuples.

### LLM perspective

- View: Lemmalog separates relevance retrieval from truth maintenance, addressing a real failure hidden beneath “memory.”
- Impact: Long-running research agents could stop resurrecting disproven hypotheses while reducing repeated context costs.
- Watch next: Test real vulnerability investigations, extraction error propagation, ontology evolution, and comparisons using equal total ingestion costs.
