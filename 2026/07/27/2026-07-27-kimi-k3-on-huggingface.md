# Kimi-K3 on HuggingFace

- Score: 1301 | [HN](https://news.ycombinator.com/item?id=49065752) | Link: https://huggingface.co/moonshotai/Kimi-K3

### TL;DR
Kimi K3 is an open‑weight, 2.8T‑parameter Mixture‑of‑Experts model with native multimodality (text+vision+video), a 1M‑token context window, and quantization‑aware MXFP4 weights. Benchmarks place it roughly in the Claude/GPT frontier tier for coding, browsing and many agent tasks, though still behind top closed models in some areas. The license is “open but not free‑for‑all,” adding revenue/MAU thresholds and branding requirements. HN discussion centers on serving cost and hardware, customization potential, licensing constraints, and early third‑party hosting prices.

### Comment pulse
- Serving a 3T model is heavy: ~1.5 TB VRAM or multi‑TB RAM; MXFP4 helps, but costs only reveal marginal inference, not training subsidies.  
- Biggest upside is custom fine‑tuning and IP sovereignty on frontier‑class weights—tempered by license clauses for >$20M revenue and 100M+ MAU requiring agreements/branding.  
- Hardware is ill‑shaped for individuals: tiny‑VRAM consumer GPUs vs power‑hungry datacenter cards; VRAM used for price discrimination; shared hardware is efficient but hard to fully trust.

### LLM perspective
- View: K3 shows that “frontier‑ish” multimodal agents can now be open‑weight, but under business‑friendly, not community‑friendly, terms.  
- Impact: Startups and researchers gain a high‑end base for agents/coding with on‑prem options; true hobbyist local use stays unrealistic.  
- Watch next: Distilled K3 variants, real‑world $/M‑token from providers, and whether prosumer‑class high‑VRAM hardware or co‑op inference services emerge.
