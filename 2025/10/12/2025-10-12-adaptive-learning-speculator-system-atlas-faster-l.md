# AdapTive-LeArning Speculator System (ATLAS): Faster LLM inference

- Score: 189 | [HN](https://news.ycombinator.com/item?id=45556474) | Link: https://www.together.ai/blog/adaptive-learning-speculator-system-atlas

### TL;DR

Together AI presents ATLAS, a speculative-decoding system combining a broad static draft model, a lightweight draft model that learns from live traffic, and a confidence controller selecting the model and lookahead. The company reports up to 501 tokens per second for fully adapted DeepSeek-V3.1 on four B200 GPUs at batch size one, versus 105 for its FP8 baseline. It also claims adaptation reduced an RL training pipeline’s total time by over 60%. These are vendor benchmarks under specified workloads, not general guarantees.

### Comment pulse

- Readers questioned provider-level tool-call quality, while noting speculative decoding itself is intended to preserve the target model’s output distribution.
- Several compared drafting and verification to branch prediction: useful when accepted guesses outweigh miss costs.

### LLM perspective

- View: Runtime adaptation addresses workload drift that makes fixed speculative models lose acceptance over time.
- Impact: Latency-sensitive inference and RL rollouts could gain substantially without retraining the target model.
- Watch next: Independent benchmarks across diverse traffic, cold starts, adaptation overhead, and provider-level correctness.
