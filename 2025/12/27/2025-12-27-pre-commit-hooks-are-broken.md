# Pre-commit hooks are broken

- Score: 141 | [HN](https://news.ycombinator.com/item?id=46398906) | Link: https://jyn.dev/pre-commit-hooks-are-fundamentally-broken/

## TL;DR
- The author demonstrates that Git pre-commit hooks are brittle: they often run on the wrong state (working tree vs index), break during rebases/merges, and can’t be relied on because other contributors may not have them installed or may bypass them.  
- Heavy hooks (formatting, tests, builds) also clash with workflows that use frequent WIP commits instead of stashes.  
- They recommend moving checks to pre-push hooks and CI, reserving pre-commit mainly for blocking secrets from ever being recorded.

## Comment pulse
- Hooks should be optional dev aids, not gates → CI enforces correctness; pre-push hooks plus PR checks reduce churn without blocking workflows.  
- Forcing strict hooks or auto-installing them breeds resentment → people commit with `--no-verify`, undermining the mechanism and complicating merges.  
- Some argue enforcing a unified workflow and formatter saves pain via consistency → counterpoint: that consistency belongs in CI, not local Git.

## LLM perspective
- View: Treat git hooks as UX-sensitive tools: favor manual scripts or opt-in helpers over automatic, repo-controlled pre-commit logic.  
- Impact: Teams gain flexibility for complex histories, rebases, and JJ-style workflows while still centralizing guarantees in CI and protected branches.  
- Watch next: Standardize lightweight secret scanning/formatting configs runnable locally and in CI; track hook adoption, `--no-verify` usage, and CI failure rates.
