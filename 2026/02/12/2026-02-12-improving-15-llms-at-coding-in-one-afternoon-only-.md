# Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed

- Score: 529 | [HN](https://news.ycombinator.com/item?id=46988596) | Link: http://blog.can.ac/2026/02/12/the-harness-problem/

### TL;DR

The author replaced a coding agent’s edit interface with line numbers plus short content hashes, letting models reference stable anchors instead of reproducing exact old text or specialized patch syntax. Stale hashes reject edits after files change. Across 180 mutation-repair tasks, three runs, 16 models, and three formats, the method usually matched or beat string replacement and outperformed patches for weaker models; one rose from 6.7% to 68.3%, while another cut output 61%. Commenters saw harnesses as part of model capability, but warned the synthetic benchmark may overstate real-world gains.

### Comment pulse

- Advocates view the agent as model plus harness, arguing better context, schemas, and feedback can revive even older or local models.
- Skeptics called the claims oversold—counterpoint: reported token reductions reached 25–50%, though translation to full workflows remains unknown.
- Codex-specific results need constrained-sampling controls because its patch grammar uses a schema; otherwise comparisons may disadvantage its native path.

### LLM perspective

- View: The technique isolates a real interface failure: editing needs compact identity, concurrency detection, and model-neutral syntax.
- Impact: Harness builders can improve reliability without retraining; benchmark designers must separate reasoning failures from mechanical application failures.
- Watch next: Replicate on natural repositories, concurrent edits, semantic refactors, multiple languages, constrained decoding, and end-to-end cost.
