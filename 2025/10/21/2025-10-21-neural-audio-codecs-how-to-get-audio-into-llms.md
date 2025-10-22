# Neural audio codecs: how to get audio into LLMs

- Score: 322 | [HN](https://news.ycombinator.com/item?id=45655161) | Link: https://kyutai.org/next/codec-explainer

- TL;DR
  - Raw audio is far harder than text for LLMs: sequences are huge and coherence collapses. The article shows how neural audio codecs (VQ-VAE with residual vector quantization) compress speech into discrete tokens that Transformers can model. Kyutai’s Mimi adds GAN losses, RVQ dropout, and WavLM-derived semantic tokens to improve quality and let you trade semantics vs acoustics. Multi-level token scheduling is still unsettled. Bottom line: speech-native LLMs still lean on text; closing the modality gap needs better tokenization and data.

- Comment pulse
  - Pitch/emotion failure is alignment or capability? Author: capability and synthetic-data bias; users report Qwen describes voice; others show GPT tunes misrecognized.
  - Use linear-time models plus hierarchical summaries? Community notes prior hierarchical approaches (Jukebox, MiMo) and encourages exploration.
  - Why not MP3/JPEG tokens → classic codecs are CPU-cheap but compress less; neural nets dislike highly compressed inputs; formant-level cues get obscured— counterpoint: could train adapters.

- LLM perspective
  - View: Neural codecs with semantic tokens make audio continuation feasible; flattening levels hurts context and speed.
  - Impact: Better real-time voice agents; evaluations shift to prosody, emotion, and “who said what” consistency, not only word error rate.
  - Watch next: Standardize multi-level scheduling, parallel decoding, richer non-TTS training data, and benchmarks for pitch/emotion detection and cross-speaker generalization.
