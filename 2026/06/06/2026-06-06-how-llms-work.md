# How LLMs work

- Score: 837 | [HN](https://news.ycombinator.com/item?id=48389360) | Link: https://www.0xkato.xyz/how-llms-actually-work/

- TL;DR  
  The article gives a clear, math-light walkthrough of how modern transformer LLMs work: text is tokenized into IDs, mapped to embeddings, enriched with positional information (typically via RoPE), then passed through many stacked layers of multi-head attention plus feed-forward networks, all tied together by residual connections and normalization. A final linear layer and softmax produce next-token probabilities. It distinguishes shared architecture from learned weights and notes a fairly standard 2023–2025 “transformer stack,” while commenters emphasize scale, data, and forward-only generation dynamics.  

- Comment pulse  
  - Transformer LLMs are conceptually simple; frontier systems are mostly huge GPT‑2-like decoders plus tweaks, with breakthroughs driven by scale, data, RL, and compute.  
  - Autoregressive, forward-only writing pushes models to maintain coherence, causing “face-saving” hallucinations; explicit step-by-step reasoning and RL reduce this by enabling internal retries.  
  - Some argue the RoPE description is misleading and question overall accuracy—counterpoint: others view it as a solid intro and link to deeper transformer guides.  

- LLM perspective  
  - View: Understanding tokens→attention→FFN→residual stream reframes LLMs as structured matrix pipelines, making limitations like hallucinations and context issues less mysterious.  
  - Impact: Practitioners can better choose prompts, decoding settings, and model families, and reason about tradeoffs like KV cache size and MoE vs dense layers.  
  - Watch next: Track text-diffusion and state-space models, richer interpretability (head/neuron-level tools), and architectures that support iterative global editing instead of strict left-to-right generation.
