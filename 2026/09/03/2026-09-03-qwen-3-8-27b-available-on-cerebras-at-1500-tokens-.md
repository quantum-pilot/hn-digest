# Qwen 3.8 27B available on Cerebras at 1500 tokens/s

- Score: 561 | [HN](https://news.ycombinator.com/item?id=49554520) | Link: https://inference-docs.cerebras.ai/models/overview

### TL;DR

Cerebras lists Qwen 3.8 27B as a public inference endpoint delivering approximately 1,500 tokens per second, with 64K context on the free tier and 128K for paid use. The model is described as original and unpruned, using selective weight-only quantization while keeping activations, attention, and KV cache at full precision. Public access is rate-limited, with dedicated endpoints offered for higher throughput and service commitments. The supplied material does not independently verify performance or quality.

### Comment pulse

- Users reported that token-per-minute limits can negate fast burst speed during sustained coding tasks.
- One commenter described high cost and an unfinished task, while another compared much cheaper completion elsewhere; both are anecdotes.
- Discussion also raised model-removal notice, billing support, local-GPU throughput, and desired OpenRouter availability.

### LLM perspective

- View: Peak generation speed is useful only when quotas, context, reliability, and pricing sustain the full workload.
- Impact: Fast bursts may improve interactive latency without improving completion time for long agentic tasks.
- Watch next: Measured sustained throughput, independent quality tests, quota transparency, and dedicated-endpoint economics.
