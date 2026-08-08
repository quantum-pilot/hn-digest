# Claude Code refuses requests or charges extra if your commits mention "OpenClaw"

- Score: 901 | [HN](https://news.ycombinator.com/item?id=47963204) | Link: https://twitter.com/theo/status/2049645973350363168

### TL;DR

A viral post claims Claude Code treated an empty repository differently when its latest commit contained an OpenClaw metadata string, either refusing a simple greeting or consuming extra usage. One commenter reproduced an immediate disconnect and exhausted session quota; another received an extra-usage error without the same quota jump, while others could not reproduce it or believed it was disabled. A separate user reported similar behavior when editing prose mentioning OpenClaw. The supplied material provides no Anthropic explanation, mechanism, billing record, or controlled test across accounts.

### Comment pulse

- Hidden content-triggered limits alarmed users because hostile repositories could embed markers that exhaust contributors’ quotas.
- Some inferred emergency capacity controls and poor validation — counterpoint: others viewed restricting a subscription-abusing tool as legitimate rather than censorship.
- Reliability problems and opaque product changes pushed commenters toward provider-agnostic clients, open models, or pay-per-token alternatives.

### LLM perspective

- Vendors should disclose prohibited workloads and enforce them at authentication or traffic layers.
- Usage debits need itemized, appealable records independent of generated content.
- Regression tests should cover adversarial repository text before policy filters ship.
