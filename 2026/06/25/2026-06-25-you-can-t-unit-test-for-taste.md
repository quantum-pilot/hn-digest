# You can't unit test for taste

- Score: 238 | [HN](https://news.ycombinator.com/item?id=48657049) | Link: https://dev.karltryggvason.com/you-cant-unit-test-for-taste/

### TL;DR

A developer built a points-of-interest pipeline for a virtual-running app, reducing 13 million GeoNames records to 725,000 candidates, matching them to routes, and ranking them with Wikimedia signals plus an LLM. Haiku’s generated descriptions hallucinated locations, populations, and elevations, so Wikipedia text replaced them; the model remained only as a subjective ranking input. Route-specific biases and spatial clustering still required manual tuning because no universal ground truth defines an interesting stop. HN debated whether taste can be formalized, favoring human validation and supervised AI over fully automated judgment.

### Comment pulse

- Explicit criteria make some preferences testable → commenters proposed documentation, evaluation gates, and manual QA — counterpoint: tacit judgment cannot be fully externalized.
- Process quality governs agent usefulness → plan-and-revise cycles, architectural decision records, and end-user evaluation can keep humans responsible for direction.
- Alternative signals may reduce ad hoc ranking → QRank aggregates page views across Wikimedia projects, offering a more direct popularity measure than language count.

### LLM perspective

- **View:** The design separates factual generation from preference scoring, assigning the model only the lower-stakes task its errors can tolerate.
- **Impact:** Product teams need route-specific overrides and visible inspection tools when optimizing subjective outputs across culturally uneven datasets.
- **Watch next:** Compare QRank, language count, and model ratings against user-selected landmarks; track hallucination, geographic coverage, and diversity.
