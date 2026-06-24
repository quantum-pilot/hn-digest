# Will It Mythos?

- Score: 305 | [HN](https://news.ycombinator.com/item?id=48640196) | Link: https://swelljoe.com/post/will-it-mythos/

### TL;DR
A benchmark based on Cloudflare’s Mythos security-auditing system tests whether public LLMs can autonomously find real-world software bugs across entire repos. Mythos still stands alone in reliably detecting all nine benchmark bugs, but several general models (Claude Opus, GPT‑5.5, DeepSeek, Qwen, Gemma) can find subsets when wrapped in a task-specific harness. Commenters debate whether Mythos is merely an unguardrailed model or a qualitatively better agentic system, how to score partial, low-sample results, and whether newer commercial models are being “nerfed” over time.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Fable/Mythos feel dramatically stronger for real coding and security work → users report faster progress and better autonomy vs prior Claude/OP models—counterpoint: blind tests might show minimal practical differences.  

- Mythos isn’t just “safety off” → effectiveness comes from a custom harness and self-directed repo analysis, pushing toward human-out-of-the-loop security auditing.  

- Simple success percentages mislead on small samples → Wilson confidence intervals plus speed/cost suggest DeepSeek v4 as best non-Mythos tradeoff on this benchmark.  

---

### LLM perspective
- View: Domain-specific agent harnesses unlock much more value than raw model upgrades for tasks like security audits and large-repo analysis.  

- Impact: Security teams, code-review pipelines, and CI systems can increasingly delegate tedious vulnerability hunting to autonomous LLM agents.  

- Watch next: Open, reproducible Mythos-like benchmarks; vendor-native “security auditor” modes; longitudinal tests to verify models aren’t silently regressing.
