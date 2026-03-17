# Leanstral: Open-Source foundation for trustworthy vibe-coding

- Score: 233 | [HN](https://news.ycombinator.com/item?id=47404796) | Link: https://mistral.ai/news/leanstral

- TL;DR  
Leanstral is Mistral’s open-source coding agent specialized for Lean 4, aiming to move from “vibe coding” to formally verified code. Trained on realistic math and spec repositories, it uses Lean as an automatic checker and focuses on efficiency: a sparse 6B-parameter expert model that rivals much larger systems on their new FLTEval benchmark. Case studies show it debugging Lean version breakages and proving program properties. HN discusses the cost–quality trade-off versus Claude Opus and the broader value of alternative alignment strategies.

- Comment pulse  
  - Benchmarks feel muddled: Haiku comparisons seem irrelevant, and Leanstral still trails Opus, though pass counts and lower costs complicate the picture.  
  - Some argue that for formal verification tasks, paying more for the highest-quality model is justified—counterpoint: open, cheaper Lean-specialists may matter where budgets dominate.  
  - Others see Leanstral as proof-of-concept for agentic workflows: models generating tests, reproducing bugs, then using proof assistants to enforce correctness.

- LLM perspective  
  - View: Specialized proof agents plus auto-verifiers look like a scalable pattern for critical software and math, beyond general chat models.  
  - Impact: Could make Lean practical for more teams, automating proof search while humans focus on specs and architecture.  
  - Watch next: independent FLTEval replications, comparisons with Codex-like tools, and whether similar agents emerge for Coq, Isabelle, Rust verification frameworks.
