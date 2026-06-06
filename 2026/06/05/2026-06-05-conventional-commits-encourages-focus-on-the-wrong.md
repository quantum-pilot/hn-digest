# Conventional Commits encourages focus on the wrong things

- Score: 249 | [HN](https://news.ycombinator.com/item?id=48414027) | Link: https://sumnerevans.com/posts/software-engineering/stop-using-conventional-commits/

### TL;DR

The author argues Conventional Commits are harmful because they foreground “type” (feat/fix/chore) and make “scope” optional, while people debugging, reviewing, or responding to incidents mainly care what subsystem changed. Commit types are often redundant or ambiguous and don’t reliably power auto-changelogs or semantic-version bumps, especially with reverts and subtle breakages. Instead, they advocate scope-first subjects (like Linux/Go’s `subsystem: description`) and treating changelog writing as a separate, curated, user-facing task. HN discussion centers on trade-offs between strict structure, context, and long-term usefulness.

### Comment pulse

- Structure defenders → Any enforced convention beats ad‑hoc “small fix” commits; Conventional Commits are “good enough,” and minor formatting differences aren’t worth a new standard.
- Structure critics → Rigid templates discard natural-language emphasis; quality comes from explaining “why,” not tagging fix/feat; external ticket links rot and shouldn’t replace in-message rationale.
- Alternative priorities → Some say scope is obvious from paths and prefer ticket IDs or curated release notes; others like Linux-style scope-first subjects and distrust automation-led SemVer/changelog schemes.

### LLM perspective

- View → Treat commit rules as local contracts: pick a style, document it with examples, and periodically adjust based on actual friction.
- Impact → Scope-oriented subjects plus a brief “why” greatly aid debugging, reviews, and future archaeology when issue trackers or docs vanish.
- Watch next → Favor tools that infer impact from diffs/tests so commit style optimizes human communication rather than driving brittle automation.
