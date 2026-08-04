# The git history command

- Score: 424 | [HN](https://news.ycombinator.com/item?id=48901010) | Link: https://lalitm.com/post/git-history/

### TL;DR

Git 2.54–2.55 added experimental `git history` subcommands for safer local history editing. `fixup` folds staged changes into an older commit, `reword` changes its message, and `split` divides its hunks; each rebuilds descendant commits and moves every affected local branch atomically, refusing operations that would conflict. Limits include merge commits, no operation log, and no first-class conflicts. HN liked the higher-level interface but noted rebase already has abort/reflog safety, debated whether Git’s problem is internals or CLI design, and found rewritten signed commits lose signatures.

### Comment pulse

- Git’s difficulty polarized commenters → some said learning its object model makes everything click — counterpoint: inconsistent, mixed-level commands remain confusing.
- Graphical front ends remain competitive → TortoiseGit and Magit expose reorder, split, combine, state, and rollback without memorizing CLI options.
- Commit signing is a blocking gap → `reword` recreated signed commits without signatures, pushing security-conscious users back to interactive rebase.

### LLM perspective

- **View:** Refusing conflicts trades power for transactional predictability, a sensible default for common cleanup operations.
- **Impact:** Stacked-branch users gain cross-branch rewriting without adopting a new VCS or disturbing active worktrees.
- **Watch next:** Commit-signing support, merge-aware rewrites, conflict representation, and a stable non-experimental interface.
