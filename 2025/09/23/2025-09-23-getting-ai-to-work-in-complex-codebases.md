# Getting AI to work in complex codebases

- Score: 194 | [HN](https://news.ycombinator.com/item?id=45347532) | Link: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md

### TL;DR

The captured source contains GitHub navigation but not the linked article’s body, so the discussion supplies the usable substance. Commenters describe a context-engineering workflow for complex codebases: research the repository, ask clarifying questions, write detailed plans and tests, critique them, then let a coding agent execute bounded tasks. They repeatedly stress human review because automated critiques can invent problems and agents may loop or miss edge cases. Several see engineering shifting toward specifying and verifying behavior, while noting observed legacy behavior can exceed written specifications.

### Comment pulse

- Structured planning improves reliability → staged research, questions, specs, and task files constrain agents before implementation begins.
- Human judgment remains essential → generated critiques can be wrong, and tests may omit clients’ reliance on undocumented behavior.
- Simpler architecture helps agents → vertical patterns and clear documentation reduce steering for repeated feature work.

### LLM perspective

- View: Context engineering works by converting tacit repository knowledge into reviewable constraints, not by eliminating supervision.
- Impact: Developers spend less effort on implementation details and more on specifications, edge cases, and verification.
- Watch next: Measure plan-review time, escaped regressions, undocumented compatibility breaks, and correction rates across repositories.
