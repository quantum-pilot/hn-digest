# The git history command

- Score: 424 | [HN](https://news.ycombinator.com/item?id=48901010) | Link: https://lalitm.com/post/git-history/

## TL;DR
Git’s new experimental `git history` command brings safer, higher‑level history editing directly into core Git, inspired by tools like `jj` but without leaving Git. It adds three operations—`fixup`, `reword`, and `split`—that rewrite past commits and automatically adjust all descendant branches, while guaranteeing atomicity by refusing conflict-producing rewrites. `git history` doesn’t yet handle merges or first‑class conflicts and lacks `jj`’s operation log and working-copy model, but already makes complex rebases and stack editing much simpler.

---

## LLM perspective
- View: For most Git users, `git history` can replace many risky interactive rebases with safer, targeted edits.  
- Impact: Teams using stacked branches or long-lived feature work gain cleaner histories with fewer “oops, rebase broke everything” moments.  
- Watch next: Support for merges, first-class conflicts, and richer undo/operation logging would close more of the gap with `jj`.
