# DeepSeek-v3.2: Pushing the frontier of open large language models [pdf]

- Score: 491 | [HN](https://news.ycombinator.com/item?id=46108780) | Link: https://huggingface.co/deepseek-ai/DeepSeek-V3.2/resolve/main/assets/paper.pdf

### TL;DR

DeepSeek presents V3.2 as an efficient open model combining sparse attention, expanded reinforcement learning, and synthesized agent training. DeepSeek Sparse Attention selects 2,048 key-value tokens per query within a 128K context, reducing core attention scaling while preserving reported long-context quality. Post-training compute exceeded 10% of pre-training cost, and 1,827 synthesized environments broadened tool use. The authors report reasoning performance comparable to GPT-5 and stronger results from a high-compute Speciale variant, but also acknowledge weaker world knowledge and poorer token efficiency than leading proprietary models.

### Comment pulse

- Readers welcomed public methods and competitive open weights → skeptics questioned how cost-effectiveness can be judged without complete economics.
- Competitive models may commoditize raw capability → hosting, energy, trust, integration, and user experience could still sustain commercial services.
- Consumer deployment remains difficult because the model’s scale exceeds ordinary single-GPU systems.

### LLM perspective

- View: Sparse inference and agent-data synthesis matter more than benchmark rank because they target deployment cost and tool generalization.
- Impact: Open-model providers gain a stronger base, while proprietary vendors must differentiate through systems rather than model access alone.
- Watch next: Independent evaluations should test cost, long-context recall, tool reliability, contamination, and output-token efficiency.
