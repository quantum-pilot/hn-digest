# .gitignore Everything by Default

- Score: 171 | [HN](https://news.ycombinator.com/item?id=49576258) | Link: https://packagemain.tech/p/gitignore-everything-by-default

### TL;DR

The author proposes starting `.gitignore` with `*`, then explicitly unignoring approved file patterns, reversing Git’s usual allow-by-default behavior. A Go example permits source files, module metadata, the README, and `.gitignore`, reducing accidental commits of secrets, dependencies, editor state, or generated files. The tradeoff is silent omission: new legitimate file types may never appear in status. Most commenters preferred selective staging, status review, project templates, or global ignore rules, while some found allowlisting ergonomic for narrowly structured repositories.

### Comment pulse

- Critics considered forgotten legitimate files more likely than accidental commits and preferred reviewing `git status` before staging.
- Selective `git add`, patch mode, and global ignores address local clutter without hiding project files from collaborators.
- Debate over agent instruction files separated shared project rules from developer-specific preferences and generated artifacts.

### LLM perspective

- View: Deny-by-default trades visible clutter for invisible omissions, shifting rather than eliminating review risk.
- Impact: Stable, homogeneous repositories benefit most; evolving projects may silently miss new assets, migrations, or configuration.
- Watch next: Test the pattern in CI by detecting required ignored files and auditing exceptions during reviews.
