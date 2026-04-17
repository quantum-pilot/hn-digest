# Darkbloom – Private inference on idle Macs

- Score: 468 | [HN](https://news.ycombinator.com/item?id=47788542) | Link: https://darkbloom.dev

## TL;DR
Darkbloom is a decentralized inference network that runs LLM, image, and speech models on idle Apple Silicon Macs via an OpenAI-compatible API. Users get cheaper inference (they claim ~50–70% savings) and hardware owners keep nearly all revenue, paying only electricity. The system relies on end-to-end encryption, Apple secure hardware keys, OS hardening, and attestations to argue that node operators cannot see prompts or outputs. Hacker News is intrigued by the idea but skeptical about earnings, demand, and the strength of the privacy guarantees.

## Comment pulse
- Business model skepticism → If running Macs is so profitable, the company should just buy Macs; replies cite utilization limits, capex, and “Airbnb for GPUs” style marketplace leverage.  
- Early provider experience → Install works but is flaky; models fail to load and nodes see health checks but almost no real traffic—network is demand-starved at launch.  
- Security and privacy concerns → Requiring MDM and relying on OS hardening, not true TEEs, makes “verifiable privacy” and data safety feel overstated—counterpoint: still may beat today’s centralized trust model.

## LLM perspective
- View: Technically ambitious mashup of federated-style infrastructure, Apple Silicon, and OpenAI compatibility, but trust and UX gaps are significant.  
- Impact: If they prove privacy and get real demand, they pressure hyperscaler margins and create a new “compute gig economy” for Mac owners.  
- Watch next: Independent security audits, real-world utilization/earnings data, and whether Apple exposes stronger attestation or enclave features for third parties.
