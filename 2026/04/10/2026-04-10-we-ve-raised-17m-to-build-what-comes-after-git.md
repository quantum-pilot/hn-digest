# We've raised $17M to build what comes after Git

- Score: 303 | [HN](https://news.ycombinator.com/item?id=47712656) | Link: https://blog.gitbutler.com/series-a

### TL;DR

GitButler raised a $17 million a16z-led Series A to rethink version control for teams and coding agents. Its CLI works inside Git repositories, targeting short-lived trunk workflows with stacked and parallel branches, change organization, scripting, and an operation log for undo. The ambition is to preserve conversations and agent context alongside changes, expose conflicts earlier, and let people and agents coordinate rather than exchange pull requests. Commenters question whether this replaces Git at all: many see a new porcelain or GitHub-like collaboration layer, with Jujutsu offering snapshot-centered alternatives.

### Comment pulse

- Git’s plumbing deliberately supports alternate porcelains, so critics want a precise unsolved problem rather than a replacement narrative.
- VC funding and unclear monetization triggered lock-in fears. — counterpoint: an open, finished CLI funded by investors could still benefit everyone.
- Jujutsu users praise automatic snapshots and cleanup-after-experimentation, though Git users argue commits, staging, and history rewriting already support that workflow.

### LLM perspective

- **View:** The opportunity is coordination metadata around change, not a new content-addressed store; positioning should reflect that narrower claim.
- **Impact:** Agent-heavy teams need context and conflict management before they need more code-generation throughput.
- **Watch next:** CLI license, hosted-service model, interoperability guarantees, large-agent-PR benchmarks, conflict detection quality, and adoption beyond early enthusiasts.
