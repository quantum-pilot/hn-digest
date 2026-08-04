# Claude Code – Everything you can configure that the docs don't tell you

- Score: 322 | [HN](https://news.ycombinator.com/item?id=48318174) | Link: https://buildingbetter.tech/p/i-read-the-claude-code-source-code

### TL;DR

A source-code tour of Claude Code 2.1.87 catalogues configuration: hooks can rewrite tool inputs, inject context, decide permissions, watch files, or run asynchronously; skills and agents can select models, scope hooks, delegate work, retain memory, or ignore project instructions. It also describes natural-language auto-mode rules, automatic memory and “dream” consolidation, Magic Docs, permission globs, and cached fork behavior. The author labels these undocumented and unstable. HN disputed that premise, linking official documentation for many fields, calling the two-month-old article outdated and AI-generated, and warning that rapid releases make reliance brittle.

### Comment pulse

- Documentation status was the central rebuttal → commenters linked official pages covering hook responses, once/async fields, skill frontmatter, and auto-mode environment strings.
- Freshness undermines source-diving guides → ten package releases weekly can document, rename, or remove behavior before an article’s circulation peaks.
- Undocumented tricks divided users → skeptics expected breakage — counterpoint: others said temporary hacks can materially improve frontier workflows if maintained.

### LLM perspective

- **View:** The useful artifact is a versioned capability inventory, not the article’s claim that those capabilities remain undocumented.
- **Impact:** Copy-paste automation built on unstable internals can silently weaken permission boundaries, memory behavior, or cost controls after upgrades.
- **Watch next:** Release-specific docs, deprecation notices, schema validation, regression tests for hooks, and security review of auto-approval configurations.
