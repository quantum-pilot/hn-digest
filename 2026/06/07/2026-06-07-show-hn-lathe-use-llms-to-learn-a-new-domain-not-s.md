# Show HN: Lathe – Use LLMs to learn a new domain, not skip past it

- Score: 223 | [HN](https://news.ycombinator.com/item?id=48433756) | Link: https://github.com/devenjarvis/lathe

### TL;DR

Lathe combines a Go CLI and web reader with agent skills that generate sourced, multi-part technical tutorials, then makes learners type and run the work rather than delegate it. Tutorials record model, voice, tool versions, and research URLs; optional verification executes checkpoints in a scratch directory and stores results. The author prefers human material when available and admits generated courses remain weaker and fallible. HN liked the deterministic-CLI-plus-agent pattern, suggested Socratic quizzing, and emphasized that repetition builds fluency while taste still separates good instruction from average output.

### Comment pulse

- Socratic questioning may deepen retention → an LLM can keep probing until learners derive answers themselves — counterpoint: long sessions risk context degradation.
- Typing correct examples builds fluency → high-volume manual reproduction strengthens reading and muscle memory before independent code generation becomes comfortable.
- Skills plus a CLI balance strengths → agents handle variable reasoning while deterministic commands manage storage, repeatable state changes, and artifacts.

### LLM perspective

- **View:** Provenance and executable checkpoints test traceability and mechanics, not whether explanations are pedagogically sound or conceptually complete.
- **Impact:** Tutorial generators should measure learner performance, not successful builds, and adapt exercises around misconceptions revealed during work.
- **Watch next:** Compare Lathe against human tutorials, direct prompting, and Socratic tutoring on retention, transfer, completion, hallucination detection, and cost.
