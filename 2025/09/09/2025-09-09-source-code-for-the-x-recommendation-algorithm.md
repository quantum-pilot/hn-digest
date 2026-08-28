# Source code for the X recommendation algorithm

- Score: 244 | [HN](https://news.ycombinator.com/item?id=45183039) | Link: https://github.com/twitter/the-algorithm

### TL;DR

X published a repository describing services, data signals, models, and frameworks behind surfaces including For You and recommended notifications. The documented pipeline draws roughly half its candidates from in-network search, supplements them with out-of-network and graph sources, then applies ranking and visibility filters. However, the repository lacks a top-level build configuration, trained weights, and proof that the published code matches production. Commenters therefore treat it as architectural documentation and selective transparency, not a reproducible release of the live recommendation system.

### Comment pulse

- Readers noticed metrics for Grok-derived categories, political neutrality, low-quality content, screenshots, and safety signals.
- Discussion cautions that tracked metrics do not by themselves prove those fields directly influence recommendations.

### LLM perspective

- View: Code disclosure is useful, but operational transparency requires deployable artifacts, weights, data lineage, and version correspondence.
- Impact: Researchers can inspect vocabulary and architecture while remaining unable to reproduce or audit actual ranking behavior.
- Watch next: Buildability, model releases, production-version attestations, and experiments showing how documented signals affect reach.
