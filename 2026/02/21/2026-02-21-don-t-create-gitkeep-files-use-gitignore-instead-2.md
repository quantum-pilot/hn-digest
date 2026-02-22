# Don't create .gitkeep files, use .gitignore instead (2023)

- Score: 122 | [HN](https://news.ycombinator.com/item?id=47094877) | Link: https://adamj.eu/tech/2023/09/18/git-dont-create-gitkeep/

### TL;DR

Git can’t track empty directories, so people often add dummy `.gitkeep` files plus root-level `.gitignore` rules. The article argues this is clunky and confusing, and instead recommends placing a `.gitignore` inside each such directory with `*` and `!.gitignore` so Git tracks the directory via that file alone, surviving renames. Hacker News discusses the historical spread of `.gitkeep`, nitpicks the suggested command and `.gitignore` semantics, and debates whether build/output directories should be versioned at all.

---

### Comment pulse

- `.gitkeep` usage is old and widespread (Rails, Stack Overflow). Some teams prefer central `.gitignore` + `.gitkeep` over many scattered `.gitignore` files.

- Debate over `.gitignore` semantics: un-ignoring `.gitignore` vs `git add -f .gitignore`; templates favor self-excepting patterns to avoid teaching special commands.

- Several argue build directories shouldn’t be committed; instead let the build system create them or use a `README.md` as a human-friendly placeholder—counterpoint: `.gitkeep` feels simpler.

---

### LLM perspective

- View: Use per-directory `.gitignore` only when templates/tools must ensure directories exist; otherwise let builds create them.

- Impact: Project generators, frameworks, and large repos should standardize on one convention to avoid confusion and sprawl.

- Watch next: Tooling could offer “track empty dir” helpers; Git might eventually add first-class support or clearer guidance.
