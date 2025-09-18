# A postmortem of three recent issues

- Score: 263 | [HN](https://news.ycombinator.com/item?id=45281139) | Link: https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues

TL;DR
Anthropic traced August–September Claude degradations to three overlapping infra issues: misrouting short-context requests to 1M‑context servers (amplified by sticky routing), a TPU misconfiguration corrupting token probabilities, and an XLA:TPU approximate top‑k miscompilation triggered by a precision rewrite. Fixes: corrected routing, rollback plus character‑anomaly tests, switch to exact top‑k with fp32 standardization, and work with XLA on a compiler fix; plus tighter, production evals and better debugging. HN applauds transparency but flags reliability, privacy consent on feedback, and possible short‑context performance penalties on long‑context stacks.

Comment pulse
- Reliability feels shaky → status page shows incidents; users report slowdowns; providers often under-report outages. — counterpoint: some prioritize model quality over uptime today.
- Consent on feedback sharing is unclear → thumbs-down may send entire conversation; Anthropic says the modal warns explicitly and asks for better copy suggestions.
- Weird-language tokens stem from inference bugs → human-written sampling/XLA kernels and precision/top‑k errors can mis-rank probabilities, selecting out-of-place tokens.

LLM perspective
- View: Heterogeneous inference stacks hide coupled failure modes; quality monitoring must catch precision/sampling regressions before load-balancing amplifies them.
- Impact: Most affected: Sonnet 4, Haiku 3.5, Opus; coding agents suffered; third-party platforms spared except routing; trust/privacy expectations tightened.
- Watch next: Upstream XLA fix and Bedrock rollout completion; production quality dashboards; benchmarks comparing 1M‑context vs short‑context performance (e.g., RoPE scaling impacts).
