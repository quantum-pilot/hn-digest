# The Cathedral, the Bazaar, and the Winchester Mystery House

- Score: 150 | [HN](https://news.ycombinator.com/item?id=47601194) | Link: https://www.dbreunig.com/2026/03/26/winchester-mystery-house.html

### TL;DR

AI makes implementation so cheap that software is shifting beyond cathedral and bazaar into a “Winchester Mystery House” model: one developer adds personalized, sprawling, poorly documented rooms because the feedback loop is immediate and building is fun. Claude-attributed commits average about 1,000 net lines, while review and coordination remain human-speed. Open source therefore receives both more useful work and overwhelming agent-generated noise. The author argues personal houses and bazaars can coexist if communities own boring, risky foundations while new tools make attention, triage, pruning, and idea discovery scale with production.

### Comment pulse

- Readers questioned whether machine-speed output creates productivity or a house of cards, particularly when claimed security remains difficult to verify.
- Net additions alone obscure churn; commenters recommended deletion-aware metrics and constrained refactoring prompts that require simpler code without altering tests.
- Historical corrections noted ESR’s cathedral described isolated development, not necessarily proprietary software, and documented an existing open-source shift rather than initiating it.

### LLM perspective

- **View:** The binding resource moved from keystrokes to judgment; measuring generated code rewards the wrong side of the bottleneck.
- **Impact:** Maintainers absorb rising verification costs, while individuals gain bespoke tools that may become untransferable when their creator leaves.
- **Watch next:** Review latency, rejected PRs, deletion ratios, defect density, maintainer burnout, provenance signals, and automated contribution triage.
