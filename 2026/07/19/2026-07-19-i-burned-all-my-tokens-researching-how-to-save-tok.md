# I burned all my tokens researching how to save tokens

- Score: 89 | [HN](https://news.ycombinator.com/item?id=48967355) | Link: https://quesma.com/blog/custom-deep-research-pipeline/

### TL;DR

After an initial deep-research run exhausted a Claude subscription limit without producing a report, the author rebuilt the workflow around role-specific models and three existing subscriptions. Cheaper agents find material, stronger models independently verify claims, expensive reasoning handles planning and disputes, and deep research runs last over a bounded evidence set. Shared memory and automatic fallbacks reportedly extended continuous work from 30 minutes to hours. The larger lesson is that harness design, caching, compaction, verification rules, and human review can matter as much as model choice.

### Comment pulse

- Pipeline staging won support → cheap parallel exploration narrows the search space before costly models judge it, with model diversity improving hypothesis coverage.
- “No hallucinations” drew pushback → rules and cross-model checks reduce errors but cannot eliminate them; the author conceded the wording overstated the result.
- Local-first routing divided readers → privacy and repetitive workloads favor it, while hardware cost and task-selection difficulty often favor cheaper cloud models.

### LLM perspective

- **View:** Cost optimization is chiefly an orchestration problem: allocate discovery, verification, judgment, and synthesis according to their marginal accuracy needs.
- **Impact:** Multi-subscription routing can stretch fixed allowances, but it shifts complexity into memory sharing, fallback logic, provenance, and governance.
- **Watch next:** Measure verified findings per dollar and hour—not agent count—and test whether different models make independent errors.
