# LLMs Are Complicated Now

- Score: 160 | [HN](https://news.ycombinator.com/item?id=48605355) | Link: https://ianbarber.blog/2026/06/19/llms-are-complicated-now/

### TL;DR
LLMs have evolved from relatively clean transformer stacks into intricate systems: mixtures-of-experts, many attention variants, multimodal encoders, and multi-GPU execution paths. The author argues this mirrors recommendation systems: once performance becomes non-negotiable, aggressive kernel fusion and optimization make architectures harder to change and iterate on. Tooling like PyTorch FlexAttention shows a way out: design kernels and abstractions for composability and verifiability from the start. HN debates whether this shift reflects the “bitter lesson” lifecycle or sheer incumbent advantage.

---

### Comment pulse
- LLM complexity marks post–bitter-lesson phase → scaling gains slow; each small improvement now needs substantial architectural and systems engineering.  
- Incumbent-advantage view → optimized baselines hinder testing new ideas until they’re tuned too—counterpoint: software flexibility and scaling laws still permit lower-scale experiments.  
- Model comparison debate → some dislike Llama3 vs Nemotron example; others note missing features in tooling like llama.cpp as concrete evidence of rising complexity.  

---

### LLM perspective
- View: Growing modular complexity is inevitable; survival depends on abstractions that let researchers swap components without heroic kernel work.  
- Impact: Frameworks offering verifiable, high-performance templates for attention, routing, and multimodal fusion gain outsized influence over frontier and open models.  
- Watch next: generalized FlexAttention-style systems, auto-kernel generators tied to formal tests, and benchmarks comparing architecture search loops versus human-designed tweaks.
