# Kimi K3, and what we can still learn from the pelican benchmark

- Score: 255 | [HN](https://news.ycombinator.com/item?id=48947717) | Link: https://simonwillison.net/2026/Jul/16/kimi-k3/

### TL;DR

Moonshot AI’s Kimi K3 is a 2.8-trillion-parameter model available by web and API, with open weights promised by July 27. At $3 per million input tokens and $15 per million output tokens, it is unusually expensive among Chinese models, though external tests place it near leading frontier systems. Simon Willison’s unserious pelican-on-a-bicycle SVG prompt exposed practical traits: valid output and strong vision, but 13,241 reasoning tokens, a 25-cent cost, only “max” effort, and probable hidden prompt overhead. The test no longer ranks models reliably; it remains a useful hands-on diagnostic.

### Comment pulse

- Training contamination split readers → critics assumed repeated public pelicans enter corpora; defenders distinguished incidental exposure from deliberate benchmark optimization.
- Token overhead drew a concrete hypothesis → the unexplained input count may include an injected reasoning-effort prompt before the model’s thinking block.
- Comparisons reinforced the intended use → Kimi appeared much cheaper but slower, illustrating that one probe is best for cost-speed-quality characterization, not ranking.

### LLM perspective

- **View:** A toy task is valuable as instrumentation: it reveals access, billing, hidden overhead, reasoning behavior, formatting, vision, and regressions.
- **Impact:** K3’s compulsory maximal reasoning can turn trivial work expensive and slow, limiting value despite per-token pricing and benchmark performance.
- **Watch next:** Re-test after open weights and effort controls arrive; measure tool reliability, long-context stability, hidden tokens, and family-level regressions.
