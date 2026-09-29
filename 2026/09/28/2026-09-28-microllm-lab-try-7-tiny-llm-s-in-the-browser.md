# MicroLLM Lab – Try 7 tiny LLM's in the browser

- Score: 272 | [HN](https://news.ycombinator.com/item?id=49882781) | Link: https://stateofutopia.com/experiments/microllmlab/

### TL;DR

MicroLLM Lab offers seven Q4-quantized models from 25.8M to 362M parameters for browser-local chat, benchmarking, comparison, and custom evaluation. It uses WebGPU where available, with WASM and JavaScript fallbacks, and stores downloaded weights in IndexedDB. The site claims private, low-latency inference without accounts or server cost, but supplies no independent tests for those claims. Commenters found the experiment technically interesting while reporting dense UI, Firefox/Linux compatibility trouble, repetition, incorrect arithmetic, and poor answers to ordinary prompts.

### Comment pulse

- Running seven models locally is the main achievement → commenters valued the WebGPU demonstration more than the models’ practical reasoning quality.
- Tiny models failed simple tasks → users reported unusable recipes, repeated phrases, wrong arithmetic, and inconsistent built-in benchmark results.
- Presentation obscured experimentation → dense explanatory copy and small text delayed access, prompting the creator to revise layout and fallbacks.

### LLM perspective

- View: This is a useful browser-inference laboratory, not evidence that tiny general-purpose models are broadly capable.
- Impact: Developers can measure device compatibility and identify narrow routing or classification tasks without transmitting prompts to a server.
- Watch next: Publish reproducible per-model accuracy, latency, memory, fallback, browser, and hardware results against clearly scoped use cases.
