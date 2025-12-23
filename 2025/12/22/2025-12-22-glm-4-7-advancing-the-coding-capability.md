# GLM-4.7: Advancing the Coding Capability

- Score: 200 | [HN](https://news.ycombinator.com/item?id=46357287) | Link: https://z.ai/blog/glm-4.7

### TL;DR
GLM-4.7 is Z.ai’s new open-weight MoE coding-focused LLM (358B/32B active) targeting Claude/GPT-level agents, reasoning, and tool use. Benchmarks show solid gains over GLM-4.6 and competitiveness with GPT-5.x, Gemini 3 Pro, and Claude Sonnet on coding, τ²-Bench, BrowseComp, and math exams, especially with its interleaved/preserved “thinking” modes. It’s accessible via Z.ai/OpenRouter and for local vLLM/SGLang inference. HN users praise coding and math quality, debate local hardware viability, and suspect substantial distillation from proprietary models.

---

### Comment pulse
- Open MoE near frontier → Users report GPT-5.x / Gemini 3 Pro-level math and coding; some prefer its less stereotypically “AI” writing style.  
- Local deployment dream → Specs hint 4-bit fits on high-RAM Macs; real tests show slow tokenization and generation — counterpoint: future accelerators may change this.  
- Training sources debate → Several suspect heavy distillation from Claude/GPT, citing similar phrases; most accept this given open weights and excellent price–performance.  

---

### LLM perspective
- View: GLM-4.7 shows open MoE models can match frontier coding agents when carefully tuned for tools and multi-turn reasoning.  
- Impact: Low-cost API and open weights pressure proprietary vendors on pricing, while boosting regional ecosystems needing strong Chinese–English models.  
- Watch next: Independent agent benchmarks, real-world repo fixes, and practical local-inference setups on mid-range GPUs or emerging inference chips.
