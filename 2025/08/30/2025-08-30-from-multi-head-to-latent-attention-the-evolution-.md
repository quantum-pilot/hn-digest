# From multi-head to latent attention: The evolution of attention mechanisms

- Score: 174 | [HN](https://news.ycombinator.com/item?id=45072160) | Link: https://vinithavn.medium.com/from-multi-head-to-latent-attention-the-evolution-of-attention-mechanisms-64e3c0505f24

- TL;DR
    - Explains attention variants for decoder-style transformers: MHA (per-head KV, quadratic cost), MQA (shared KV), GQA (KV per head-group), and MHLA (projects KV into a low-rank latent cache with up/down projections). MHLA trains like MHA but infers like MQA, targeting MHA-level quality with far less memory; cited in DeepSeek. HN debates the 2017 paper’s title/impact, whether “frontier” models use these (training advances drive most gains; architecture tweaks aid scaling), and offers Medium paywall workarounds.

- Comment pulse
    - They didn’t foresee dominance → Built for non-recurrent translation; later scaling/hardware unlocked impact — counterpoint: attention is local/brittle; new architectures needed.
    - Frontier use is modest → Open models show gains from training (data, objectives); GQA/MHLA mainly cut KV memory; Grok 2 uses standard MHA+MoE.
    - Medium paywall tips → Use freedium.cfd, close the interstitial, or disable JavaScript.

- LLM perspective
    - View: MHLA reframes KV as a compressed latent with up/down projections, enabling head-agnostic cache reuse at inference.
    - Impact: Longer contexts on single GPUs, cheaper serving; possible quality regressions on tasks needing head-specific KV diversity.
    - Watch next: Benchmarks: tokens/s, latency, perplexity vs MHA/GQA; kernels for on-the-fly projections; integration with paged KV and FlashAttention.
