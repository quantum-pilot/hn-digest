# Transformers Explained Visually

- Score: 584 | [HN](https://news.ycombinator.com/item?id=49792342) | Link: https://poloclub.github.io/transformer-explainer/

### TL;DR

An interactive GPT-2 Small walkthrough follows text generation from tokenization and 768-value embeddings through 12 transformer blocks, multi-head self-attention, MLPs, logits, and sampling. It explains how queries and keys produce attention weights over values, while residual connections and normalization stabilize processing. HN readers praise the visualization, especially attention as an input-dependent layer, but request more explanation of why transformers beat alternatives. Critics also flag “safety” as a misleading description of low-temperature sampling and question emphasizing dropout in modern models.

### Comment pulse

- Attention dynamically constructs computation from input → query-key scores become weights applied to value vectors during inference.
- Transformers won through scalable efficiency → distant tokens exchange information directly and training parallelizes better than recurrent alternatives.
- Some teaching choices mislead → temperature trades predictability for variation, not safety, while dropout is less central in newer recipes.

### LLM perspective

- View: The visualization explains mechanics effectively, while architectural motivation still requires comparison against recurrent and convolutional models.
- Impact: Learners gain a concrete path from tokens to probabilities without treating transformer generation as magic.
- Watch next: Add side-by-side complexity, memory, and information-path comparisons with RNNs, CNNs, and newer architectures.
