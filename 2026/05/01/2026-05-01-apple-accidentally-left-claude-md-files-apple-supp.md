# Apple accidentally left Claude.md files Apple Support app

- Score: 364 | [HN](https://news.ycombinator.com/item?id=47973378) | Link: https://x.com/aaronp613/status/2049986504617820551

### TL;DR

A widely viewed post reported that Apple Support 5.13 accidentally bundled `CLAUDE.md` files, then said Apple released 5.13.1 the next day to remove them. The supplied post does not show their contents, so it establishes a packaging mistake but not what Claude did during development. Discussion treated the files as evidence of internal Anthropic use, citing an outside claim that Apple runs customized Claude models on its own servers. Most technical debate separated version-controlling shared agent instructions, often useful, from incorrectly shipping development documentation inside a product.

### Comment pulse

- Teams defended committing agent files because they capture architecture, repository layout, conventions, prohibitions, and reproducible context.
- Critics blamed AI-driven haste and weak review — counterpoint: the packaging pipeline, not source control, should exclude development-only artifacts.
- Some objected to LLM-written social replies, viewing synthetic conversation as corrosive to human communities.

### LLM perspective

- Release manifests should allowlist intended resources rather than depend on scattered ignore rules.
- CI can inspect application bundles for instruction files, secrets, and workstation metadata.
- Human review remains accountable even when generation tools accelerate commit volume.
