# Project Glasswing: An Initial Update

- Score: 268 | [HN](https://news.ycombinator.com/item?id=48240419) | Link: https://www.anthropic.com/research/glasswing-initial-update

- TL;DR  
  - Anthropic’s Project Glasswing is using its unreleased Mythos Preview model with ~50 major partners to scan critical and open‑source software, already surfacing over 10k high‑severity vulnerabilities in private systems and thousands more in OSS, with independently validated true‑positive rates far above typical tools. The new bottleneck is human triage and patch rollout, not discovery. Anthropic is keeping Mythos private for now, offering safer tools like Claude Security and scanning harnesses, while HN debates hype, comparables, and access.

- Comment pulse  
  - Users report Codex/Claude‑style scanners finding many real bugs and targeted patches, quickly becoming essential—counterpoint: others worry about verbose, unnecessary “safety” code from LLMs.  
  - Some cite curl’s maintainer, who saw little Mythos advantage over existing tools; others note curl’s hardening and limited access, pointing to Firefox and AISI benchmarks.  
  - Debate over Mythos hype: some see genuinely higher true‑positive rates and strategic, possibly US‑only access; skeptics compare to GPT‑2‑style “too dangerous” marketing and replicable data.

- LLM perspective  
  - View: Mythos‑class models shift security from “finding bugs” scarcity to “humans fixing and shipping patches” scarcity, stressing governance and staffing.  
  - Impact: Teams already disciplined with CI, static analysis, and fast patch pipelines benefit most; laggards risk overwhelming backlogs of unremediated vulnerabilities.  
  - Watch next: Track independent benchmarks, patch‑latency metrics, and any government mandates tying procurement to AI‑assisted security audits of critical software.
