# Claude Code gets native LSP support

- Score: 264 | [HN](https://news.ycombinator.com/item?id=46355165) | Link: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

### TL;DR

Claude Code 2.0.74 adds a Language Server Protocol tool for go-to-definition, reference finding, and hover documentation, alongside terminal support, syntax-highlighting controls, and several fixes. The changelog does not detail language coverage, triggering behavior, or setup. Commenters report discovering language servers through the plugin manager but describe documentation and installation as unclear. They welcome deterministic code intelligence, while arguing that semantic refactoring and compiler-backed transformations would matter more than read-only navigation when agents rename symbols or restructure large codebases.

### Comment pulse

- LSP access should reduce missed references, but readers want mutation-safe refactors rather than smarter lookup alone.
- CLI users value editor independence; critics note IDE agents and competing tools already offered comparable integration.

### LLM perspective

- View: Semantic lookup is foundational, but reliable transformation is the higher-value capability.
- Impact: Agents can navigate large repositories with less textual guessing, potentially shrinking context and review errors.
- Watch next: Verify supported servers, invocation transparency, refactoring commands, and measurable rename accuracy.
