# MacBook M5 Pro and Qwen3.5 = Local AI Security System

- Score: 152 | [HN](https://news.ycombinator.com/item?id=47457107) | Link: https://www.sharpai.org/benchmark/

### TL;DR

A self-published home-security benchmark reports that quantized Qwen3.5-9B scored 90 of 96 text tests on a 64 GB M5 Pro MacBook, versus 94 for GPT-5.4 and 92 for GPT-5.4-mini. Using llama.cpp, it produced about 25 tokens per second, reached first token in 765 milliseconds, and occupied 13.8 GB. The suite covers classification, deduplication, tool calls, structured output, privacy, reasoning, routing, and prompt injection. HN readers welcomed offline ownership but questioned synthetic fixtures, simple tasks, and the lack of independent validation.

### Comment pulse

- Critics called model selection cherry-picked and suggested task-specific small vision models could suit the application better.
- The author said costly new hardware is unnecessary; a used M2 Mini with 16 GB can run the stack.
- Larger Qwen variants scored no better, which readers said may reveal task fit rather than general capability.

### LLM perspective

- **View:** Local AI wins when bounded workloads reward privacy and predictable cost over frontier breadth.
- **Impact:** Commodity Apple Silicon could support useful private automation without continuous cloud inference.
- **Watch next:** Replication on real camera streams, measuring accuracy, latency, and energy together.
