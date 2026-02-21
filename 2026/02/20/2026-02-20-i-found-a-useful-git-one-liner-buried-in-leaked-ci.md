# I found a useful Git one liner buried in leaked CIA developer docs

- Score: 582 | [HN](https://news.ycombinator.com/item?id=47088181) | Link: https://spencer.wtf/2026/02/20/cleaning-up-merged-git-branches-a-one-liner-from-the-cias-leaked-dev-docs.html

### TL;DR
A developer found a handy Git cleanup one-liner in leaked CIA Vault7 docs: list branches already merged into the main line, then batch-delete them while protecting key branches. The post modernizes it for `main` and common workflows, wrapping it in a shell alias so `ciaclean` quickly purges stale local branches after deployments. Hacker News expands this into more robust variants that respect different default-branch names, worktrees, non-fast-forward workflows, and interactive selection via tools like fzf.

---

### Comment pulse
- Vault7 context → The Git tip is trivial, but the leaked docs reveal elaborate CIA tooling like “Fine Dining” USB exfiltration apps—raising interest beyond Git alone.  
- Safer automation → Users share extended aliases that detect the real default branch, avoid active/worktree branches, prune gone remotes, and integrate fzf for interactive deletion — counterpoint: relying on `init.defaultBranch` can misfire across repos.  
- Workflow edge cases → `git branch --merged` fails with squash/rebase merges; people instead track remote-branch deletion, age thresholds, or `git gone`-style aliases to avoid losing work.

---

### LLM perspective
- View: The real value is encoding cleanup as repeatable aliases, not the specific pipeline; automation beats memorizing fragile one-liners.  
- Impact: Teams with many short-lived feature branches gain clearer `git branch` output, less cognitive load, and fewer mistakes when switching or backporting.  
- Watch next: Git itself could expose higher-level “prune merged/gone branches” commands, informed by common alias patterns seen in dotfiles.
