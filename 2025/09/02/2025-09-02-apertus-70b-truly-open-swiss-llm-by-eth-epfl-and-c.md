# Apertus 70B: Truly Open - Swiss LLM by ETH, EPFL and CSCS

- Score: 321 | [HN](https://news.ycombinator.com/item?id=45108401) | Link: https://huggingface.co/swiss-ai/Apertus-70B-2509

- TL;DR
  - Apertus is a 70B/8B Swiss LLM trained on 15T tokens with open weights, data recipes, checkpoints, and EU AI Act documentation. It enforces robots.txt-based, retroactive opt-out filtering and supports 1,811 languages, 65k-token context, and tool use. Benchmarks place 70B roughly around Llama 3.1 on general tasks, trailing in code/reasoning. HN likes the transparency and multilingual scope but flags Hugging Face gating vs “truly open,” legal nuances of opt-out/memorization claims, suggests historical robots.txt parsing, and asks about training cost.

- Comment pulse
  - robots.txt-based retroactive filtering → clear opt-out mechanism with 8% EN, 4% multi token loss — counterpoint: parse historical robots.txt to avoid over-removal.
  - ‘Truly open’ claim vs Hugging Face gating → download requires account and indemnity; users ask to remove restrictions; question reproducibility and “avoids memorization” assertions.
  - Performance parity with Llama 3.1 on general knowledge → behind on code/reasoning; trained on 4,096 GH200s; reports note Nvidia driver bugs; what did it cost?

- LLM perspective
  - View: Open data recipes plus checkpoints matter more than leaderboards; legal compliance mechanisms are becoming a differentiator.
  - Impact: If gating is removed and scripts are reproducible, Apertus becomes a strong baseline for multilingual, 65k-context, EU-compliant research and deployments.
  - Watch next: Publish training cost/energy and long-context evals; release PII output filter; consider historical robots.txt parsing and a formal reproducibility run.
