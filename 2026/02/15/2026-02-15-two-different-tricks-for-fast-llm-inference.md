# Two different tricks for fast LLM inference

- Score: 157 | [HN](https://news.ycombinator.com/item?id=47022329) | Link: https://www.seangoedecke.com/fast-llm-inference/

### TL;DR

Anthropic and OpenAI reach faster coding inference through different trade-offs. Anthropic serves unchanged Opus 4.6 at about 170 tokens per second versus 65, prioritizing latency over cost efficiency. OpenAI's Cerebras-backed Codex Spark exceeds 1,000 tokens per second but is a distinct, less reliable model than GPT-5.3-Codex. The author attributes Anthropic's gain to smaller batches and Spark's to wafer-scale SRAM, while explicitly acknowledging uncertainty and corrections: continuous batching complicates the analogy, and large models can be sharded across multiple Cerebras chips.

### Comment pulse

- Low batching is plausible but unconfirmed → counterpoint: commenters proposed parallel refinement or routing to newer hardware.
- Single-chip capacity is not Spark's ceiling → Cerebras already serves roughly 355B-parameter models by sharding across wafers.
- Speed helps only when errors stay low → extra tool mistakes can cost users more time than slower generation.

### LLM perspective

- **View:** Tokens per second, first-token latency, quality, price, and aggregate throughput require joint evaluation.
- **Impact:** Fast small models may become internal primitives for routing, search, and routine agent operations.
- **Watch next:** Independent quality benchmarks, queue latency, batch sizes, hardware topology, error-adjusted completion time, and serving economics.
