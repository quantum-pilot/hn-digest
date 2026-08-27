# Cerebras Code now supports GLM 4.6 at 1000 tokens/sec

- Score: 175 | [HN](https://news.ycombinator.com/item?id=45852751) | Link: https://www.cerebras.ai/code

### TL;DR

Cerebras markets GLM 4.6 inference at more than 1,000 tokens per second for AI coding, compatible with editors and agents that accept an API key. Its advertised plans range from a limited free tier to $50 Pro with 24 million daily tokens and $200 Max with 120 million. Users said the speed can keep generation in an interactive workflow, even when GLM’s output trails stronger models. Others reported API demand failures, request-rate friction, and unexpectedly rapid token consumption from repeated context transmission.

### Comment pulse

- Some users paired a frontier model for planning with fast GLM execution, trading peak quality for responsiveness.
- Experiences varied by domain: mainstream web work performed well, while specialized code demanded closer review and exposed hallucinations.

### LLM perspective

- View: Latency can matter as much as model quality when developers continuously steer and verify output.
- Impact: Extreme generation speed shifts the bottleneck toward tests, review, context costs, and service reliability.
- Watch next: Sustained throughput, prefix caching, rate-limit behavior, and quality benchmarks beyond vendor-selected coding claims.
