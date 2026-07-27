# Ruff v0.16.0 – Significant new updates – 413 default rules up from 59

- Score: 332 | [HN](https://news.ycombinator.com/item?id=49056112) | Link: https://astral.sh/blog/ruff-v0.16.0

### TL;DR
Ruff 0.16 massively expands its default linting surface: 413 rules now run out‑of‑the‑box (up from 59), surfacing many previously hidden syntax and runtime issues, including bugbear, pyupgrade, and Ruff‑specific checks. You can still opt back into the old minimal set via `select`. New features include formatting Python code inside Markdown/Quarto, richer `ruff: ignore`/`file-ignore` comments with auto‑insertion, and inline diffs in `check`/`format --check`. HN discussion praises Ruff’s real‑world impact, debates linter “overreach,” and compares ecosystems like Go’s.

---

### Comment pulse
- Upgrading existing projects → Users report painless migration from 0.15, many real issues found; Ruff and uv praised, ty seen as weaker than basedpyright.
- Linters as “style police” vs helpers → Critics see arbitrary churn; defenders say consistent bots end PR bikeshedding and save cognitive load—counterpoint: strict rules can still fight author intent.
- Default 413 rules → Great zero‑config safety for new repos; legacy code may drown in warnings, but AI/agents could bulk‑fix them.

---

### LLM perspective
- View: Ruff’s speed plus broad rule coverage makes “one linter to rule them all” actually practical for Python teams.
- Impact: Large, long‑lived codebases and doc‑heavy projects gain most from default rules, Markdown support, and granular suppressions.
- Watch next: Rule recategorization, migration tooling for legacy projects, and other languages copying Ruff’s fast, unified-tooling model.
