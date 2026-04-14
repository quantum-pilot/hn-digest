# GitHub Stacked PRs

- Score: 353 | [HN](https://news.ycombinator.com/item?id=47757495) | Link: https://github.github.com/gh-stack/

## TL;DR
GitHub Stacked PRs, now in private preview, brings first-class stacked-diff workflows to GitHub: a CLI (gh stack) and new UI let you arrange PRs as ordered chains, auto-rebase remaining layers, and merge whole or partial stacks. CI and protections apply as if each PR targeted main. Commenters familiar with Phabricator, Gerrit, or Mercurial are excited, saying this finally modernizes GitHub reviews, while others argue Git already has commits and that better per-commit tooling would solve most pain.

## Comment pulse
- Stacked PRs recreate Phabricator-style flow → small dependent diffs review and land easily for big refactors — counterpoint: some want better per-commit UI instead.  
- Skeptics worry about rebases, squashes, and force-pushes → stacked workflows feel like fragile history surgery compared to simple merge commits and first-parent bisecting.  
- Questions remain about squash-merge edge cases and CI costs → users hope `gh stack sync` and multi-PR merge will finally make stacked branches “just work”.  

## LLM perspective
- View: Native stacks plus an official CLI normalize a workflow previously cobbled together via scripts, Gerrit, or third-party tools.  
- Impact: Biggest wins for teams with large monorepos, long-lived feature branches, or AI agents that can reason over GitHub-managed stacks.  
- Watch next: How GitHub refines merge, rebase, and CI for partial-stack merges, and whether commit review tooling improves alongside stacks.
