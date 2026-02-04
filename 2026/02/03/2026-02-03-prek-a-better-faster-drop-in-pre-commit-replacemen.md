# Prek: A better, faster, drop-in pre-commit replacement, engineered in Rust

- Score: 176 | [HN](https://news.ycombinator.com/item?id=46873138) | Link: https://github.com/j178/prek

## TL;DR
Prek is a Rust reimplementation of the popular Python-based `pre-commit` framework: a single, dependency-free binary that’s significantly faster, reuses existing `.pre-commit-config.yaml` files, and adds monorepo/workspace support, better toolchain sharing, built‑in Rust hooks, and tight integration with Astral’s `uv`. It’s already adopted by projects like CPython, Airflow, and FastAPI. HN commenters like the speed and drop‑in compatibility but debate whether pre‑commit-style hooks are the right model at all, proposing background daemons, WASI sandboxes, or push-time checks instead.

---

## Comment pulse

- Pre-commit hooks are the wrong abstraction → prefer a local CI/daemon (SelfCI, jj workflows, file watchers) running checks per change in the background — counterpoint: aliases + `pre-commit` still work well for explicit validation.

- Building on the pre-commit ecosystem is a mistake → it entangles tool installation, limits parallelism, and increases supply-chain risk — counterpoint: compatibility unlocks a huge existing catalog of hooks immediately.

- Value of git hooks is questioned → they’re optional, slow, and duplicable by scripts; supporters mirror CI steps in hooks to fail faster and reuse configs in CI.

---

## LLM perspective

- View: Prek smartly optimizes an existing workflow rather than inventing a new one, lowering adoption friction via full config compatibility.

- Impact: Most useful for large or polyglot repos, Python-averse environments, and orgs standardizing lint/test logic across local dev and CI.

- Watch next: Maturity of language support, clearer security/supply-chain posture, and whether git or DVCS tools standardize a first-class hook/extension mechanism.
