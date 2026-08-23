# Autolith: A programming agent with a live runtime

- Score: 121 | [HN](https://news.ycombinator.com/item?id=49376197) | Link: https://www.lambda-symbolics.com/autolith

### TL;DR

Autolith is a terminal coding agent whose tools, conversation state, and Common Lisp runtime share one process. It can inspect or redefine its own running functions, journal experiments, retain approved changes as private replayable commits, recover from crashes, and analyze corpora larger than a model window through bounded recursive inference. Captured sessions demonstrate these claims, but the program explicitly is not a security sandbox. Commenters liked Lisp’s moldability while questioning when self-modification beats generating ordinary external tools and asking for agent-benchmark comparisons.

### Comment pulse

- Self-modification may be unnecessary for routine extensions → an agent can write and invoke external tools without changing its own interface.
- Lisp, Smalltalk, and Elixir invite inspectable live systems → enthusiasts see agents as a modern setting for old self-improving-program ideas.
- Demonstrations show distinctive mechanics → benchmark results against agents such as Prime Agent remain an open request.

### LLM perspective

- View: Autolith’s novelty is durable, inspectable runtime mutation with recovery, not merely repository editing or persistent chat history.
- Impact: Lisp developers gain an unusually moldable agent; users assume the full risk of model-generated code running under their privileges.
- Watch next: Independent benchmarks should measure task quality, recovery reliability, resource use, and whether live mutation outperforms ordinary tool generation.
