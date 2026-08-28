# Stop writing CLI validation. Parse it right the first time

- Score: 203 | [HN](https://news.ycombinator.com/item?id=45151622) | Link: https://hackers.pub/@hongminhee/2025/stop-writing-cli-validation-parse-it-right-the-first-time

### TL;DR

Optique applies “parse, don’t validate” to TypeScript CLIs: dependent, mutually exclusive, and environment-specific options are composed into parsers that return discriminated types representing only valid configurations. This moves checks to one boundary, lets TypeScript expose every affected call site during refactoring, and removes scattered validation logic. The author says the young library suits complex CLIs, not tiny scripts. Commenters agreed with encoding invariants but noted validation still exists inside the parser, dependencies change, and helpful multi-error reporting remains essential.

### Comment pulse

- Supporters emphasized transforming raw input once into a structure whose invariants application code can trust.
- Critics called the slogan semantic repackaging because a library still performs validation and creates maintenance risk.
- Runtime debates were separate from the design: native binaries simplify distribution, while managed runtimes can simplify builds and internal tooling.

### LLM perspective

- View: The gain comes from boundary normalization and invariant-rich types, not from eliminating validation itself.
- Impact: Complex CLI code becomes easier to refactor, but users depend heavily on parser diagnostics and API stability.
- Watch next: Aggregate error quality, shell completion, compatibility behavior, and whether Optique’s API stabilizes under broader use.
