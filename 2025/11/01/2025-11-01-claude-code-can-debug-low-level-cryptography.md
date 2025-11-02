# Claude Code Can Debug Low-Level Cryptography

- Score: 155 | [HN](https://news.ycombinator.com/item?id=45784179) | Link: https://words.filippo.io/claude-debugging/

- TL;DR
  - Filippo Valsorda implemented ML‑DSA in Go; verification kept failing. Claude Code rapidly pinpointed the culprit: HighBits of w1 were applied twice in Verify due to a reused helper. In a replay, it also identified two signing bugs: miscomputed Montgomery constants that caused looping and a 32‑bit vs 32‑byte length error. Filippo refactored himself but said the agent saved hours. HN commenters praise LLMs for targeted bug-hunting, with cautions about bikeshedding, overconfidence, and weaker performance on concurrency.

- Comment pulse
  - Use LLMs as bug hunters, not authors → fast root-cause on failing tests; humans decide fixes — counterpoint: agents bikeshed, flood PRs, create busywork.
  - Strong on algorithmic debugging and test generation → pattern matching across code; weaker at concurrency orchestration and timing.
  - Experts benefit most → they detect hallucinations; novices risk being misled and wasting time.

- LLM perspective
  - View: Test-guided, spec-heavy debugging is a sweet spot for agents; generate hypotheses and minimal patches, let humans refactor.
  - Impact: Faster root-cause isolation for cryptography, compilers, and systems code; improved maintainer productivity during PQC rollouts.
  - Watch next: CI agents triaging failing tests; benchmarks on time‑to‑diagnosis and false positives; datasets for concurrency bugs.
