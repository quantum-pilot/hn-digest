# Agent Skills

- Score: 348 | [HN](https://news.ycombinator.com/item?id=46871173) | Link: https://agentskills.io/home

- TL;DR  
  Agent Skills is an open standard for packaging reusable “skills” as folders containing instructions, code, and resources that LLM agents can discover and load on demand. The goal is to turn organizational know‑how and workflows into portable, version‑controlled capabilities that work across multiple agent products. Hacker News discussion splits between viewing skills as glorified documentation versus genuinely new infrastructure for semi‑deterministic workflows, with debate over how much standardization is needed and whether future, stronger models will render such formats temporary.

- Comment pulse  
  - Skills are just good documentation in folders; stronger models and larger context may make special formats unnecessary — counterpoint: small benchmarks show measurable coding gains.  
  - Teams succeeding treat skills as explicit, reusable workflows or subroutines invoked via CLI or slash commands, not vague best‑practice guides buried in context.  
  - Debate over standardizing skill directories (.agent/skills, XDG‑style config) versus avoiding premature lock‑in while tools still experiment with discovery mechanisms.

- LLM perspective  
  - View: This pattern approximates software engineering for agents—encapsulated behaviors, explicit triggers, and composable “functions” instead of ad‑hoc mega‑prompts.  
  - Impact: Most value likely in enterprises needing auditable workflows, consistent style/tooling, and cross‑vendor portability for agent‑assisted development.  
  - Watch next: A/B tests versus plain READMEs, standardized discovery metadata, and automatic skill routing based on filetypes, repos, or roles.
