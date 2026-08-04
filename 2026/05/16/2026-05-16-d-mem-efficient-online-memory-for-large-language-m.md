# δ-mem: Efficient Online Memory for Large Language Models

- Score: 189 | [HN](https://news.ycombinator.com/item?id=48158506) | Link: https://arxiv.org/abs/2605.12357

### TL;DR

δ-mem augments a frozen full-attention LLM with a fixed-size associative state updated online by a delta rule; its readout creates low-rank corrections to attention without extending context, replacing the backbone, or fully fine-tuning it. An 8×8 state reportedly scores 1.10× the backbone average, 1.15× the strongest compared memory baseline, 1.31× on MemoryAgentBench, and 1.20× on LoCoMo. HN found the approach promising but questioned fixed-capacity forgetting, query sensitivity, novelty, missing runtime and RAM costs, benchmark overfitting, and whether it provides usable cross-session memory.

### Comment pulse

- Fixed size trades unbounded growth for interference → new information may degrade older details — counterpoint: associative matrices can theoretically encode far more than caches.

- Retrieval remains the hard part → semantically similar queries can produce different activations, motivating contextual search or explicit structured-memory filtering.

- Evaluation is incomplete → commenters wanted actual RAM bytes, latency, throughput, update cost, contamination checks, and comparisons against simpler DeltaNet-style baselines.

### LLM perspective

- **View:** Lossy online adaptation differs from a searchable archive; it may capture recurring patterns better than exact historical facts.

- **Impact:** Long-running assistants could retain compact behavioral context with constant state size, but sensitive applications need predictable forgetting and auditability.

- **Watch next:** Test month-scale streams, adversarial updates, exact-fact recall, memory saturation, recovery after interference, cross-domain transfer, and total inference overhead.
