# Using go fix to modernize Go code

- Score: 256 | [HN](https://news.ycombinator.com/item?id=47049479) | Link: https://go.dev/blog/gofix

### TL;DR
Go 1.26 completely rewrites `go fix` as a first-class, analysis-based refactoring tool. It now runs the same modular analyzer framework as `go vet`, applying safe, automated code rewrites to modernize Go projects: adopting generics helpers (`maps.Keys`, `strings.Cut`), new language features (`range`-over-int, `min`/`max`, `new(expr)`), and better patterns (`strings.Builder`, etc.). Modernizers are version-aware, can be selectively enabled, compose synergistically, and will evolve toward “self-service” analyzers that library and infra maintainers can ship with their own code.

---

### Comment pulse
- LLMs stagnate idioms → models emit outdated or unsafe Go (especially concurrency), even when asked for “modern Go,” so modernizing open-source corpus matters for future training data.  
- Go tooling praised → `go fix`, `go vet`, `gopls` feel unusually cohesive; some note other ecosystems have similar tools (Coccinelle, Roslyn, clippy, IDE refactorings) but less standardized.  
- Self-service/static analyzers excite people → infra and big-library authors want first-class, sharable analyzers; parallels drawn to Rust’s clippy, Python’s pyupgrade, and Java/TypeScript codemods.

---

### LLM perspective
- View: Tools like `go fix` systematically uplift corpus quality, indirectly steering future LLM outputs toward safer, idiomatic Go.  
- Impact: Library authors, infra teams, and large Go codebases gain cheap, repeatable upgrades; reviewers shift from style policing to semantic review.  
- Watch next: Dynamic loading of project-local analyzers, control-flow–templated “don’t forget to X after Y” checks, and tighter integration with LSP/agent guardrails.
