# Qwen3.8-Flash-Next

- Score: 611 | [HN](https://news.ycombinator.com/item?id=49448210) | Link: https://qwen.ai/blog?id=qwen3.8-flash-next

### TL;DR

Alibaba open-sourced Qwen3.8-Flash-Next, a multimodal 125B-parameter mixture-of-experts model activating 6B per token, plus 51B host-offloadable n-gram embeddings. Its Qwen4-preview architecture combines compressed Gated DeltaNet memory, micro-block sparse attention, four gated residual branches, and Muon optimization. Native context is 262,144 tokens, extendable to one million; QwenCloud charges $0.16/$0.47 per million input/output tokens. HN focused on fitting quantized variants into 128GB systems, promising 12-token/s early tests, and whether its strong reported agent benchmarks survive independent use.

### Comment pulse

- N-gram embeddings trade memory for cheap factual lookup → tables can page from RAM or SSD while only 6B backbone parameters activate.
- Consumer 128GB systems may run practical quants → early DGX Spark tests reached roughly 12-token/s decode, though prefill and context growth remain constraints.
- Benchmark gains suggest strong efficiency → Flash-Next often beats 27B and 397B relatives — counterpoint: quantization can visibly degrade generated output.

### LLM perspective

- View: Separating slow lookup memory from active computation creates a credible new scaling axis for affordable local models.
- Impact: Developers gain stronger agentic capability on unified-memory hardware, while serving stacks must master paging, sparse attention, and speculative decoding.
- Watch next: Verify community quant quality, llama.cpp support, long-context retrieval, MTP gains, and independent coding benchmarks across 128GB machines.
