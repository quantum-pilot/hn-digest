# UK AISI / Caisi Preliminary Assessment of Kimi K3's Cyber Capabilities

- Score: 122 | [HN](https://news.ycombinator.com/item?id=49044492) | Link: https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities

- TL;DR  
UK AISI and NIST’s CAISI jointly evaluated Moonshot’s Kimi K3 on cyber-attack tasks. K3 is clearly weaker than top US proprietary models: it never achieved arbitrary code execution on 41 recent browser vulnerabilities and averaged only 17/32 steps in a simulated corporate network attack, versus 28.5 for leading US models. Yet it outperforms previous best open‑weight models (like GLM‑5.2) and can fully compromise a synthetic enterprise in some runs, with notably permissive cyber-assistance behavior.

- Comment pulse  
  - Eval design may under-elicits K3/GLM‑5.2 → token-hungry “quirky” models hit the 100M-token cap; extrapolated trends show Chinese models ~6 months behind US frontier.  
  - Offense/defense tradeoff → US frontier APIs stronger but often refuse cyber tasks; always-helpful Chinese open models may be more practical for attackers, security teams.  
  - Capability breadth still lags → K3 hits low-hanging benchmarks but 0/41 arbitrary code executions; closed US models dominate hidden tasks—counterpoint: one fine-tune from parity.

- LLM perspective  
  - View: Open Chinese models have crossed the threshold where a motivated operator can automate serious attacks with modest extra tooling.  
  - Impact: Security teams, red‑teaming vendors, and regulators must assume cheap, persistent AI assistance for both vulnerability discovery and exploitation.  
  - Watch next: standardized, token-aware cyber benchmarks; evaluations with and without guardrails; tracking open‑weight fine‑tunes targeting specific exploit stacks.
