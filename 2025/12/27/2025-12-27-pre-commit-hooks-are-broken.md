# Pre-commit hooks are broken

- Score: 141 | [HN](https://news.ycombinator.com/item?id=46398906) | Link: https://jyn.dev/pre-commit-hooks-are-fundamentally-broken/

### TL;DR

The author argues pre-commit hooks inspect the wrong state, collide with rebases, reject unrelated legacy files, and disrupt work-in-progress commits. Even sophisticated frameworks temporarily alter Git state and cannot guarantee every developer installs or honors them. The proposed alternative is optional, fast pre-push checks backed by authoritative CI, reserving earlier blocking mainly for secrets. HN largely agreed mandatory hooks become bypassed friction, though some defended pre-commit tooling as a convenient shared check definition when CI remains the final gate.

### Comment pulse

- Mandatory local hooks fail socially → unusual Git workflows and inconsistent branches teach developers to use `--no-verify`.
- Pre-commit remains useful voluntarily → shared definitions catch failures early while CI enforces repository policy.
- Automatic installation drew hostility → tools should not mutate personal workflows merely because tests ran.

### LLM perspective

- View: The real design error is confusing a developer feedback mechanism with an enforceable trust boundary.
- Impact: Moving enforcement to CI preserves commit workflows while optional local checks still reduce review latency.
- Watch next: Measure CI retries, hook bypass rates, rebase failures, and secret-detection coverage after changing stages.
