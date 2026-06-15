# Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model

- Score: 369 | [HN](https://news.ycombinator.com/item?id=48528371) | Link: https://github.com/nex-agi/Nex-N2/issues/4

### TL;DR
Rio de Janeiro’s IT agency released “Rio-3.5-Open-397B” as a homegrown Qwen-based LLM. Nex‑AGI analyzed the open weights and showed Rio is almost exactly a 60/40 linear merge of Nex‑N2 Pro and Qwen3.5-397B, with no evidence of extra training: the model even identifies itself as Nex when system prompts are removed. After public scrutiny, Rio’s Hugging Face page was edited to acknowledge the merge and claim an accidental upload. HN discusses model merging tech, attribution norms, and public-sector credibility.

---

### Comment pulse
- Benign-mistake view → Team meant a merge plus on‑policy distillation but mistakenly uploaded the raw 60/40 blend; virality and mayor’s boasting amplified the mess.  
- Skeptical view → Perfect 0.6/0.4 weight collinearity and delay uploading a “real” model suggest there never was extra training—counterpoint: claim is still testable.  
- Meta/technical → Thread dives into linear weight merging, linear mode connectivity, and why averaging finetunes of the same base (Qwen3.5) can preserve or boost performance.

---

### LLM perspective
- View → Open-weights ecosystems will see more “paper labs” repackaging merges; community verification becomes part of the release process.  
- Impact → Overselling government AI capabilities risks reputational damage and deepens public skepticism about funding priorities and technical competence.  
- Watch next → If Rio posts a new checkpoint, community benchmarks and weight-diff checks will show whether real distillation exists.
