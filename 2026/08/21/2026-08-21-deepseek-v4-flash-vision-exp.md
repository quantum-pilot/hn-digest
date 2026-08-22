# DeepSeek-v4-flash-vision-exp

- Score: 489 | [HN](https://news.ycombinator.com/item?id=49386163) | Link: https://api-docs.deepseek.com/guides/vision/

### TL;DR

DeepSeek’s experimental V4 Flash Vision accepts JPEG, PNG, GIF, and WebP through base64, public URLs, or uploaded file IDs across OpenAI-compatible Chat Completions and Responses APIs plus an Anthropic-compatible endpoint. Images are resized to roughly 800×800 pixels at the high end and capped at 384 tokens each; requests allow up to 600 images within size limits. Comments welcomed screenshot support but warned that downscaling constrains OCR. Informal clock tests produced mixed initial results and strong repeat performance, underscoring evaluation variance.

### Comment pulse

- Predictable token costs appealed to users → the 384-token ceiling supports cheap multi-image workflows, but sacrifices fine detail.
- Native vision fixes an agent failure mode → earlier text-only versions reportedly attempted improvised pixel analysis when given screenshots.
- Clock-test debate cautioned against single anecdotes → one failure contrasted with nine successes across ten fresh sessions and an ambiguous image.

### LLM perspective

- View: Broad API compatibility and bounded image cost are attractive, while forced resizing defines a significant detail ceiling.
- Impact: Coding agents can inspect screenshots directly; document OCR and dense charts may still require tiling or another model.
- Watch next: Standard vision benchmarks, OCR accuracy, text-model parity, latency, real pricing, configurable resolution, and promotion beyond experimental status.
