# Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms

- Score: 558 | [HN](https://news.ycombinator.com/item?id=49883844) | Link: https://github.com/firelex/jeff

### TL;DR

Jeff is an open family of 0.8B–2B models that returns calibrated probabilities over described options in one forward pass, using Jev’s request format. The project reports 22 ms decisions on an RTX PRO 6000 and 28 ms on an M4 Max for the 0.8B model. Its 79.1% five-benchmark score approaches Jev’s published 83.0%, but samples and timing hardware differ, reasoning-heavy tasks remain much weaker, prompts strongly affect results, and game performance diverges from benchmark rank. Domain fine-tuning can greatly improve narrow tasks.

### Comment pulse

- Small decision models can replace generative calls → classification needs probabilities and choices, not text generation or parsing.
- Reported averages hide workload variance → one commenter measured 70% versus Jev’s 94% on job-ad labels.
- Fine-tuning can close narrow gaps → the project reports voice-navigation accuracy rising from 31.7% to 95.8% with roughly 11,000 examples.

### LLM perspective

- View: Jeff demonstrates efficient local classification, not Jev-equivalent general reasoning or universally superior accuracy.
- Impact: Teams can trade broad zero-shot robustness for speed, privacy, open weights, and application-specific training.
- Watch next: Same-sample comparisons, identical-hardware latency, independent calibration tests, multilingual support, and domain fine-tune reproducibility.
