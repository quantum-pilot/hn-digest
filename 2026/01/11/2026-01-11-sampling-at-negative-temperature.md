# Sampling at negative temperature

- Score: 98 | [HN](https://news.ycombinator.com/item?id=46579374) | Link: https://cavendishlabs.org/blog/negative-temperature/

### TL;DR

Language-model temperature mirrors the Boltzmann distribution: positive values flatten or sharpen token probabilities, while a negative value reverses their ranking. After modifying llama.cpp, sampling LLaMA near zero from below repeatedly selected the least likely tokens, producing persistent multilingual fragments and anomalous tokens near the embedding-space centroid rather than ordinary random text. HN readers liked the mechanistic demonstration but questioned whether it reveals meaningful anti-language or numerical noise, distinguished sampling temperature from physical thermodynamics, and proposed experiments involving perplexity, constrained vocabularies, dynamic temperature control, and training on negatively sampled text.

### Comment pulse

- Mechanism → near-zero negative temperature chooses minimum-logit tokens; farther negative values remain random but weight unlikely tokens.
- Interpretation → anomalous centroid tokens may expose weak representations — counterpoint: minimum logits may primarily reflect numerical noise, not meaningful opposites.
- Extensions → commenters suggest temperature-perplexity comparisons, human-text measurement, model-controlled sampling, constrained vocabularies, and retraining experiments.

### LLM perspective

- View: Negative sampling is a diagnostic of probability tails, not a practical route to coherent creativity.
- Impact: Researchers gain a simple probe for anomalous tokens and embedding weaknesses, while generation quality collapses.
- Watch next: Test precision sensitivity, vocabulary constraints, model scale, and whether tail tokens remain stable across checkpoints.
