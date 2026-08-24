# Beyond agentic coding

- Score: 239 | [HN](https://news.ycombinator.com/item?id=46930565) | Link: https://haskellforall.com/2026/02/beyond-agentic-coding

### TL;DR

Gabriella Gonzalez argues chat-based coding agents often fail outcome-based productivity tests, weaken codebase familiarity, and interrupt flow, so AI tooling should instead follow “calm technology”: minimize attention demands, keep developers directly in contact with code, and recede into the background. She favors next-edit suggestions and proposes semantic project navigation, automatic commit refactoring, focused file views, and alternate editable representations. Commenters especially wanted AI-generated human review plans and structure-versus-behavior commits; others preferred rapid, user-approved edits to stay mentally synchronized, while a counterview defended chat for design exploration followed by delegated execution.

### Comment pulse

- Review assistance beats review replacement → reorder files, map dependencies, and split changes so human attention lands on behavior and risk.
- Speed cannot erase desynchronization → model output may arrive instantly, but developers still need time to reconstruct its decisions.
- Chat remains useful upstream → counterpoint: conversational design can produce a solid plan before agents execute bounded work.

### LLM perspective

- View: The central interface problem is attention control, not whether an LLM can generate code.
- Impact: Toolmakers could compete on developer comprehension and calm, shifting AI from autonomous producer to peripheral cognitive aid.
- Watch next: Outcome-based trials comparing chat, next-edit, review-plan, semantic-navigation, and small-edit workflows across speed, correctness, and codebase recall.
