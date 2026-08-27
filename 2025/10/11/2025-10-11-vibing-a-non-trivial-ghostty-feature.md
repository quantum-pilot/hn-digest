# Vibing a non-trivial Ghostty feature

- Score: 246 | [HN](https://news.ycombinator.com/item?id=45549434) | Link: https://mitchellh.com/writing/non-trivial-vibing

### TL;DR

Mitchell Hashimoto documents 16 AI-assisted sessions used to ship unobtrusive macOS update notifications in Ghostty, costing $15.98 and roughly eight hours of his time. He began with human research and a scoped UI plan, used agents for prototypes, mechanical refactors, simulations, integration, and reviews, and repeatedly intervened when they produced architectural mistakes or failed on title-bar layout. Some generated work was discarded entirely; manual restructuring made later prompts succeed. His central rule is expert supervision: understand, clean up, test, and manually review every AI-written change before shipping.

### Comment pulse

- Readers valued agents for overcoming blank-page friction, though others find initial design the most rewarding part of programming.
- Several distinguished this reviewed, domain-expert workflow from unsupervised “vibe coding” and highlighted the unusually transparent session record.

### LLM perspective

- View: The case demonstrates iterative delegation with human architectural ownership, not autonomous feature development.
- Impact: Agents can accelerate prototypes and tedious edits while failures still demand expertise, restraint, and cleanup.
- Watch next: Maintainability after release, defect rates, reproducibility for less-expert users, and total review effort.
