# Two different tricks for fast LLM inference

- Score: 157 | [HN](https://news.ycombinator.com/item?id=47022329) | Link: https://www.seangoedecke.com/fast-llm-inference/

### TL;DR
Anthropic and OpenAI both launched “fast mode” for coding models, but via very different trade-offs. Anthropic appears to speed up its flagship Claude Opus 4.6 by changing inference configuration (likely smaller batches, preferential routing to faster hardware, and possibly more aggressive test-time compute), giving ~2.5x tokens/sec at much higher cost but unchanged quality. OpenAI’s GPT‑5.3‑Codex‑Spark runs on Cerebras wafer-scale chips, delivering ~15x tokens/sec via a smaller distilled model that’s meaningfully less capable, better suited as an internal sub‑agent than a primary assistant.

---

### Comment pulse
- Anthropic fast mode ≠ weaker model → Same Opus 4.6; some argue it likely uses parallel distill-and-refine test-time compute, trading extra tokens/$ for faster, smarter answers.  
- Cerebras constraints are nuanced → Models can be sharded across chips; long pipelines raise latency, not throughput—counterpoint: heavy sharding erodes the main on-chip bandwidth advantage.  
- Batching model is oversimplified → Continuous batching means users don’t “wait for the bus” in the naive way; queueing and slot availability matter more than batch fill time.

---

### LLM perspective
- View: Fast-but-dumber modes mainly help tools and background agents; humans usually prefer fewer mistakes over raw tokens/sec.  
- Impact: API consumers must benchmark *end-to-end task time*, including error handling, not just latency or speed marketing numbers.  
- Watch next: Transparent “quality tiers,” public QPS/latency benchmarks, and clearer docs on when to route to fast submodels vs flagship models.
