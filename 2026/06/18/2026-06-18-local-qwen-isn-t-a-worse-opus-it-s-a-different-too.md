# Local Qwen isn't a worse Opus, it's a different tool

- Score: 445 | [HN](https://news.ycombinator.com/item?id=48580209) | Link: https://blog.alexellis.io/local-ai-is-not-opus/

### TL;DR

A $12,000 RTX 6000 running Qwen 3.6 27B cannot replace Claude or Codex, but paid for itself after private telemetry exposed 4–5× license underpayment. Local models proved useful for air-gapped support, codebase explanation, and tightly scoped maintenance while offering fixed costs and vendor independence. Long unsupervised tasks triggered loops, hallucinations, arithmetic errors, and ignored instructions; quantization and harness choices mattered, while serving added access, metering, routing, and power operations. HN agreed models need workload-specific evaluation, though hardware and future capability remain contested.

### Comment pulse

- Prompting resembles instrument tuning → users described Claude, GPT, and Qwen responding to different structures — counterpoint: unstable outputs may make such recipes post-hoc superstition.
- Local often means portable open weights → models can stay on-device or move among independent hosts, reducing lock-in beyond strict air-gapping.
- Serving-stack conclusions depend on workload → vLLM favors concurrent batching; llama.cpp delivered faster startup and single-user generation in the author’s tests.

### LLM perspective

- **View:** Sovereignty is the product; model quality only needs to clear a task-specific threshold that cloud use cannot safely cross.
- **Impact:** Teams inherit infrastructure engineering and supervision in exchange for predictable access, controlled data, and uncapped private inference.
- **Watch next:** Test repeated runs on real tasks; record loop rate, intervention time, correctness, energy, concurrency, and total operator cost.
