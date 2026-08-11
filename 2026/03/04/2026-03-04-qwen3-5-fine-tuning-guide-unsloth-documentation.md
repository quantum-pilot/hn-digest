# Qwen3.5 Fine-Tuning Guide – Unsloth Documentation

- Score: 251 | [HN](https://news.ycombinator.com/item?id=47246296) | Link: https://unsloth.ai/docs/models/qwen3.5/fine-tune

### TL;DR

Unsloth’s guide covers text and vision tuning across Qwen3.5 models from 0.8B through 122B, claiming 1.5× faster training and 50% less VRAM than FlashAttention 2 setups. bf16 LoRA ranges from 3GB for 0.8B to 256GB for 122B; full tuning needs roughly four times more. It requires Transformers v5, discourages 4-bit QLoRA because of quantization and BitsandBytes limitations, and explains Colab notebooks, MoE kernels, selective vision/language training, GGUF/vLLM export, OOM mitigation, and reasoning preservation. Commenters focused on data quality, rank selection, edge deployments, and fine-tuning versus RAG.

### Comment pulse

- Preserving reasoning reportedly requires at least 75% reasoning examples; incorrect chat templates or EOS settings can ruin exports.
- Commenters suggested testing multiple LoRA ranks and emphasized that curated task data matters more than fashionable training mechanics.
- Fine-tuning can specialize behavior; counterpoint: changing knowledge may be better handled through retrieval and carefully structured context.

### LLM perspective

- **View:** The guide turns a broad model family into a practical memory-budget and deployment decision tree.
- **Impact:** Smaller teams can experiment cheaply, but quantization quirks and version mismatches create deceptively fragile workflows.
- **Watch next:** vLLM compatibility, quantization quality, reproducible task gains, and whether exported models retain vision and reasoning behavior.
