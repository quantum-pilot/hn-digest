# Train Your Own LLM from Scratch

- Score: 419 | [HN](https://news.ycombinator.com/item?id=48017948) | Link: https://github.com/angelos-p/llm-from-scratch

### TL;DR
A GitHub workshop walks you through implementing every part of a small GPT-style language model from scratch: tokenizer, transformer blocks, training loop, and text generation. It targets a ~10M-parameter character-level model trained on Shakespeare that can finish in under an hour on a laptop (CPU, CUDA, or Apple MPS). The docs are structured as progressive exercises, echoing Karpathy’s nanoGPT but scaled down. HN commenters add deeper courses, alternative “from scratch” books, and reflections on real-world GPU needs.

---

### Comment pulse
- Use this as a gentle intro → Stanford’s CS336 then deepens theory, scaling laws, and systems-level optimization—counterpoint: access to lectures/materials can be unclear for outsiders.  
- Many parallel “from scratch” paths → Raschka’s LLMs-from-scratch book and PyTorch notebook series provide similar end-to-end builds with more math and detailed derivations.  
- DIY training is illuminating, not trivial → past ULMFiT/Wikipedia projects on consumer GPUs showed it’s fun and educational, but serious models demand lots of compute and careful engineering.

---

### LLM perspective
- View: This is an educational pipeline, not a production stack; its value is demystifying transformers via hands-on coding.  
- Impact: Best suited for students, indie devs, and engineers wanting intuition before using larger frameworks or hosted APIs.  
- Watch next: Community forks adding BPE, larger datasets, and benchmarks; course-style integrations; comparisons against nanoGPT and Raschka implementations.
