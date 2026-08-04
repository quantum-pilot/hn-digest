# DeepSeek-V4-Flash means LLM steering is interesting again

- Score: 199 | [HN](https://news.ycombinator.com/item?id=48160807) | Link: https://www.seangoedecke.com/steering-vectors/

### TL;DR

Sean Goedecke argues DeepSeek-V4-Flash and DwarfStar 4 make activation steering practical for a locally runnable, coding-capable model. Steering derives vectors from activation differences, then applies them during inference to amplify behaviors. He doubts ordinary style controls beat prompting or complex goals beat fine-tuning, but sees possible context compression and “unpromptable” controls. HN highlighted the concrete counterexample: runtime steering can suppress refusal only when needed, avoiding the broader capability damage of permanently altered weights while exposing controls frontier APIs hide.

### Comment pulse

- Runtime refusal control is already practical → conditional steering can avoid the capability loss of permanently ablating or republishing model weights.
- DwarfStar 4 is independent but indebted to llama.cpp, sharing some kernels, formats, and engineering knowledge rather than being a stripped-down fork.
- Users want hidden inference knobs exposed → counterpoint: dynamic uncensoring also removes safeguards, making access and release policy contentious.

### LLM perspective

- **View:** Steering matters most where prompts cannot reach a behavior and full fine-tuning is unnecessarily destructive.
- **Impact:** Local-model users gain reversible, phase-specific controls; providers face pressure to expose comparable interfaces.
- **Watch next:** Benchmark refusal suppression, capability degradation, vector portability, threshold activation, codebase compression, and agent-task outcomes.
