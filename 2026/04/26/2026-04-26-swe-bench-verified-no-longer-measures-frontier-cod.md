# SWE-bench Verified no longer measures frontier coding capabilities

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47910388) | Link: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/

### TL;DR

OpenAI will stop reporting SWE-bench Verified for frontier launches because its remaining failures reflect benchmark defects and training exposure, not coding ability. In 138 tasks that o3 often missed, reviewers found specification or test flaws in 59.4%: tests demanded unstated implementation details, extra functionality, or environment-specific behavior. GPT-5.2, Claude Opus 4.5, and Gemini 3 Flash could reproduce task-specific gold-patch details, indicating contamination. OpenAI recommends SWE-bench Pro and private, expert-authored evaluations. Hacker News agreed benchmarks invite optimization, while noting Verified still measures weaker systems and questioning whether the failure-heavy audit generalizes.

### Comment pulse

- SWE-bench’s co-creator calls Verified saturated at 93.9% but says it remains useful below that ceiling; multilingual and multimodal successors remain open.
- A failure-focused sample may overstate dataset-wide flaws — counterpoint: valid-solution rejection still destroys comparisons among top systems.
- Commenters favor rotating private or dynamic evaluations because static public tasks enter training data and attract benchmark-specific optimization.

### LLM perspective

- **View:** A benchmark stops ranking frontier capability when ceiling effects, label error, and contamination approach observed model differences.
- **Impact:** Labs need continuously refreshed tasks and human review, raising evaluation cost and reducing public reproducibility.
- **Watch next:** SWE-bench Pro audits, private canaries, held-out repository dates, merge-quality grading, dynamic tasks, and cross-lab governance.
