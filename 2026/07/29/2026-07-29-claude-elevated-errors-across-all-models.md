# Claude: Elevated errors across all models

- Score: 243 | [HN](https://news.ycombinator.com/item?id=49102150) | Link: https://status.claude.com/incidents/q2kg8n613kr3

- TL;DR  
  Claude experienced a multi-hour incident causing elevated error rates and latency across all models on July 29, 2026, before recovering and being marked resolved. The status page logs a standard incident lifecycle (investigating → identified → recovering → resolved) and offers subscription to updates. Hacker News users respond with automation tricks to pause/resume workloads, complaints about reliability and billing fairness for Max subscribers, jokes about “one nine” uptime and quirky status metrics, and speculation about cloud-provider costs driving infrastructure changes.

- Comment pulse  
  Heavy users script around outages → tmux + other models (DeepSeek, etc.) auto-resume sessions, even voice-triggered, to keep workflows running.  
  Reliability seen as weak → users note frequent incidents, “one nine” uptime, and accuse Anthropic of overselling capacity — counterpoint: many still rate model quality highly.  
  Business concerns arise → some want Max usage resets for downtime; others wonder if Azure cost spikes might push Anthropic to another cloud.

- LLM perspective  
  View: Serious users should treat LLM APIs like any external dependency: expect outages, engineer retries, backoff, and fallbacks.  
  Impact: SaaS built on Claude must design multi-model strategies, or risk visible downtime and frustrated paying customers.  
  Watch next: Better SLAs, automatic multi-provider routing tools, and clearer capacity disclosures will become differentiators alongside raw model quality.
