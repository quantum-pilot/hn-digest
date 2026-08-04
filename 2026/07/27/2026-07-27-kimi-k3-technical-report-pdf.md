# Kimi-K3 Technical Report [pdf]

- Score: 361 | [HN](https://news.ycombinator.com/item?id=49070985) | Link: https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf

### TL;DR

Kimi K3 is a 2.8-trillion-parameter mixture-of-experts model activating 104 billion parameters per token, with native vision and a 1-million-token context. Kimi Delta Attention, Attention Residuals, and 16-of-896 expert routing reportedly deliver 2.5× Kimi K2’s scaling efficiency; multi-domain reinforcement learning targets long agentic work. Released weights accompany benchmark results that generally trail Claude Fable 5 and GPT-5.6 Sol but lead evaluated alternatives. HN discussion focused less on scores than self-hosting economics, infrastructure demands, and commercial license restrictions.

### Comment pulse

- At sufficient scale, owning hardware may slash token costs → commenters estimated strong savings and privacy — counterpoint: staffing, power, cooling, and colocation add substantially.
- The release’s openness is contested → weights and infrastructure are downloadable, but large service operators face separate-agreement and attribution clauses.
- Technical details drew curiosity → readers highlighted the self-expanding knowledge graph and SiTU-GLU’s bounded tanh-sigmoid construction.

### LLM perspective

- **View:** Sparse scale shifts the frontier from parameter count toward orchestration: routing, cache management, persistent sandboxes, and workload scheduling.
- **Impact:** Organizations with sustained, private workloads gain negotiating leverage, while smaller teams remain dependent on hosted inference.
- **Watch next:** Verify million-token quality, real hardware utilization, total operating cost, license enforcement, and independent replications of benchmark claims.
