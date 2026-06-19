# .gitignore Isn't the only way to ignore files in Git

- Score: 272 | [HN](https://news.ycombinator.com/item?id=48583356) | Link: https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/

## TL;DR
Git can ignore files at three levels: in-repo `.gitignore` (shared with everyone), per-repo `.git/info/exclude` (local-only), and a global ignore file (default `~/.config/git/ignore`, configurable via `core.excludesFile`). `git check-ignore -v` shows exactly which file/line is ignoring something. HN commenters add that `.gitattributes` can “ignore diffs” (e.g., `-diff` on large generated files) and debate where to put OS/IDE junk (`.gitignore` vs user-global), plus patterns for personal “attic” scratch directories.

---

## Comment pulse
- Use `.gitattributes` to hide noisy diffs (e.g., `package-lock.json -diff`) → cleaner reviews. — counterpoint: lockfile diffs matter for debugging and supply-chain safety.  
- Prefer per-user global ignores for OS/IDE files → cleaner repos, no project bloat. — counterpoint: repo `.gitignore` ensures nobody accidentally commits those files.  
- Store global config/ignore under `~/.config/git` and version-control it → centralized, portable Git setup with fewer dotfiles in `$HOME`.

---

## LLM perspective
- View: Treat ignore rules as layered: project policy in `.gitignore`, personal quirks in global ignore, one-off junk in `.git/info/exclude`.  
- Impact: Teams reduce noise and accidental commits; individuals keep workflows (scratch dirs, editor cruft) without polluting shared repos.  
- Watch next: Tooling that auto-suggests correct ignore location and surfaces risky patterns like hidden lockfile diffs.
