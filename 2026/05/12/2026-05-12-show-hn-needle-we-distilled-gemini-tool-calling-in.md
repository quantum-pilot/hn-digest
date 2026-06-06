# Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

- Score: 243 | [HN](https://news.ycombinator.com/item?id=48111896) | Link: https://github.com/cactus-compute/needle

### TL;DR
Needle is a 26M-parameter “Simple Attention Network” distilled from Gemini 3.1, specialized purely for function/tool calling. It outperforms much larger open models (FunctionGemma-270M, Qwen-0.6B, Granite-350M, LFM2.5-350M) on single-shot tool selection and argument filling, while fitting into ~14MB with INT4 quantization and running at high token throughput. The repo ships an open checkpoint, data-generation pipeline, CLI, and web playground so developers can test, finetune, and embed the model in apps or devices, especially on-device assistants.

---

### Comment pulse
- Embed in CLIs → Natural-language arguments mapped to flags/subcommands by an in-binary 14MB INT4 model; great UX, but runtime/bloat if every tool does it.  
- Deploy in browsers → Interest in ONNX/WebGPU and a public playground; authors say local runs are easy, but they lack infra for a scalable hosted demo.  
- Tiny-model patterns → Builders like many constrained local agents; some confusion over 26M vs 26B naming, suggestion to label 0.026B — counterpoint: devs should read units carefully.

---

### LLM perspective
- View: Highly specialized, tiny tool-call routers can complement larger LLMs, offloading structured API selection and argument construction.  
- Impact: CLI tools, desktop apps, and wearables gain private, offline “understands-my-API” assistants without cloud calls or large dependencies.  
- Watch next: Robustness on arbitrary tool schemas, multi-step workflows, mobile/browser ports, and comparisons against other small tool-calling baselines.
