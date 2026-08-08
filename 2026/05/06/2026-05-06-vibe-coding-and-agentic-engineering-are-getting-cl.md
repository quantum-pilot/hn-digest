# Vibe coding and agentic engineering are getting closer than I'd like

- Score: 346 | [HN](https://news.ycombinator.com/item?id=48037128) | Link: https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/

### TL;DR

Simon Willison’s boundary was simple: vibe coding meant accepting unreviewed code for low-stakes personal tools, while agentic engineering paired AI with professional judgment for production systems. That line is blurring as reliable agents tempt him to treat routine code like a trusted team’s black-box service. The danger is normalization of deviance: repeated success may encourage misplaced trust, while polished tests, documentation, and commit history no longer prove care. HN remained skeptical, arguing routine endpoints still contain design choices and that increasingly subtle AI errors can raise, not reduce, review burden.

### Comment pulse

- Production APIs encode naming, errors, reuse, queries, observability, and evolution choices → generating the wiring does not eliminate engineering decisions.
- AI amplifies existing discipline → strong teams can formalize tests and small changes — counterpoint: weak teams can manufacture technical debt far faster.
- Generated polish is no longer credible provenance → sustained real-world use and accountable maintainers become stronger trust signals than repository appearance.

### LLM perspective

- **View:** Review should become risk-based, not line-based; generated code needs evidence proportional to blast radius and novelty.
- **Impact:** Maintainers inherit more plausible code per hour, shifting cost toward validation, operations, deletion, and ownership.
- **Watch next:** Escaped-defect rates, review time per generated change, incident attribution, maintainer reputation, and longitudinal production use.
