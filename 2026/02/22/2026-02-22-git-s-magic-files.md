# Git's Magic Files

- Score: 104 | [HN](https://news.ycombinator.com/item?id=47111218) | Link: https://nesbitt.io/2026/02/05/git-magic-files.html

### TL;DR
This post catalogs “magic” Git-related files that live in the repository (not just `.git/`) and shape behavior: ignoring files, attributes, LFS, submodules, identity mapping, blame noise, commit templates, forge configs, and cross-tool dotfiles like `.editorconfig`, language-version files, and `.dockerignore`. It argues that any tool operating on Git repos should honor these files when walking trees, rendering diffs, or showing authorship. HN comments correct a few factual errors and add practical tips for local ignores and blame configuration.

### Comment pulse
- .gitignore misunderstanding → Web UIs still show tracked-but-now-ignored files; ignore rules govern untracked status only — counterpoint: this obvious mistake made some readers abandon the article.  
- Local-only ignores → `.git/info/exclude` is ideal for personal or tool directories (e.g. `.jj/`) you never want tracked but also don’t want in `.gitignore`.  
- Blame and identity details → `.git-blame-ignore-revs` can break blame if globally configured; Git ≥2.52 adds an optional flag; GitHub graphs still ignore `.mailmap`.

### LLM perspective
- View: Treat repos as “behavioral manifests”; tools that skip these files will misreport state, authorship, or binary/generated status.  
- Impact: Git frontends, code search, and CI tools gain trust by mirroring Git’s own semantics for ignores, attributes, and identity.  
- Watch next: Shared libraries and compliance test suites to validate correct handling of ignore, attributes, mailmap, and blame-ignore across tooling.
