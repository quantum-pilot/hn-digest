# Google Titans architecture, helping AI have long-term memory

- Score: 363 | [HN](https://news.ycombinator.com/item?id=46181231) | Link: https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/

- TL;DR  
Titans is a new sequence model that adds a deep neural long‑term memory alongside attention, updating its own weights during inference using a “surprise” signal derived from gradients. MIRAS is the unifying theory framing transformers, RNNs, and new Titans‑style models as associative memories with explicit choices of memory architecture, objective, retention, and optimizer, extending beyond standard MSE/dot‑product. Experiments show Titans beating strong baselines and even GPT‑4 on extreme long‑context tasks. HN reactions mix excitement with concerns about openness and robustness.  

- Comment pulse  
  - Google’s publication is praised, but others note Meta, DeepSeek, Bytedance also publish heavily; lack of Titans code/weights undermines Google’s “openness” edge.  
  - Surprise‑driven memory invites worries about poisoning with random junk; replies argue training teaches the model to down‑weight irrelevant tokens, but curated streams remain dangerous.  
  - Several see Titans as a major step toward more human‑like, persistent AI; others lament no public pretrained models and encourage more high‑level conceptual writing.  

- LLM perspective  
  - View: Online‑updating deep memory could replace huge prompts and brittle RAG for long‑running assistants and agents.  
  - Impact: Best suited to domains needing months‑scale context—large codebases, scientific projects, logs, genomics—if inference‑time learning is made stable.  
  - Watch next: Open Titans‑style releases, standardized >1M‑token benchmarks, and safety/privacy protocols for models that change weights during user interactions.
