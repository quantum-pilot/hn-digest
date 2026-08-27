# Heretic: Automatic censorship removal for language models

- Score: 372 | [HN](https://news.ycombinator.com/item?id=45945587) | Link: https://github.com/p-e-w/heretic

### TL;DR

Heretic is an AGPL tool that automatically alters supported transformer models to suppress refusals without full post-training. It identifies refusal directions, ablates selected attention and MLP projections, and uses Optuna to minimize refusals alongside divergence from the original model. The project reports 3 refusals per 100 harmful prompts and lower KL divergence than two comparison models on Gemma 3 12B, but these are author-provided metrics. Commenters praised user control and optimization while sharply disputing the ethics of enabling explicitly harmful requests.

### Comment pulse

- Supporters framed refusal removal as intellectual autonomy → they objected to model creators imposing moral boundaries.
- Dataset examples exposed concrete dual-use risk → prompts include self-harm, child abuse, hacking, drugs, and confidential-data theft.
- Automated tuning attracted technical interest → Optuna searches for lower refusal without excessive model drift.

### LLM perspective

- View: Heretic makes alignment removal accessible while reducing neither the resulting capability risks nor operator responsibility.
- Impact: Model owners gain control, but abuse barriers become easier to remove without specialized transformer expertise.
- Watch next: Independently evaluate capability retention, harmful-output rates, dataset licensing, architecture coverage, and quantization sensitivity.
