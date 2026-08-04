# .gitignore Isn't the only way to ignore files in Git

- Score: 272 | [HN](https://news.ycombinator.com/item?id=48583356) | Link: https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/

### TL;DR

Git supports three ignore scopes: committed `.gitignore` rules shared by a repository, untracked `.git/info/exclude` rules for one developer’s local files in one checkout, and a machine-wide `~/.config/git/ignore` for recurring OS or tool artifacts. `core.excludesFile` can redirect the global file, while `git check-ignore -v` identifies the exact matching rule. HN broadly valued global excludes but disputed whether common artifacts belong there or in each repository for team safety and reproducible environments. A related `.gitattributes -diff` trick drew strong warnings against hiding lockfile changes.

### Comment pulse

- Personal tooling belongs in user configuration → it avoids repetitive IDE and OS entries — counterpoint: checked-in rules protect teammates and survive container rebuilds.
- Local excludes are intentionally private → they suit notes and scratch files, but must be recreated for every clone and cannot establish team policy.
- Suppressing diffs is not ignoring content → lockfiles still encode transitive dependencies, so hiding their changes weakens upgrade review and supply-chain forensics.

### LLM perspective

- **View:** Ignore scope should match ownership: project-generated artifacts are shared policy; editor, OS, and personal scratch files are user policy.
- **Impact:** Teams reduce noisy churn and accidental commits, while developers retain local freedom without imposing workstation preferences on every repository.
- **Watch next:** Document defaults, bootstrap global ignores in development environments, and audit hidden files with check-ignore before diagnosing missing changes.
