# SQL patterns I use to catch transaction fraud

- Score: 308 | [HN](https://news.ycombinator.com/item?id=48155212) | Link: https://analytics.fixelsmith.com/posts/sql-fraud-patterns/

### TL;DR

The article proposes six SQL heuristics for transaction fraud: short-window velocity, impossible travel, suspicious amounts, merchant-level spikes, off-hours behavior, and reusable window-function features that combine signals. It recommends baselines, whitelists, human review, privacy controls, and date filtering before expensive windows. HN challenged the practical grounding: round amounts and border crossings can be normal, merchant locations may be wrong, and off-hours rules invite false positives. Several readers suspected the examples and author persona were AI-generated, making validation more important than query elegance.

### Comment pulse

- Geography and amounts are market-specific → €10 purchases, border commutes, $1 authorizations, and bad merchant metadata can all look fraudulent.
- Single heuristics need calibrated baselines and review → counterpoint: the article recommends combining signals, feedback loops, and avoiding automatic blocks.
- Readers questioned provenance and experience, citing contradictions, generic prose, and unrealistic location assumptions rather than merely objecting to AI-like style.

### LLM perspective

- **View:** Fraud SQL is hypothesis generation, not adjudication; operational value depends on labels, calibration, and investigation outcomes.
- **Impact:** Analysts can iterate quickly, but false positives burden customers and reviewers when data semantics or regional behavior are misunderstood.
- **Watch next:** Backtest precision, recall, alert volume, segment drift, metadata quality, reviewer agreement, query cost, and confirmed-loss reduction.
