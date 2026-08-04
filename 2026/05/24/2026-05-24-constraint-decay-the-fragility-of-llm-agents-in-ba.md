# Constraint Decay: The Fragility of LLM Agents in Back End Code Generation

- Score: 156 | [HN](https://news.ycombinator.com/item?id=48256912) | Link: https://arxiv.org/abs/2605.06445

### TL;DR

A study of 100 backend tasks across eight web frameworks finds that coding agents lose reliability as architectural, database, and ORM constraints accumulate, even when the API contract stays fixed. Strong configurations dropped about 30 assertion-pass-rate points from baseline to fully specified tasks; weaker ones neared zero. Flask fared better than convention-heavy FastAPI and Django, with data-layer defects leading failures. HN commenters found the pattern familiar but cautioned that limited frontier-model testing weakens exact comparisons, and argued that early constraints, examples, automated checks, and repeated review can mitigate decay.

### Comment pulse

- More acceptance criteria mechanically raise failure odds — counterpoint: commenters still considered joint behavioral-and-architectural degradation an important distinct signal.
- Agents can anchor on an initial architecture; later corrections are resisted or quietly undermined, while repeated patterns calcify through context.
- Production users reported 5–10 review-and-fix cycles, using specs, tests, linters, runners, and orchestration rather than trusting one generation pass.

### LLM perspective

- View: Constraint adherence is a compositional reliability problem; individually high pass rates multiply into low whole-system success.
- Impact: Teams must budget architecture validation separately from endpoint testing, especially around ORM queries and runtime behavior.
- Watch next: Replicate with current frontier models, equalized reasoning budgets, mature codebases, and constraint-aware scaffolding.
