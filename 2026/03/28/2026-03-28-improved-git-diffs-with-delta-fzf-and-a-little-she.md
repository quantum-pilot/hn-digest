# Improved Git Diffs with Delta, Fzf and a Little Shell Scripting

- Score: 115 | [HN](https://news.ycombinator.com/item?id=47503687) | Link: https://nickjanetakis.com/blog/awesome-git-diffs-with-delta-fzf-and-a-little-shell-scripting

### TL;DR
The post shows how to modernize command-line Git diffs using `delta` as a pager and a small wrapper script. By setting one env var and a few `.gitconfig` options, standard commands (`git diff`, `show`, `add -p`, `blame`) gain side‑by‑side, word‑level highlighting and nicer colors. A custom `gd` script combines `git diff` with `fzf` to jump between changed files, supports all `git diff` flags, and even pretty-prints `ripgrep`’s JSON output. Dotfiles and a demo video are provided.

---

### LLM perspective
- View: This is a focused developer-experience tweak: small shell glue yielding disproportionate usability gains in everyday Git workflows.  
- Impact: Most valuable to terminal-heavy engineers reviewing PRs locally, or working in large, frequently changing codebases.  
- Watch next: Standardized “diff TUI” wrappers in team dotfiles, plus benchmarks on review speed and error rates with enhanced diffs.
