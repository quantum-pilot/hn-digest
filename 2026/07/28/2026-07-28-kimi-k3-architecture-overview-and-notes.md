# Kimi K3 Architecture Overview and Notes

- Score: 281 | [HN](https://news.ycombinator.com/item?id=49085698) | Link: https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html

### TL;DR

Kimi K3 scales the 48B Kimi Linear design to 2.8T parameters, reportedly the largest open-weight model at release, with an emphasis on inference efficiency. LatentMoE compresses expert layers; multi-head latent attention and Kimi Delta Attention replace conventional attention. Attention residuals link layers for 4% more training and 2% more inference cost. K3 also replaces RoPE with NoPE everywhere and adds native multimodality. HN discussion explored how causal masking and recurrent decay may encode position implicitly, praised the explanation, and treated the architecture as evidence of engineering beyond distillation.

### Comment pulse

- Novelty counters distillation narratives → readers viewed LatentMoE, attention residuals, and all-NoPE design as substantive original engineering regardless of any teacher-model use.
- NoPE surprised readers → causal masking can expose order implicitly, while recurrent or decaying linear-attention states encode relative position without explicit embeddings.
- Presentation earned unusual praise → readers found Raschka’s concise, direct architecture notes easier to trust than generic AI-generated summaries.

### LLM perspective

- View: K3’s design shows frontier scaling increasingly depends on composing multiple targeted efficiency mechanisms rather than one dominant architectural breakthrough.
- Impact: Inference implementers must support hybrid attention, compressed experts, residual routing, and NoPE instead of assuming a standard transformer stack.
- Watch next: Validate latency, memory, long-context behavior, multimodal quality, and whether attention residual gains justify their recurring inference overhead.
