# Everything as code: How we manage our company in one monorepo

- Score: 159 | [HN](https://news.ycombinator.com/item?id=46437381) | Link: https://www.kasava.dev/blog/everything-as-code-monorepo

### TL;DR
Kasava runs nearly everything in a single monorepo—frontend, backend, marketing site, public/internal docs, email templates, browser extensions, investor deck, and some cloud functions. The point isn’t “monorepo vs polyrepo” so much as “everything-as-code” optimized for AI tooling: one source of truth, atomic PRs that touch product + docs + marketing, and Git-based workflows for all content. They avoid npm workspaces, use path-based CI, and rely on CLAUDE.md files so AI assistants can quickly orient and operate across the whole codebase.

---

### Comment pulse
- This is just a standard product monorepo → not “whole company”; likely a one-person startup, missing infra, finance, and real non-code artifacts.  
- Monorepo ≠ lockstep deploys → you still need stable APIs, backward-compatible DB changes, releases, and cherry-picks; “one change everywhere” can be dangerous at scale.  
- AI tools make monorepos newly attractive → easier context for Claude/LLMs, synced FE/BE changes, PRDs/docs in Git—counterpoint: good tooling could also span multiple repos.

---

### LLM perspective
- View: Treating docs, marketing, and specs as code in one repo genuinely boosts what LLMs can safely automate and validate.  
- Impact: Small teams and solo founders benefit most; large orgs must still manage versioning, permissions, and deployment independence.  
- Watch next: Better multi-repo AI context handling, monorepo-aware CI/release tooling, and real-case studies from bigger companies with uptime and compliance constraints.
