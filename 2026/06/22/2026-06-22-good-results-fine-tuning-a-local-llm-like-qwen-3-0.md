# Good results fine tuning a local LLM like Qwen 3:0.6B to categorize questions

- Score: 203 | [HN](https://news.ycombinator.com/item?id=48623434) | Link: https://www.teachmecoolstuff.com/viewarticle/fine-tuning-a-local-llm-to-categorize-questions

- TL;DR
    - A hobbyist built a household Q&A chatbot and fine‑tuned tiny Qwen‑3 0.6B locally to classify questions into ~18 categories, raising accuracy from 10% (prompt‑only) to 79%, then 92% by mapping categories to opaque two‑letter codes instead of natural labels. This demonstrates that small LLMs can be effective local classifiers with ~850 examples and Unsloth/QLoRA, though overlapping concepts (e.g., pool vs. water heater) still confuse it. HN commenters argue simpler classifiers or constrained decoding might solve this more efficiently.

- Comment pulse
    - LLM fine-tuning feels overkill; n-gram or logistic/SGD classifiers are tiny, fast, and likely match performance — counterpoint: if Qwen fits needs, that's acceptable.
    - Others propose exploring small encoders, synthetic data, GRPO/GEPA tuning, and embedding-plus-classifier pipelines to learn modern LLM training and evaluation techniques.
    - Several note the "invented categories" issue could vanish by using grammar-constrained decoding or logit masking, forcing outputs to valid labels only.

- LLM perspective
    - Fine-tuning tiny LLMs as classifiers works, but classical ML baselines and constrained decoding should be systematically compared.
    - Pattern — LLMs used where simpler tools suffice — suggests need for decision checklists in hobby and production ML projects.
    - Benchmark Qwen 0.6B codes-vs-labels against logistic regression, small transformers, and grammar-constrained decoding on the same datasets.
