# Google releases Gemma 4 open models

- Score: 1046 | [HN](https://news.ycombinator.com/item?id=47616361) | Link: https://deepmind.google/models/gemma/gemma-4/

## TL;DR
Gemma 4 is Google DeepMind’s new line of open-weight models built on Gemini 3 tech, spanning tiny E2B/E4B variants for phones and IoT up to 26B and 31B for “local-first” workstation servers. They’re multimodal (text, vision, audio), support function calling and agentic workflows, and target high “intelligence-per-parameter.” Benchmarks show the 26B/31B models approaching or matching strong open/closed baselines on coding, math, multilingual QA, and tool-use. HN users report excellent local coding and image-generation performance (especially 26B), fast community quantizations, but mixed small-model quality and some confusion around “thinking” traces and tool integration.

---

## Comment pulse
- Community quantizations ship immediately → Unsloth GGUF builds make Gemma 4 usable on consumer GPUs/CPUs; users report robust pipelines (OCR, multilingual land-record search) and strong coding assistance.
- Quality scales sharply with size → 2B/4B give weak images; 26B produces best-in-class “pelican” tests on laptops; some 31B local runs appear broken—counterpoint: instruction-tuned variants work better.
- Benchmarks vs Qwen 3.5 debated → 26B/31B look roughly competitive with Qwen mid/large on many tasks, but Gemma smalls lag; ELO/TAU2 discrepancies spark concerns about cherry-picked or misread scores.

---

## LLM perspective
- View: Gemma 4 meaningfully raises the ceiling for open, locally runnable models, especially in the 20–30B range with multimodal + agentic features.
- Impact: Strong new default for offline dev tools, IDE copilots, and sovereign deployments where Gemini API or OpenAI can’t be used.
- Watch next: 4-bit QAT releases, better small-model variants, mature agent harnesses for safe real tool execution beyond “hallucinated” scripts and fake thinking traces.
