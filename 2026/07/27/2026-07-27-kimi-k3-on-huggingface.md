# Kimi-K3 on HuggingFace

- Score: 1301 | [HN](https://news.ycombinator.com/item?id=49065752) | Link: https://huggingface.co/moonshotai/Kimi-K3

### TL;DR

Moonshot AI released weights for Kimi K3, a native multimodal mixture-of-experts model with 2.8 trillion total parameters, 104 billion active per token, and a one-million-token context window. It combines Kimi Delta Attention, gated latent attention, 896 experts, and quantization-aware MXFP4 weights for coding, reasoning, vision, and long-horizon agents. Published benchmarks place it near leading closed models across many tasks. Commenters celebrate fine-tuning and data sovereignty, but estimate roughly 1.5TB of VRAM just for weights and flag commercial license thresholds that limit unrestricted service use.

### Comment pulse

- Customization outweighs headline price → startups can fine-tune frontier-scale weights on proprietary data, preserving IP control unavailable with closed APIs.
- Open weights are not home-accessible → native MXFP4 still needs about 1.5TB VRAM — counterpoint: slow multi-terabyte CPU servers may suit unattended jobs.
- The license is source-available, not permissionless → model-service businesses above $20 million annual revenue need a separate agreement; large products face branding rules.

### LLM perspective

- View: Weight availability shifts the frontier from API access to infrastructure access; openness now depends on capital and licensing.
- Impact: Independent labs gain inspectability and adaptation, while shared inference providers remain the practical route for most users.
- Watch next: Compare third-party token prices, sustained latency, fine-tuning recipes, quantization loss, license enforcement, and independent benchmark reproduction.
