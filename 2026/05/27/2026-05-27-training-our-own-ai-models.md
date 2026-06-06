# Training our own AI models

- Score: 190 | [HN](https://news.ycombinator.com/item?id=48296359) | Link: https://posthog.com/blog/training-ai-models

- TL;DR  
  PostHog’s CEO announces they’ll start training in-house AI models on customer product-usage data to power features like scalable session-replay analysis, synthetic user testing, and behavior prediction. EU-cloud and contract-constrained customers are excluded by default; everyone else on US cloud is auto-enrolled with an org-level opt-out. Data will be anonymized and not shared with external model providers. Hacker News discussion centers on the “opt‑in by default” framing, user consent, and loss of trust in SaaS analytics.

- Comment pulse  
  - “Opt‑in by default” is seen as dishonest → users argue this is simply opt‑out, undermining claims of valuing consent and transparency.  
  - Long-time fans feel bait‑and‑switched → PostHog’s AI pivot and auto-enrollment push teams to uninstall it and prefer self-hosted or simpler analytics.  
  - Some shrug and plan to opt out → appreciate explicit notices but question legality (GDPR, Article 13) and robustness of PostHog’s “anonymization” promises.

- LLM perspective  
  - View: PostHog is trading short-term training data volume against long-term trust; analytics tools are especially sensitive because they see end-user behavior.  
  - Impact: Expect more teams to self-host or minimize analytics vendors; vendors that default to no training may gain disproportionate goodwill.  
  - Watch next: Watch whether PostHog ships compelling AI features users actually want; adoption vs churn will reveal if the opt-out gamble succeeded.
