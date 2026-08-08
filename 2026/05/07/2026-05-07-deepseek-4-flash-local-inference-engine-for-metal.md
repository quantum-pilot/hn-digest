# DeepSeek 4 Flash local inference engine for Metal

- Score: 260 | [HN](https://news.ycombinator.com/item?id=48050751) | Link: https://github.com/antirez/ds4

### TL;DR

`ds4.c` is an alpha, Metal-only inference engine built specifically for DeepSeek V4 Flash rather than as a general GGUF runtime. It pairs custom 2-bit or 4-bit weights with official-logit validation, OpenAI- and Anthropic-compatible APIs, agent integrations, and persistent disk KV checkpoints so long prompts can be reused across sessions. The 2-bit model targets Macs with 128GB RAM; published single-run M3 Max results reached 26.68 generated tokens per second on a short prompt. The authors openly credit llama.cpp/GGML and disclose strong GPT-5.5 assistance.

### Comment pulse

- Readers liked model–hardware specialization for compact, hackable systems — counterpoint: mature runtimes already optimize kernels, and model churn makes bespoke engines disposable.
- Long-context prefill remained the practical bottleneck; disk checkpoints help repeated sessions but not an unrelated large first prompt.
- Energy discussion admired a reported 50-watt MacBook peak while questioning whether centralized inference remains more efficient per user.

### LLM perspective

- Co-designing quantization, templates, cache semantics, and agent protocols can improve end-to-end reliability.
- Comparisons need equal quantization, context, sampling settings, output quality, and broader-runtime baselines.
- Serialized inference limits concurrent throughput even when single-user generation is acceptable.
