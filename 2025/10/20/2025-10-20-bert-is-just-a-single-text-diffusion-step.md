# BERT is just a single text diffusion step

- Score: 336 | [HN](https://news.ycombinator.com/item?id=45644328) | Link: https://nathan.rs/posts/roberta-diffusion/

- TL;DR
  - The post shows that discrete text diffusion is essentially masked language modeling (MLM) at varying mask rates: a single MLM prediction equals one diffusion denoising step. A quick RoBERTa fine-tune with a mask schedule and iterative remasking generates 256-token blocks from a 16-token prompt—coherent but slower and weaker than GPT-2. HN notes substantial prior art tying denoising autoencoders/MLM to diffusion, debates “brain-like” generation, and suggests edit/insert operations and embedding-space noise to improve discrete diffusion.

- Comment pulse
  - This equivalence is known → 2014–2021 denoising/MLM papers and DiffusionBERT connect MLM to diffusion; masking often beats semantic-noise corruption.
  - Diffusion feels brain-like planning → people draft then refine; parallel denoising resembles edits — counterpoint: AR LLMs plan ahead in latent space too.
  - Support edit/insert/delete operations → fixed-length masking makes length changes hard; Levenshtein-like steps or expand/delete tokens can improve flexibility.

- LLM perspective
  - View: Variable-rate MLM enables non-autoregressive generation using existing BERT weights and standard tooling.
  - Impact: Potential for parallel decoding and controllable edits; today’s quality/latency still trails optimized autoregressive models.
  - Watch next: Head-to-head benchmarks, insertion/deletion tokens, embedding-noise diffusion, and throughput/latency profiling on modern accelerators.
