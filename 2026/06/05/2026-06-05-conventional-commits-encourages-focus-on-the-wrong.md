# Conventional Commits encourages focus on the wrong things

- Score: 249 | [HN](https://news.ycombinator.com/item?id=48414027) | Link: https://sumnerevans.com/posts/software-engineering/stop-using-conventional-commits/

### TL;DR

The essay argues that Conventional Commits makes type mandatory while scope—the component contributors, debuggers, and incident responders actually search for—is optional. Types can be ambiguous or redundant, and commit-derived changelogs, SemVer bumps, and CI decisions misread developer history as release intent. It recommends project-specific scope prefixes and separately curated user-facing changelogs. HN discussion was less categorical: some valued any enforceable convention and automation, while others said neither type nor scope captures the durable information future readers need—the reason for a change—and warned that external issue links may disappear.

### Comment pulse

- Standardization → Supporters prefer a common grammar over competing formats and say linting prompts thought — counterpoint: rigid structure cannot guarantee useful communication.
- Context → Many prioritized why over what; issue IDs can preserve discussion, but repository-external trackers may vanish and leave immutable commits meaningless.
- Release notes → Type grouping aids automated scanning; opponents say users need deliberately curated narratives, not development mechanics.

### LLM perspective

- **View:** Commit messages are durable human evidence first; machine-readable metadata should remain subordinate and independently verifiable.
- **Impact:** Teams can keep automation without flattening prose by using trailers, changed-path analysis, and curated release artifacts.
- **Watch next:** Compare formats using incident lookup time, changelog editing effort, versioning errors, and contributor correction rates.
