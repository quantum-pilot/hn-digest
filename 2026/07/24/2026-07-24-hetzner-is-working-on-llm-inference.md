# Hetzner is working on LLM Inference

- Score: 144 | [HN](https://news.ycombinator.com/item?id=49033087) | Link: https://sliplane.io/blog/hetzner-inference

### TL;DR

Hetzner is testing a free, OpenAI-compatible inference API with no billing, SLA, or production guarantee. Its sole endpoint is Qwen3.6-35B-A3B-FP8, a multimodal 35B-parameter mixture-of-experts model with 3B active parameters and 262K context. One tester measured 153 ms median first-token latency and 224 output tokens/second, while noting arithmetic failures and no concurrency evidence. The larger opportunity is low-cost, EU-hosted commodity inference; Hacker News welcomed competition but said existing European providers suffer limited models, reliability, support, or sovereignty premiums, and questioned Hetzner’s capacity for larger models.

### Comment pulse

- Sovereignty demand is real but underserved → EU customers want compliant hosting without accepting weaker catalogs, poor reliability, or a regulatory price premium.
- Hetzner’s efficiency could commoditize smaller-model inference → pooled utilization may push pricing toward ordinary web hosting and simplify eventual in-house migration.
- Large-model ambitions face a hardware ceiling → the public catalog tops out at single 96GB GPUs, while desirable frontier weights need multi-GPU systems.

### LLM perspective

- **View:** OpenAI API compatibility makes provider switching cheap, so operational quality and price—not proprietary interfaces—become the defensible advantages.
- **Impact:** European startups gain a credible path from experimentation to regional deployment if model breadth and support mature.
- **Watch next:** Measure cold starts, sustained concurrency, multimodal correctness, reasoning defaults, uptime, pricing, data residency, and roadmap delivery.
