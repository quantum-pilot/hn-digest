# Tally – A tool to help agents classify your bank transactions

- Score: 86 | [HN](https://news.ycombinator.com/item?id=46475218) | Link: https://tallyai.money/

### TL;DR

Tally classifies exported bank transactions using local, inspectable rules rather than model calls at runtime. An optional coding agent interprets messy merchant descriptions and helps author or refine those files; once rules exist, classification runs deterministically and offline, producing spending reports without a database or cloud service. HN criticism initially assumed a token-burning model sat in the execution path, while the author’s clarification shifted debate toward whether agents genuinely reduce rule-maintenance work, how irregular payment data defeats simple matching, and whether CSV import is sufficiently user-friendly.

### Comment pulse

- Determinism is the retained artifact → agents help write rules, but recurring classification is local, explainable, and model-free.
- Merchant strings resist tiny scripts → inconsistent descriptors and cross-account references require continuing exceptions and context.
- CSV workflows limit mainstream appeal → turnkey bank integrations feel easier, but may be inaccessible to small open-source tools.

### LLM perspective

- View: Using probabilistic tools to produce deterministic rules is a practical boundary between assistance and automation.
- Impact: Users retain auditable financial logic while offloading tedious rule discovery.
- Watch next: Evaluate classification accuracy, rule conflicts, new-merchant handling, and support for heterogeneous bank exports.
