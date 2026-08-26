# Cursor's latest “browser experiment” implied success without evidence

- Score: 348 | [HN](https://news.ycombinator.com/item?id=46646777) | Link: https://embedding-shapes.github.io/cursor-implied-success-without-evidence/

### TL;DR

Cursor described hundreds of agents collaborating for nearly a week on a million-line browser codebase, presenting screenshots and claiming meaningful progress. The author found no reproducible build: current code had dozens of compiler errors, recent CI failed, and none of 100 checked commits passed cargo check. HN largely criticized the gap between cautious technical wording and promotional claims. Counterarguments noted substantial custom browser components, later compilation fixes, and that the real experiment tested long-running multi-agent coordination rather than delivery of a usable browser.

### Comment pulse

- Public evidence showed no clean build across 100 commits → screenshots lacked a known-good revision or reproduction instructions.
- Critics saw fundraising hype disguised as research → counterpoint: the article itself avoided calling the browser production-ready.
- Defenders identified custom JS, DOM, layout, and painting systems → the experiment’s target may be agent coordination, not product quality.

### LLM perspective

- View: Scale measured in agents, commits, or lines is meaningless without executable acceptance tests.
- Impact: AI coding vendors face higher demands for pinned revisions, build recipes, and functional demonstrations.
- Watch next: Reproducible benchmarks for long-running teams, CI pass rates, regression trends, and maintained releases.
