# PEP 810 – Explicit lazy imports

- Score: 245 | [HN](https://news.ycombinator.com/item?id=45466086) | Link: https://pep-previews--4622.org.readthedocs.build/pep-0810/

### TL;DR

PEP 810 proposes explicit `lazy import` and `lazy from` syntax that binds a name immediately but loads and executes its module only on first use. It aims to reduce startup latency, memory use, and unnecessary dependency work while leaving ordinary imports unchanged. Laziness is designed to be local, non-recursive, granular, and opt-in, using proxy objects that resolve and rebind on access. The proposal also specifies filters, global controls, tooling behavior, deferred-error handling, compatibility mechanisms, and restrictions such as module-level use and no star imports.

### Comment pulse

- A CLI author welcomed relief from plugins that eagerly import heavy dependencies even for help output.
- Supporters contrasted the explicit design with an earlier rejected proposal; skeptics feared `lazy` would become permanent visual noise.
- Commenters also raised linting, platform-specific imports, and alternative user-space implementations.

### LLM perspective

- View: Explicit laziness makes import cost visible without silently changing every module’s execution semantics.
- Impact: Faster startup trades immediate failures for delayed ones, increasing the value of representative execution tests.
- Watch next: Steering Council feedback should clarify whether implementation complexity justifies syntax-level support.
