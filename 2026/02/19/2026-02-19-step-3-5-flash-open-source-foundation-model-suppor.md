# Step 3.5 Flash – Open-source foundation model, supports deep reasoning at speed

- Score: 209 | [HN](https://news.ycombinator.com/item?id=47069179) | Link: https://static.stepfun.com/blog/step-3.5-flash/

### TL;DR

StepFun released Step 3.5 Flash, an open-source 196-billion-parameter sparse mixture-of-experts model that activates 11 billion parameters per token. It combines a 256,000-token context window, sliding and full attention, and three-token prediction; StepFun reports 100–300 tokens per second in typical use and up to 350 on Hopper GPUs. Company benchmarks include 74.4% on SWE-bench Verified and 51% on Terminal-Bench 2.0. Quantized builds fit roughly 128 GB systems, but StepFun acknowledges long reasoning traces and instability under specialized or extended interactions.

### Comment pulse

- Local testers praise context efficiency, Mac speed, and usable coding-agent performance — counterpoint: others report hallucinations, infinite reasoning loops, and tool-call incompatibilities.
- Commenters caution that a 51% benchmark score cannot prove unwavering stability and that agent harness choices materially affect results.
- Hardware economics remain uncertain: four-bit quantization needs roughly 112–116 GB, prompting comparisons with paid hosted coding services.

### LLM perspective

- **View:** Its distinguishing feature is efficient local agentic inference, not unqualified parity with proprietary models.
- **Impact:** High-memory workstation owners gain a private coding model with long context and strong reported throughput.
- **Watch next:** Independent benchmarks, loop fixes, quantization quality, harness compatibility, and real-world hallucination rates.
