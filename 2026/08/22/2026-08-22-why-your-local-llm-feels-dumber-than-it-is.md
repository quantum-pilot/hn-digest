# Why your local LLM feels dumber than it is

- Score: 285 | [HN](https://news.ycombinator.com/item?id=49402232) | Link: https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917

### TL;DR

Local model quality depends on the entire inference stack, not just weights: sampler and chat-template settings, hardware math, attention backend, kernels, and weight or KV-cache quantization can shift token probabilities. On one roughly 100,000-token Qwen3.6-27B workload, attention backends diverged in content-dependent clusters; quantized KV caches produced a reproducible tool-call failure, and two 4-bit-weight variants botched calls that BF16, FP8, and INT8 completed. These controlled results show divergence, not universal intelligence rankings. Discussion supplied vivid anecdotes but no shared configuration or workload for comparison.

### Comment pulse

- Readers reported the same 27B family succeeding on 8GB gaming hardware yet failing on 48GB Macs, often under different harnesses.
- Several blamed deployment mistakes such as disabled thinking or bad samplers—counterpoint: others achieved strong local results with minimal setup.
- Speed, heat, context limits, and hardware requirements remained practical constraints even when private local inference proved useful.

### LLM perspective

- View: Fidelity is a systems-engineering property, not a label attached solely to a downloaded checkpoint.
- Impact: Operators may misjudge models, break tool use, or trust misleading quantization claims when implementations differ silently.
- Watch next: Multiple prompts and GPUs, unconstrained generations, task-level benchmarks, disclosed KLD methods, same-weight kernel comparisons, and long-context tool reliability.
