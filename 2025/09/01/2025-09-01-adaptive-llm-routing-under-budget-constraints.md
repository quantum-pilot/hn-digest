# Adaptive LLM routing under budget constraints

- Score: 206 | [HN](https://news.ycombinator.com/item?id=45094421) | Link: https://arxiv.org/abs/2508.21141

### TL;DR

PILOT frames LLM routing as a contextual-bandit problem rather than supervised classification. It learns a shared query-model embedding from offline human preferences, then updates that representation from online bandit feedback without evaluating every model on every query. A multi-choice knapsack policy adapts selections to different budgets. The paper was accepted to EMNLP 2025 Findings. Commenters questioned how quality should be measured, whether token price ignores interaction length, and whether API savings matter yet in typical enterprises.

### Comment pulse

- Routing economics look attractive across large price gaps → counterpoint: tokens per interaction and failure costs can erase per-token savings.
- Human preferences may encode suitability better than model self-assessment, though commenters disputed whether that extra supervision is necessary.

### LLM perspective

- View: Online adaptation fits changing workloads better than a frozen table of supposedly optimal model assignments.
- Impact: High-volume applications could trade small quality losses for controlled inference spending under explicit budgets.
- Watch next: Independent results using task success, user satisfaction, retries, and total interaction cost.
