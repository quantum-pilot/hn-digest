# Nvidia Nemotron 3.5 Lightning and NeMo Switchyard

- Score: 230 | [HN](https://news.ycombinator.com/item?id=49263340) | Link: https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/

### TL;DR

Nvidia released Nemotron 3.5 Lightning, a customizable 30-billion-parameter mixture-of-experts model for high-volume agent tasks, and NeMo Switchyard, an open-source router selecting among local, proprietary, and Nvidia models by quality, latency, or cost. Nvidia claims up to 4× generation speed, 30% faster task completion, and near-frontier routing at about one-third of Opus 4.8's cost, based largely on internal or partner tests. HN's hands-on reports found Lightning fast but unreliable on substantial coding, questioned omitted Qwen comparisons, and flagged caching and extra routing-call overhead.

### Comment pulse

- One whiteboard test favored several dense 27–31B models; Laguna XS complicated a simple dense-versus-MoE explanation.
- Per-turn routing can sacrifice prompt-cache reuse → cache-aware stickiness exists, but Switchyard's documented strategy remained unclear.
- The repository calls Switchyard experimental despite deployment language, sharpening doubts about production readiness.

### LLM perspective

- **View:** Router value must be measured on completed workflows, including classification overhead, cache misses, and retries.
- **Impact:** Enterprises can combine specialized local models with costly frontier calls without rewriting agent applications.
- **Watch next:** Independent Qwen comparisons, cache behavior, routing latency, failure recovery, and graduation from experimental status.
