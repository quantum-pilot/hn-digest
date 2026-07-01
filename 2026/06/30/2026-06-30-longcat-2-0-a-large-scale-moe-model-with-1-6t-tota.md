# LongCat-2.0, a large-scale MoE model with 1.6T total and 48B Active

- Score: 268 | [HN](https://news.ycombinator.com/item?id=48727116) | Link: https://longcat.chat/blog/longcat-2.0/

### TL;DR
LongCat-2.0 is a large MoE language model (1.6T params, ~48B active) reportedly trained end‑to‑end on massive Huawei Ascend 910C ASIC clusters, sidestepping Nvidia GPUs. Commenters see that infrastructure achievement as the real headline, though some suspect it builds heavily on DeepSeek V4’s architecture/weights. Early user tests rate its answers decent but weaker than Gemini Flash and Qwen 3.7 on niche technical questions, and its refusal to discuss Mao-era deaths highlights tight Chinese political censorship. It likely powers OpenRouter’s previously “owl‑alpha” model.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Nvidia‑free training at scale → Tens of thousands of Ascend chips plus custom infra show a viable alternative hardware stack—counterpoint: details aren’t audited, could mostly reuse DeepSeek V4.

- Quality vs peers → On niche nuclear-engineering questions, users rank Gemini Flash > Qwen 3.7 > LongCat-2.0; ChatGPT variants give more nuanced, context‑aware answers.

- Alignment and politics → The model dodges questions about Mao’s death toll, confirming strong China-specific safety filters that constrain historical and political discussion.

---

### LLM perspective
- View: The main innovation is ecosystem diversification: large-scale training on Huawei ASICs proves frontier-ish models don’t require Nvidia.

- Impact: Strengthens China’s AI autonomy; pressures Nvidia and Western labs by lowering dependence on one hardware and software stack.

- Watch next: Independent benchmarks, model/card release details, and whether more open weights appear or it remains a tightly controlled commercial API.
