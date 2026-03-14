# Can I run AI locally?

- Score: 854 | [HN](https://news.ycombinator.com/item?id=47363754) | Link: https://www.canirun.ai/

### TL;DR
CanIRun.ai is a browser-based tool that guesses which open-weight AI models your hardware can run, using memory size/bandwidth and a curated catalog from llama.cpp, Ollama, and LM Studio. It helps non-experts navigate dense vs Mixture-of-Experts architectures, quantization options, and context lengths. HN users like the idea but note that MoE performance, context choices, and personal speed/quality tradeoffs make predictions approximate. Many still rely on trial-and-error or CLI tools like llmfit, especially for serious coding or research workflows.

---

### Comment pulse
- Small local models are great for embedded tools and extraction → Qwen 3.5 9B strongly recommended; fits long context on modest GPUs — counterpoint: reports of heavy hallucinations and flaky tool use.  

- Site’s estimates miss MoE nuances → speed depends on active parameters and context; real tok/s can exceed predictions and differs between prefill and generation, especially with speculative decoding.  

- Users want “best model for my hardware and constraints” → quality, tok/s thresholds, and task type matter; people still mix heuristics, llmfit, and cloud models to converge.  

---

### LLM perspective
- View: Tools like CanIRun.ai are early attempts at a “compatibility layer” between messy hardware realities and exploding model catalogs.  

- Impact: Power users, tinkerers, and small teams gain faster shortlist generation, but serious deployments still need hands-on benchmarking.  

- Watch next: Expect standardized quality scores, hardware profiles, and IDE/CLI integration that auto-pick and tune local models per task.
