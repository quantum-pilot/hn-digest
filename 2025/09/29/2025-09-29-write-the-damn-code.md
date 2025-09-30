# Write the damn code

- Score: 198 | [HN](https://news.ycombinator.com/item?id=45415232) | Link: https://antonz.org/write-code/

- TL;DR
  - Anton Zhiyanov argues: stop “programming in English.” If AI nails it quickly, great; otherwise write code and use AI to review, refactor, or fill gaps. HN largely agrees: autocomplete often distracts and harms comprehension, while chat/agents help when summoned. Treat LLMs like junior devs—stay in control; if progress stalls, switch models or ask a human. AI is best for bootstrapping unfamiliar APIs or idioms, with human verification. Some push code-only models and comment specs; others value LLMs’ embedded domain conventions for scaffolding.

- Comment pulse
  - Autocomplete distracts and breaks flow → constant suggestions and TAB misfires; prefer disabling and using chat on-demand — counterpoint: autocomplete differs from prompt-refinement the article critiques.
  - Use AI to overcome 'energy barrier' in new APIs/frameworks → quick, imperfect examples accelerate discovery; humans verify correctness and resource handling.
  - Treat LLMs as uncoachable juniors → you design interfaces/tests; if it fails, stop iterating, switch models or ask a human.

- LLM perspective
  - View: Code-first, AI-in-the-loop beats prompt-chasing; maintain agency by writing code and letting models refactor, review, or scaffold.
  - Impact: Shifts effort to clear interfaces and tests; reduces reliance on autocomplete; improves comprehension and long-term codebase familiarity.
  - Watch next: IDE workflows blending selective chat with structural refactors; benchmarks on task completion time and defect rates; viability of code-only models.
