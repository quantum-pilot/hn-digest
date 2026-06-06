# GPT-5.5 Price Increase: What It Costs

- Score: 193 | [HN](https://news.ycombinator.com/item?id=48057209) | Link: https://openrouter.ai/announcements/gpt55-cost-analysis

### TL;DR
OpenRouter analyzed real usage from users who switched from GPT‑5.4 to GPT‑5.5. Although OpenAI doubled token prices, GPT‑5.5 only shortens completions for very long prompts (10k+ tokens) and is actually more verbose for 2k–10k-token inputs. Net effect: average cost per million tokens rose 49–92% across prompt sizes, with the smallest prompts hit hardest. Hacker News discussion argues that cost-per-token is incomplete; what matters is cost per completed task, turns required, and quality gains in coding and reasoning.

---

### Comment pulse
- Cost per task beats cost per token → some see GPT‑5.5 as ~1.5–2x pricier but only worth it at highest reasoning tiers.  
- Methodology skeptics → token-level, per-request analysis ignores turns, task boundaries, and distribution plots—counterpoint: still useful as a first-order pricing sanity check.  
- Quality vs plateau → some see 5.5 as a clear leap in “just doing the task,” others report regressions, bottleneck vibes, and overfocus on coding/agents.

---

### LLM perspective
- View: Token prices doubled while real costs rose ~1.5–2x, not 2x+, due to modest verbosity changes.  
- Impact: Teams with many short prompts or chatty workflows get hit hardest; long-context power users are cushioned slightly.  
- Watch next: Independent cost-per-task benchmarks and multi-model agent evaluations will drive provider choice more than raw token pricing tables.
