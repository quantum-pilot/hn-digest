# Mistral Medium 3.5

- Score: 409 | [HN](https://news.ycombinator.com/item?id=47949642) | Link: https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5

### TL;DR

Mistral Medium 3.5 is a 128B dense, 256k-context open-weight model combining reasoning, instruction following, vision, and coding, with configurable effort and a claimed 77.6% SWE-Bench Verified score. It now defaults in Le Chat and Vibe, powers parallel cloud coding agents and Work mode, can reportedly self-host on four GPUs, and costs $1.50/$7.50 per million API input/output tokens. Hacker News welcomed a credible European alternative and its size-to-quality tradeoff, but questioned benchmark comparisons and whether 4-bit local deployments retain quality or run fast enough against sparse competitors.

### Comment pulse

- A 70GB Q4 model technically fits premium unified-memory machines — counterpoint: reports near 3 tokens/second make cloud inference more practical.
- Dense weights preserve capability but impose bandwidth costs; commenters asked why Mistral moved away from the MoE approach it helped popularize.
- Model and national diversity improve buyer leverage, even if Medium 3.5 trails the frontier on absolute performance.

### LLM perspective

- **View:** The release optimizes for deployable control and acceptable quality rather than benchmark leadership.
- **Impact:** Enterprises gain another self-hostable or hosted agent backend with visible tool execution and approval gates.
- **Watch next:** Independent quantization tests, sustained agent runs, vision quality, tokens per second, and total serving cost.
