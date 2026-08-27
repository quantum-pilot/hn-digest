# Show HN: Pyscn – Python code quality analyzer for vibe coders

- Score: 115 | [HN](https://news.ycombinator.com/item?id=45481298) | Link: https://github.com/ludo-technologies/pyscn

### TL;DR

pyscn is a Go and tree-sitter-based structural analyzer aimed at Python code produced with AI assistance. It reports control-flow-based dead code, clone candidates using tree edit distance plus locality-sensitive hashing, module coupling, and cyclomatic complexity. Users can generate HTML or JSON reports, select analyses, configure thresholds, or run a pass/fail CI check. The project claims throughput above 100,000 lines per second, but the supplied material offers no independent benchmark or accuracy evaluation for its findings.

### Comment pulse

- Commenters saw value in cleanup workflows, inherited codebases, and feeding findings back to coding agents.
- One tester reported a misleading progress percentage, though analysis completed quickly.

### LLM perspective

- View: Structural checks are useful grounding for AI-assisted maintenance because duplication and dead code evade ordinary diffs.
- Impact: Fast CI feedback helps only if teams calibrate false positives and avoid treating metrics as design judgment.
- Watch next: Comparative accuracy tests and additional language front ends would clarify whether the approach generalizes.
