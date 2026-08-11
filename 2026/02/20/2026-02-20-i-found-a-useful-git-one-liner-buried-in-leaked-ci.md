# I found a useful Git one liner buried in leaked CIA developer docs

- Score: 582 | [HN](https://news.ycombinator.com/item?id=47088181) | Link: https://spencer.wtf/2026/02/20/cleaning-up-merged-git-branches-a-one-liner-from-the-cias-leaked-dev-docs.html

### TL;DR

The post revives a branch-cleanup command found in leaked CIA developer documentation: list local branches merged into a target, exclude the current and protected mainline branches, then delete the remainder with Git’s safe lowercase deletion flag. Its updated version checks against `origin/main` and can be saved as an alias. It is convenient for conventional merge workflows, but not universally safe or complete: squash and rebase merges break ancestry detection, linked worktrees need protection, and hard-coded branch names may not match a repository’s actual default.

### Comment pulse

- Commenters proposed deriving the default branch from remote metadata and excluding branches checked out in other worktrees.
- Squash/rebase workflows need different signals — counterpoint: pruning deleted upstream branches is often sufficient when remote cleanup is disciplined.
