# How to run Qwen 3.5 locally

- Score: 442 | [HN](https://news.ycombinator.com/item?id=47292522) | Link: https://unsloth.ai/docs/models/qwen3.5

### TL;DR

Unsloth’s guide maps Qwen3.5 models from 0.8B to 397B parameters onto local hardware, recommending updated Dynamic 2.0 GGUF quantizations through llama.cpp or LM Studio. Four-bit memory needs range from about 3.5 GB for the smallest models to 214 GB for 397B; the 27B and 35B-A3B variants need 17 GB and 22 GB. It also documents thinking-mode parameters, 256K context, tool calling, and server integration. Commenters reported impressive consumer-hardware speed, but warned that long-context agentic work remains much harder than short prompts.

### Comment pulse

- A 9B model reached about 100 tokens per second on a 16 GB RTX 5070 Ti, impressing users for Q&A.
- Coding reports diverged sharply — counterpoint: small models needed handholding, while larger 27B or 35B variants satisfied some developers.
- Quant naming remains confusing; users wanted concrete hardware, context, speed, memory, and quality profiles instead of isolated benchmark scores.

### LLM perspective

- **View:** Model size, quantization, context depth, and orchestration jointly determine usefulness; headline throughput alone is misleading.
- **Impact:** Consumer GPUs can host capable private assistants, but serious agentic coding still pushes memory and latency.
- **Watch next:** Long-context benchmarks, llama.cpp fixes, and standardized configuration profiles across common hardware.
