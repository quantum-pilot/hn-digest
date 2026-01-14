# Signal leaders warn agentic AI is an insecure, unreliable surveillance risk

- Score: 315 | [HN](https://news.ycombinator.com/item?id=46605553) | Link: https://coywolf.com/news/productivity/signal-president-and-vp-warn-agentic-ai-is-insecure-unreliable-and-a-surveillance-nightmare/

- TL;DR
  - Signal’s Meredith Whittaker and Udbhav Tiwari warn that OS-level “agentic AI” like Windows Recall effectively creates a searchable, malware-exploitable log of users’ entire digital lives, bypassing end‑to‑end encryption and enabling pervasive surveillance. They argue today’s agents are probabilistic systems whose accuracy collapses over multi-step tasks, making real autonomy unsafe. They call for pausing reckless deployments, making participation opt‑in, and enforcing radical transparency. HN commenters dispute whether the core flaw lies in legacy OS security or in fundamentally untrustworthy LLM-based agents.

- Comment pulse
  - Root cause is weak OS security → agents expose old sandboxing failures — counterpoint: LLMs are unsecurable, so integration itself introduces distinct AI-driven risks.
  - Signal must prioritize privacy above usability → their stance suits messaging, while enterprises juggle productivity gains against poorly understood agent risks and IT governance constraints.
  - Recall-style total logging seen as surveillance risk → some propose opt-in, local-only, task-specific recorders; skeptics argue verifiable privacy impossible without on-device models and stronger regulation.

- LLM perspective
  - View: Treat general-purpose agents as high-risk infrastructure, demanding certification, logs, and constraints similar to payments or identity providers.
  - Impact: OS vendors must redesign permission models; enterprises limit agents to narrow workflows with audited tools rather than desktop-wide autonomy.
  - Watch next: Benchmarks for multi-step reliability, threat models for agent logging, and crypto guarantees for local or federated private inference.
