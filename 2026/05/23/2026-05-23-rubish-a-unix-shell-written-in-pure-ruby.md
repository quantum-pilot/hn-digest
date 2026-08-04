# Rubish: A Unix shell written in pure Ruby

- Score: 168 | [HN](https://news.ycombinator.com/item?id=48245262) | Link: https://github.com/amatsuda/rubish

### TL;DR

Rubish is a Unix shell that parses Bash-compatible syntax into Ruby and executes it on the Ruby VM, while adding native Ruby expressions, method-call commands, chained pipelines, iterator blocks, lambdas, function definitions, programmable prompts, and project-local configuration. It also claims zsh-style features, restricted execution for untrusted scripts, background-loaded initialization, broad built-ins, and an embeddable REPL API. HN readers admired the Bash–Ruby fusion but saw deployment on remote hosts as its adoption barrier; discussion also questioned whether agent-assisted, long-method code makes open-source contribution tooling-dependent.

### Comment pulse

- Bash persists because it is already installed almost everywhere; replacing it can force users to maintain incompatible local and remote workflows.
- Maintainers debated 200-line methods and missing boundaries — counterpoint: similarly difficult hand-written code long predates LLMs and remains refactorable.
- Language-native shells can be valuable learning environments even when ergonomics eventually send users back to conventional shells.

### LLM perspective

- View: Compatibility lowers migration cost, but Ruby extensions create a portability gradient where enhanced scripts cease being ordinary Bash.
- Impact: Ruby users gain expressive pipelines and embedding hooks; teams inherit another runtime, parser, security model, and deployment dependency.
- Watch next: Bash conformance results, startup latency, restricted-mode escapes, job-control edge cases, packaging, and real-world remote usage.
