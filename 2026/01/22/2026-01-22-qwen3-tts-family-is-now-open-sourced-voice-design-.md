# Qwen3-TTS family is now open sourced: Voice design, clone, and generation

- Score: 439 | [HN](https://news.ycombinator.com/item?id=46719229) | Link: https://qwen.ai/blog?id=qwen3tts-0115

### TL;DR

Qwen released 1.7B- and 0.6B-parameter speech models for ten languages, covering natural-language voice design, nine preset timbres, three-second cloning, streaming, and reconstruction. Its 12Hz multi-codebook tokenizer and Dual-Track architecture claim first audio after one character and latency as low as 97ms; published evaluations report strong WER, speaker similarity, and instruction control. HN users ran models locally, praised cloning quality, found 0.6B viable on older GPUs, but reported erratic emotion, noise leakage, slow inference without FlashAttention, and serious impersonation risks.

### Comment pulse

- Local access → macOS and GTX 1080 users ran models, though downloads, memory limits, and acceleration materially affected speed.
- Quality → cloning often preserved timbre impressively, but long-form chunks could become monotonous, laugh, moan, or inherit background noise.
- Dual use → readers imagined audiobooks and audio restoration while warning that effortless voice impersonation strengthens scams.

### LLM perspective

- View: Open weights turn advanced voice synthesis into deployable infrastructure, while reliability still trails polished demonstrations.
- Impact: Creators gain inexpensive multilingual production; verification systems must increasingly treat unauthenticated audio as untrusted.
- Watch next: Real-time factors by hardware, long-form consistency, controllable prosody, watermarking, and consent safeguards.
