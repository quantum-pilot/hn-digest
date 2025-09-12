# A staff engineer's journey with Claude Code

- Score: 548 | [HN](https://news.ycombinator.com/item?id=45107962) | Link: https://www.sanity.io/blog/first-attempt-will-be-95-garbage

- TL;DR
    - A staff engineer at Sanity reports six weeks with Claude Code: first attempts ~95% garbage, but iterative, tightly scoped passes yielded working components (e.g., quota thresholds, Sentry cron wrapper). He treats Claude as a fast junior exploring options while he owns architecture and reviews every line, reporting net productivity. HN replies echo: LLMs help with debugging, scaffolding, and ideation, but struggle on complex production code without heavy supervision. Skeptics want concrete repos or livestreams; others tout agent workflows and stepwise prompting as quality multipliers.
    - Content unavailable; summarizing from title/comments.

- Comment pulse
    - Adjunct tool, not autonomous coder → good at debugging/boilerplate; production work needs supervision, style control, tests, and pruning.
    - Junior risk and trust → reliance reduces learning; reviewers can’t trust outputs — counterpoint: agent loops, small steps, and TDD markedly improve outcomes.
    - Show proof → demand independent, non-greenfield livestreams with PRs/tests; skepticism about delegating core infra and claims of >$1k/month costs.

- LLM perspective
    - View: Treat models as fast breadth-first explorers; humans prune, enforce taste, and write tests to converge.
    - Impact: Boosts senior productivity; may widen skill gap for juniors lacking review judgment and system context.
    - Watch next: Public benchmarks on existing repos comparing agent workflows: cost-per-merged-change, defect density, rework time, and wall-clock to green PR.
