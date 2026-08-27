# Write the damn code

- Score: 198 | [HN](https://news.ycombinator.com/item?id=45415232) | Link: https://antonz.org/write-code/

### TL;DR

Anton Zhiyanov advises programmers to stop endlessly refining natural-language prompts when an AI coding result remains wrong. Instead, ask for a draft and refactor it, write the draft and request review, implement critical pieces manually, or supply a code outline for completion. The argument is pro-tool but anti-detachment: programming languages give engineers a more precise way to specify and correct behavior than repeated English instructions. If the model does not converge within one or two tries, direct code changes create a stronger new context for further assistance.

### Comment pulse

- Several disabled intrusive autocomplete because evaluating suggestions broke focus, while retaining on-demand chat or agent tools.
- Readers valued AI most in unfamiliar APIs and languages, treating imperfect examples as a starting map.
- Others recommended controlling architecture, interfaces, and tests while delegating bounded implementation work.

### LLM perspective

- View: Code, tests, and interfaces are high-bandwidth feedback when conversational correction stops converging.
- Impact: Staying hands-on preserves comprehension and turns AI from an opaque factory into a bounded collaborator.
- Watch next: Teams should measure whether prompting, editing, or manual implementation is fastest by task and failure mode.
