# Kimi Linear: An Expressive, Efficient Attention Architecture (2025)

- Score: 266 | [HN](https://news.ycombinator.com/item?id=49082022) | Link: https://arxiv.org/abs/2510.26692

## TL;DR
Kimi Linear introduces Kimi Delta Attention, a gated, RNN-like linear attention module combined with a chunkwise, hardware-efficient Diagonal‑Plus‑Low‑Rank transition scheme. In a 3B-activated, 48B-total-parameter model, it outperforms full Multi-Head Latent Attention on short- and long-context and RL-scaling tasks, while cutting KV cache usage by up to 75% and delivering 6× faster 1M-token decoding. HN discussion ranges over “emergent” scaling behavior, relations to Gated DeltaNet2/LSTMs and K3, and the role of distillation vs. genuine innovation.

## Comment pulse
- Large models show abilities at scale → Bitter Lesson: more compute plus generic search/learning beats clever algorithms — counterpoint: capabilities may follow smooth scaling laws.  
- Practitioners report Gated DeltaNet2 as even more expressive than Kimi Linear; some see these gated state-space blocks as revisiting classic LSTM-style recurrent architectures.  
- Kimi’s open-sourced kernels and checkpoints impress many; others argue its success mixes real innovation with possible training-data distillation, which some view as normal knowledge transfer.  

## LLM perspective
- View: Strong linear attention plus gated state makes RNN-style architectures competitive again for frontier-scale, long-context language and multimodal models.  
- Impact: Inference providers can serve million-token contexts cheaper; open-source checkpoints let smaller labs replicate results without massive KV-cache infrastructure.  
- Watch next: Head-to-head benchmarks with FlashAttention models, scaling beyond 48B parameters, and whether major labs adopt Kimi-style kernels.
