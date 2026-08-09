# GitHub Stacked PRs

- Score: 353 | [HN](https://news.ycombinator.com/item?id=47757495) | Link: https://github.github.com/gh-stack/

### TL;DR

GitHub’s private-preview Stacked PRs lets teams split one large change into ordered, dependent pull requests, each targeting the branch below it and ultimately main. GitHub adds a stack map, focused diffs, final-target branch protections, per-layer CI, cascading rebases, and one-click merging of all or part of a stack; the `gh stack` extension manages branches, pushes, submissions, and navigation locally. Commenters welcomed a Phabricator/Gerrit-style workflow for monorepos and long features, but questioned branch-over-commit abstraction, CLI dependence, squash/rebase conflict handling, history rewriting, and repeated CI after restacking.

### Comment pulse

- Phabricator and Gerrit veterans said small dependent diffs make massive upgrades and long-running features easier to review without requiring partial landing.
- Some wanted commit-level review, comments, and diff-of-diffs instead — counterpoint: PRs represent atomic outcomes while commits can preserve their evolution.
- GitHub clarified multiple lower PRs can merge together after their CI passes; only the remaining top is rebased and likely retested.

### LLM perspective

- **View:** Native stack semantics close a long-standing GitHub gap by making dependency structure visible to reviewers, automation, and branch protection.
- **Impact:** Teams can keep diffs small without serializing development, reducing review burden while preserving an all-or-nothing delivery option.
- **Watch next:** Availability, UI-only workflows, squash correctness, force-push safety, CI reuse after rebases, merge-queue behavior, and interoperability with other tools.
