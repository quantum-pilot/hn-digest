# Claude Fable 5

- Score: 1667 | [HN](https://news.ycombinator.com/item?id=48463808) | Link: https://www.anthropic.com/news/claude-fable-5-mythos-5

### TL;DR
Anthropic’s Claude Fable 5 is a “Mythos-class” model made safe for general use, paired with Mythos 5 for vetted cyber/bio partners. It claims state‑of‑the‑art performance in long‑horizon coding, knowledge work, vision, and scientific research, with a 1M‑token context window and strong autonomous‑agent behavior. Safety classifiers aggressively route risky cyber/biology/distillation queries to Opus 4.8, plus a hidden dampening layer for frontier‑LLM development and 30‑day data retention. HN testers report big gains in complex coding and design, but also aggressive filters and worries about anticompetitive “safety.”

---

### Comment pulse
- Fable 5 is a noticeable jump for coding and design → handles large refactors, dense specs, UI work with cleaner, more surgical diffs and fewer tokens—counterpoint: still fails on some very hard, open‑ended problems.  
- Safeguards feel heavy‑handed → frequent classifier fallbacks and silent throttling on frontier‑LLM tooling make some users see “safety” as cover for entrenching Anthropic’s competitive lead.  
- Progress seems driven by scale and data, not novel architecture → new large pretrain plus rich usage traces and better GPUs, with architecture reportedly close to earlier Claude models.

---

### LLM perspective
- View: This is among the first broadly accessible models that can act as a semi‑autonomous coworker on large, messy real‑world code and research tasks.  
- Impact: Teams with huge legacy codebases, complex analytics, and scientific workflows get disproportionate leverage; small labs face new dependence on closed, policy‑mutable infrastructure.  
- Watch next: Jailbreak incidents, the scope of trusted‑access programs, how often silent LLM‑dev throttling triggers, and whether open models can close the autonomy/safety gap.
