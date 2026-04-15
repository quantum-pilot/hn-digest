# jj – the CLI for Jujutsu

- Score: 479 | [HN](https://news.ycombinator.com/item?id=47763759) | Link: https://steveklabnik.github.io/jujutsu-tutorial/introduction/what-is-jj-and-why-should-i-care.html

### TL;DR
Jujutsu’s jj CLI is a git-backed distributed VCS that aims to be simpler yet more powerful than git and Mercurial. It treats commits as cheap, always-present snapshots, encouraging workflows built around `jj new`, `squash`, `split`, and automatic rebasing over a clean git history. The tutorial walks from installation through branching, sharing, stacked changes, and recovery tools like undo and operation logs, assuming prior git experience. HN discussion focuses on practical day-to-day workflows, how jj’s commit-first model changes mental habits, and tradeoffs between powerful history editing and interoperability quirks.

### Comment pulse
- Simple workflow beats model debates → use `jj` as status, commit changes, `squash` fixes, `new` for diverging work; git log stays clean, hiding jj’s machinery.  
- Commit-first model aids experimentation → `jj new` mirrors a staging area; `split` plus frequent message-less commits give undoable scratch history—counterpoint: others still prefer git’s index.  
- Auto-committing edits surprises git users → `jj edit` can rewrite history; recommended `jj new`, `undo`, op log, absorb, workspaces—plus caution that jj–git interoperability is incomplete.  

### LLM perspective
- View: jj is best evaluated on real work, not toy repos, to see if it genuinely reduces everyday version-control friction.  
- Impact: Teams may standardize on jj or git per repo; mixing tools in one directory risks history corruption and confusion.  
- Watch next: IDE integrations, command conventions, and CI/hosting support that encode jj’s concepts (change-ids, op log) rather than hiding them.
