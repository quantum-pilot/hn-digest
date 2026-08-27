# BERT is just a single text diffusion step

- Score: 336 | [HN](https://news.ycombinator.com/item?id=45644328) | Link: https://nathan.rs/posts/roberta-diffusion/

### TL;DR

Nathan Barry reframes BERT-style masked language modeling as a restricted form of discrete text diffusion: BERT learns one masking regime, while a diffusion model trains across mask rates and repeatedly denoises a sequence. He fine-tunes RoBERTa on WikiText with ten masking levels, preserves a 16-token prompt, and iteratively fills and remasks a 256-token block. After 30 minutes on an H200, the proof of concept produced somewhat coherent text, though GPT-2 remained faster and more coherent. The author acknowledges earlier DiffusionBERT work.

### Comment pulse

- Readers supplied earlier generative masked-model and denoising references dating well before the experiment.
- Discussion questioned fixed-length masking and suggested insertion/deletion operations for changing sequence structure.
- Some found whole-block refinement cognitively intuitive; others noted autoregressive models also exhibit latent planning.

### LLM perspective

- View: The experiment is a clear pedagogical bridge between familiar masked models and modern discrete diffusion.
- Impact: Existing encoder weights can support generation with objective and sampling changes, albeit inefficiently here.
- Watch next: Variable-length edits, stronger baselines, scaling tests, and comparison with established diffusion methods.
