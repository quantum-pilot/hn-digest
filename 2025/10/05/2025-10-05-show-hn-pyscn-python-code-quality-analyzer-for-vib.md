# Show HN: Pyscn – Python code quality analyzer for vibe coders

- Score: 115 | [HN](https://news.ycombinator.com/item?id=45481298) | Link: https://github.com/ludo-technologies/pyscn

- TL;DR
  - pyscn is a fast Go-based Python code quality analyzer for AI-assisted "vibe" coding and legacy cleanup. It performs structural analysis: CFG-based dead code, clone detection via APTED + LSH, coupling (CBO), and cyclomatic complexity, outputting HTML/JSON and CI-friendly checks. HN likes its focus on duplication/dead code and asks about research (APTED) and multi-language plans (tree-sitter suggests feasible). Discussion debates "vibe coding" framing; many see the real users as maintainers cleaning AI-generated code. One user notes a progress-bar ETA glitch.

- Comment pulse
  - Positioning matters → "for vibe coders" polarizes; maintainers inheriting AI codebases are the real buyers — counterpoint: veteran devs also vibe-code and would use it.
  - Technique → clone detection uses APTED with LSH to prune O(n²); CFG for dead code; tree-sitter enables multi-language, though CFG/deps need per-language plumbing.
  - Workflow fit → shines in CI to surface duplication/dead code invisible in diffs; Qlty integration planned; one report of progress-bar ETA glitch.

- LLM perspective
  - View: Structural analysis complements linters, giving objective guardrails for AI-assisted coding and large refactors.
  - Impact: Python teams inheriting AI code; CI quality gates; reviewers prioritizing clones, dead code, coupling hotspots.
  - Watch next: Publish accuracy/recall benchmarks, ship GitHub Action and Qlty plugin, prototype multi-language CFGs, fix progress ETA.
