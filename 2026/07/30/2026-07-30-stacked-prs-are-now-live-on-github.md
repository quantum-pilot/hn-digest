# Stacked PRs are now live on GitHub

- Score: 421 | [HN](https://news.ycombinator.com/item?id=49112232) | Link: https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/

## TL;DR
GitHub has rolled out first-class “stacked PRs,” letting developers submit dependent pull requests as an ordered stack instead of a single giant diff. Early users welcome mainstream support for workflows long common in Gerrit/Phabricator, enabling smaller, focused reviews, partial merges, and parallel work on large features. However, commenters report serious bugs—especially with squash-merging entire stacks—and argue GitHub retained a flawed review model (per-branch PRs, no change-ids/interdiffs), limiting the feature’s power until the underlying tooling evolves.

*Content unavailable; summarizing from title and discussion only.*

## Comment pulse
- Stacked PRs ship with bugs: squash merges fail, approvals reset, merges get stuck → feels premature — counterpoint: GitHub says fixes are priority, success ~99%.
- Critics say GitHub copied stacked diffs poorly: per-PR branches, no change-ids/interdiffs, still centered on new-commit+merge instead of amend+rebase workflows.
- Fans argue stacks enable small, focused reviews, parallel work, targeted reviewers, partial merges, and help teams whose commits are messy “savepoints” rather than curated history.

## LLM perspective
- View: Feature formalizes existing stacked-branch workflows, but exposes GitHub’s aging review model; long-term value depends on deeper tooling changes, not UI alone.
- Impact: Large orgs with complex changesets, monorepos, or AI-sized diffs gain most; small teams may see marginal benefit over disciplined commit-based review.
- Watch next: Watch for cross-fork support, robust squash-merge semantics, change-id style tracking, and better diff navigation before standardizing workflows around stacked PRs.
