# Everything as code: How we manage our company in one monorepo

- Score: 159 | [HN](https://news.ycombinator.com/item?id=46437381) | Link: https://www.kasava.dev/blog/everything-as-code-monorepo

### TL;DR

Kasava keeps application code, documentation, marketing, email templates, extensions, internal plans, and even its investor deck in one repository. Shared configuration enables cross-boundary changes, while path-filtered CI and independent npm projects limit unnecessary builds. The company argues this structure gives AI assistants complete context and makes every change reviewable through Git. HN challenged the “entire company” framing, noting missing finance and HR, and stressed that atomic commits do not eliminate backward-compatible APIs, database migrations, or staged deployments.

### Comment pulse

- The scope is overstated → this resembles a product monorepo, possibly for a one-person company, rather than complete corporate operations.
- Atomic source changes are useful → coordinated frontend, backend, and docs edits reduce drift—counterpoint: runtime rollouts remain non-atomic.
- AI context favors proximity → one repository is convenient, though multi-repository workspaces can expose the same files.

### LLM perspective

- View: Repository topology improves discoverability, not distributed-system consistency or organizational coordination.
- Impact: Small teams gain simpler reviews and richer agent context while accepting broader permissions and repository coupling.
- Watch next: Measure deployment failures, CI latency, access-control pressure, and divergence as teams and services multiply.
