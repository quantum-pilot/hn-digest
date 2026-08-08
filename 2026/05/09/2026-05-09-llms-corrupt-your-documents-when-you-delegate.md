# LLMs corrupt your documents when you delegate

- Score: 336 | [HN](https://news.ycombinator.com/item?id=48073246) | Link: https://arxiv.org/abs/2604.15597

### TL;DR

DELEGATE-52 tests 19 models on long document-editing workflows across 52 professions and finds even Gemini 3.1 Pro, Claude 4.6 Opus, and GPT 5.4 corrupt roughly 25% of content on average. Damage compounds with larger files, longer interactions, and distractors; the study’s basic agentic tools did not help. HN accepted the danger of repeated semantic rewriting but challenged the harness, which largely reads and rewrites whole files. Commenters argued surgical edits, deterministic transformations, diffs, and validation should surround the model—while noting ordinary office users rarely have such infrastructure.

### Comment pulse

- Whole-document regeneration invites lossy “semantic ablation” → repeated passes pull precise, unusual material toward generic training-distribution language.
- Experienced agent users faulted read/write-only tooling → counterpoint: unsophisticated workflows are exactly how many organizations deploy models.
- Keep LLMs as thin intent translators → deterministic code should move data, while tests and diffs detect unintended changes.

### LLM perspective

- **View:** The benchmark exposes a product-level trust gap even if optimized harnesses would score better.
- **Impact:** High-stakes document owners must treat delegated edits as untrusted patches, not finished artifacts.
- **Watch next:** Re-run DELEGATE-52 with modern edit tools, immutable source spans, and independent semantic validators.
