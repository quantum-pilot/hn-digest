# Using AI to write better code more slowly

- Score: 1135 | [HN](https://news.ycombinator.com/item?id=48272984) | Link: https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/

### TL;DR

The author rejects AI coding as a race to generate code, instead using Claude, Codex, and Cursor Bugbot as independent PR reviewers. A lead agent validates and ranks findings; humans guide fixes, skip low-value edge cases, or abandon flawed approaches. Repeated passes often uncover pre-existing bugs, trading velocity and tokens for stronger code and deeper understanding. HN commenters largely described similarly review-heavy workflows, but disputed the payoff: some gain better specifications and near-final quality, while others lose time, control, architectural judgment, or enjoyment.

### Comment pulse

- Architecture dialogue preserves agency → developers refine specifications before coding; one experienced commenter spends roughly 70% of agent sessions discussing design.
- Fallible suggestions can teach → explicit requests for critiques and alternatives counter anchoring while forcing users to verify reasoning before implementation.
- Review feels less deskilling than generation → skeptical developers retain judgment — counterpoint: multi-reviewer PR interfaces are cumbersome and ethical costs remain.

### LLM perspective

- **View:** Model diversity resembles ensemble testing: independence reduces correlated blind spots, while synthesis introduces another failure point.
- **Impact:** Engineering teams may shift effort from typing to specification, evaluation, and deciding when additional review no longer pays.
- **Watch next:** Benchmark multi-model review against expert review for defect recall, false positives, latency, token cost, and developer comprehension.
