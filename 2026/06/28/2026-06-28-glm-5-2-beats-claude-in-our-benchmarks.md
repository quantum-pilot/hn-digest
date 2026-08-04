# GLM 5.2 beats Claude in our benchmarks

- Score: 343 | [HN](https://news.ycombinator.com/item?id=48709670) | Link: https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/

### TL;DR

On Semgrep’s IDOR benchmark, GLM 5.2 reached 39% F1 with a minimal Pydantic harness, versus a reported 32% aggregate for Claude Code, at about $0.17 per true vulnerability. Semgrep’s endpoint-aware multimodal harness still led at 53–61%, reinforcing that repository navigation and context selection can matter more than model choice. The MIT-licensed weights enable private deployment, though training data remain closed. HN users praised GLM’s hosted cost and daily coding quality, but independent security tests favored other open models and warned that one dataset, run, and harness cannot establish general superiority.

### Comment pulse

- Task rankings are unstable → another benchmark found DeepSeek V4 Pro stronger and MiMo 2.5 Pro initially lucky, emphasizing repeated trials across vulnerability classes.
- Tools can reduce performance → simply exposing open-source Semgrep made no tested model better; effective harnesses must pre-process findings instead of adding tool-learning burden.
- Open weights do not mean cheap local inference → full-size hardware may cost $80,000–$100,000 — counterpoint: hosted and quantized options make usage inexpensive.

### LLM perspective

- **View:** The benchmark’s strongest result is architectural: targeted context delivery produces larger gains than swapping capable base models.
- **Impact:** Security teams can route tasks among models by vulnerability class, privacy requirements, latency, and cost instead of standardizing prematurely.
- **Watch next:** Repeat seeded cross-class runs, isolate protected answers, and report precision, recall, variance, tokens, latency, and harness ablations.
