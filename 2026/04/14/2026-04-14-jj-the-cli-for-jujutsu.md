# jj – the CLI for Jujutsu

- Score: 479 | [HN](https://news.ycombinator.com/item?id=47763759) | Link: https://steveklabnik.github.io/jujutsu-tutorial/introduction/what-is-jj-and-why-should-i-care.html

### TL;DR

Jujutsu’s `jj` CLI presents a simpler, composable DVCS model with Git-compatible storage, letting individuals experiment without forcing a team-wide migration. Its working copy is always a mutable commit; cheap snapshots, `new`, `squash`, `split`, `absorb`, operation logs, and automatic rebasing support fluid revision workflows. Commenters praised easy undo and experimentation but warned that `edit` can unexpectedly rewrite earlier work. Git interoperability also has limits: mixing both interfaces, or relying on LFS, submodules, hooks, and Git-only operations, can cause friction.

### Comment pulse

- Git-style users can commit after editing; others create anonymous snapshots, then squash or split them once the change’s shape becomes clear.
- `jj edit` is widely viewed as a footgun; using `jj new` keeps experiments isolated, while `jj undo` recovers mistakes.
- Git backing eases adoption, but commenters recommend one primary interface per worktree. — counterpoint: it remains valuable for migration and deployment.

### LLM perspective

- View: Jujutsu’s advantage is a safer history-editing model, not merely shorter commands.
- Impact: Teams must define bookmarks, shared immutability, and which client owns repository mutations.
- Watch next: Better Git-coexistence guidance and edge-case support could determine broader adoption.
