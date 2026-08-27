# Z.ai confirms Ox Alpha is a new GLM-series model and will release its weights

- Score: 417 | [HN](https://news.ycombinator.com/item?id=49446422) | Link: https://www.bloomberg.com/news/articles/2026-08-26/china-s-z-ai-made-ox-alpha-stealth-model-that-rivals-deepseek

### TL;DR

Z.ai confirmed that the free, high-usage stealth model Ox Alpha is a new GLM-series model and said its weights would be released that night. The brief report supplied no architecture or size details. HN’s hands-on reports were sharply mixed: some placed its coding between Sonnet and Opus or ran multi-day autonomous experiments, while others saw repeated command loops, network failures, or scores below much smaller models. Commenters emphasized that harness behavior, quantization, run variance, and questionable unofficial benchmarks confound model comparisons.

### Comment pulse

- Coding quality looked useful but uneven → some sustained complex work, while repeated shell-command loops made unattended agents unsafe.
- Benchmark claims conflict dramatically → scores ranged below Nano to above Fable, with unofficial sites and sponsorship undermining confidence.
- Public-test behavior appeared to change → possible explanations included quantization experiments, normal pass-at-K variance, or a new reinforcement-learning checkpoint.

### LLM perspective

- View: Open weights will make Ox Alpha testable; until then, stealth endpoints entangle model capability with changing serving configurations.
- Impact: Developers may gain another capable local model, but automation needs loop detection and execution limits regardless of benchmark rank.
- Watch next: Verify parameter count, license, quantization sensitivity, harness-controlled evaluations, long-horizon reliability, and reproducible weights-versus-hosted behavior.
