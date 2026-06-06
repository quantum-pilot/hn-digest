# Cloudflare Flagship

- Score: 342 | [HN](https://news.ycombinator.com/item?id=48287468) | Link: https://developers.cloudflare.com/flagship/

### TL;DR
Cloudflare Flagship is a new feature flag service tightly integrated with Workers and KV, offering typed flags, targeting rules, percentage rollouts, and dashboard-based management. It implements the OpenFeature standard and ships JS SDKs so applications can evaluate flags locally, and the docs even include explicit instructions and indexes for LLM-based agents. HN discussion debates local vs edge evaluation architectures, warns against conflating flags with configuration, questions client-side token scope, and notes broader Cloudflare concerns around permissions and enterprise gating.

---

### Comment pulse
- Local in-memory evaluation of rulesets avoids network hops and enables rich context, but needs robust client engines and governance—counterpoint: some prefer simpler periodic flag-table fetches.  
- Feature flags, app config, A/B tests, and entitlements should stay distinct; SaaS flag platforms add scale, UX, and safety beyond “booleans-as-a-service.”  
- Adoption concerns: broad-scope API tokens, enterprise-only features, and coarse account permissions make teams wary of using Flagship for serious production workloads.  

---

### LLM perspective
- Embedding explicit LLM guidance and llms.txt in docs hints at Cloudflare expecting autonomous agents as first-class API consumers.  
- Flagship’s OpenFeature compatibility lowers vendor lock-in, enabling migration from LaunchDarkly/Statsig while reusing the same evaluation code.  
- Key maturity signals: app-scoped tokens, better RBAC across environments, and published performance benchmarks for local versus edge flag evaluation.
