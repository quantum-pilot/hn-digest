# An empirical study of harness design for coding agents

- Score: 201 | [HN](https://news.ycombinator.com/item?id=49753878) | Link: https://arxiv.org/abs/2609.20804

### TL;DR

A 43-page study isolates coding-agent harness components by testing four models across 176 matched configurations on SWE-Bench Verified and Terminal-Bench 2.1. Context management mattered most under tight windows, mainly by preventing overflow; rule-based elision followed by model summarization offered the best efficiency, while recoverable elisions added unused machinery. Planning improved weaker-model accuracy but mostly reduced stronger-model cost. Predefined tools helped models weak at bash, whereas bash-capable models performed effectively and more cheaply with bash alone. HN welcomed the component-level evidence but debated model generalizability.

### Comment pulse

- Harness design materially shapes measured capability → identical models can differ through planning, context policy, tool semantics, and task fit.
- Simpler agents remain competitive → commenters report minimal loops often matching elaborate systems while leaving room for targeted infrastructure.
- Model selection limits confidence → critics wanted current frontier systems; others argued component trends need evidence before being dismissed as obsolete.

### LLM perspective

- View: Harness features should compensate for specific model weaknesses instead of accumulating by default.
- Impact: Teams can lower cost by matching context, planning, and tools to model proficiency and task environment.
- Watch next: Replicate across frontier and open models, larger windows, additional benchmarks, and real repositories with controlled ablations.
