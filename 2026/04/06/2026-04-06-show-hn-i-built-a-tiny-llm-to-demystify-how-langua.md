# Show HN: I built a tiny LLM to demystify how language models work

- Score: 837 | [HN](https://news.ycombinator.com/item?id=47655408) | Link: https://github.com/arman-bd/guppylm

- TL;DR  
  GuppyLM is an 8.7M-parameter, from-scratch transformer LLM that role‑plays a fish named Guppy. It’s designed as an educational, end‑to‑end example: one Colab trains tokenizer, model, and synthetic dataset (60k fish‑tank dialogues) in about 5 minutes on a single T4 GPU. The architecture is deliberately minimal—6 layers, 384-dim, standard attention, ReLU FFN, learned positions—so students can understand and modify it. A quantized ONNX model runs fully in the browser, emphasizing transparency over capability.

- Comment pulse  
  Educational scaffold → Simple, readable code makes a good teaching OS‑style project (like Minix); students can extend capabilities and learn LLM internals—counterpoint: still needs more narrative docs.  
  Comparison curiosity → Some ask how it stacks up against Karpathy’s microGPT/minGPT; author hasn’t compared yet, others say benchmarks miss the “toy to learn” point.  
  Behavior observations → Lowercase-only training/tokenizer makes uppercase tokens unknown; responses stay in‑character, nicely illustrating how data and tokenization shape model behavior.

- LLM perspective  
  View: Ideal starter codebase for learning transformers by tinkering with real training loops, tokenizers, and deployment paths.  
  Impact: Helps students, hobbyists, and educators build intuition before touching billion-parameter systems or complex frameworks.  
  Watch next: Community forks adding multi‑turn context, richer datasets, better docs, or visualizations could evolve this into a standard teaching reference.
