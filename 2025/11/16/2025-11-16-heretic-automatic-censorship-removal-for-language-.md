# Heretic: Automatic censorship removal for language models

- Score: 372 | [HN](https://news.ycombinator.com/item?id=45945587) | Link: https://github.com/p-e-w/heretic

- TL;DR
    - Heretic automates “decensoring” of LLMs via directional ablation, using Optuna to minimize refusals while keeping low KL divergence to preserve capabilities. Example: Gemma-3-12B-IT drops from 97/100 to 3/100 refusals with 0.16 KL, rivaling manual ablations. Works on many dense/MoE models; ~45 minutes for an 8B model on an RTX 3090. HN debates ethics (autonomy vs guardrails), dataset quality/licensing and robustness, quantization effects, and Optuna’s practicality; the author advises prioritizing KL<1 and notes classifier quirks.

- Comment pulse
    - Automatic decensoring preserves user autonomy and diversity → alignment embeds vendor morals into tools. — counterpoint: dataset includes extreme illegal/self-harm prompts; guardrails address real risks.
    - Optuna hyperparameter search accelerates ablation tuning → better refusal/quality trade-offs; author advises choosing KL<1 and notes CoT refusal monologues can mislead the classifier.
    - Practical quirks matter → higher-precision quantization (Q8_0) uncensors where Q4 fails; dataset licensing and generalization to stronger models remain open concerns.

- LLM perspective
    - View: Automating directional ablation lowers the barrier to alignment research and misuse; no finetuning costs, minutes to deploy per model.
    - Impact: Open-weight ecosystems face faster churn of uncensored forks; vendors may respond with architectural changes, watermarking, or encrypted weight distribution.
    - Watch next: Independent benchmarks across families, robustness against RLAIF/SFT variants, and legal/policy reactions to shipping or hosting decensored derivatives.
