# Lambda Calculus Benchmark for AI

- Score: 128 | [HN](https://news.ycombinator.com/item?id=47900506) | Link: https://victortaelin.github.io/lambench/

### TL;DR
LamBench is a new benchmark of 120 pure lambda‑calculus programming tasks where models must implement algorithms in a minimal “Lamb” language and pass hidden tests. Frontier closed models (GPT‑5.4, Claude Opus 4.6, Gemini 3.1 Pro) cluster near ~90% solved, while popular open or cheaper models lag well behind. Discussion says this undercuts “Opus killer” hype, notes odd regressions in newer model releases, and questions single‑shot methodology and opaque model/run configurations.

---

### Comment pulse
- Top models cluster; open/local “opus killers” lag → hype exceeds reality; Opus mainly helps on hardest tasks — counterpoint: cheaper “almost opus” suits many users.  
- Single-shot, one-sample scoring misrepresents stochastic LLMs → critics want multiple attempts per task and clearer details on quantization, prompts, and run settings.  
- Pure lambda-calculus tasks expose weaknesses in algorithmic reasoning → encodings make array-like FFT logic costly; models can’t just copy typical mutable-array implementations.  

---

### LLM perspective
- View: This benchmark probes compositional reasoning beyond usual coding tests, but needs multi-sample curves and transparent configs to be decision-grade.  
- Impact: Could guide selection of premium APIs versus cheaper local models for algorithm-heavy workloads, if rerun rigorously and expanded to more languages/tasks.  
- Watch next: results for Mistral and other strong open models, plus variants benchmarking interaction combinators or richer type systems, not just pure lambdas.
