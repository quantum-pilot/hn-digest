# Signal leaders warn agentic AI is an insecure, unreliable surveillance risk

- Score: 315 | [HN](https://news.ycombinator.com/item?id=46605553) | Link: https://coywolf.com/news/productivity/signal-president-and-vp-warn-agentic-ai-is-insecure-unreliable-and-a-surveillance-nightmare/

### TL;DR

Signal president Meredith Whittaker and VP Udbhav Tiwari argue that OS-level AI agents combine excessive access, insecure memory, prompt injection, and compounding probabilistic errors. Windows Recall exemplifies the risk by turning screen activity into a searchable local dossier that malware could exploit, bypassing encrypted apps. Even optimistic 95% per-step accuracy falls to about 21% across 30 steps; at 90%, it is 4.2%. They urge halted deployment, default opt-out, explicit developer opt-in, and granular auditability. HN saw both an AI flaw and an overdue operating-system security reckoning.

### Comment pulse

- Sandboxing is necessary but insufficient → capability isolation limits damage, while prompt injection still blurs trusted instructions with hostile data.
- Secure defaults impose real friction → granular permissions and zero-trust controls often fail adoption when developers must manually authorize every access.
- Signal’s absolutism fits its mission → enterprise IT balances risk and usability — counterpoint: broad desktop agents may make compromise unacceptable.

### LLM perspective

- View: Agents collapse application boundaries, so least-privilege models need task-scoped capabilities and explicit data-flow controls.
- Impact: Users and enterprises risk turning encrypted activity into centralized, malware-readable behavioral records.
- Watch next: Demand long-horizon reliability tests, injection benchmarks, revocable permissions, local processing, and independently verified telemetry guarantees.
