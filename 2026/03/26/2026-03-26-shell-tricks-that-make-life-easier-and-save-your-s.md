# Shell Tricks That Make Life Easier (and Save Your Sanity)

- Score: 516 | [HN](https://news.ycombinator.com/item?id=47525243) | Link: https://blog.hofstede.it/shell-tricks-that-actually-make-life-easier-and-save-your-sanity/

## TL;DR
The article is a tour of practical shell tricks that dramatically speed up interactive work: Emacs-style line editing (`Ctrl+A/E`, `Ctrl+U/K/W`, `Alt+B/F`), terminal recovery (`reset`), navigation helpers (`cd -`, `pushd/popd`), safe truncation with `>file`, last-argument reuse via `$_`, and safer scripting with `set -euo pipefail`. Bash/Zsh extras include history search (`Ctrl+R`), `sudo !!`, editing commands in `$EDITOR`, brace expansion, process substitution, globstar, backgrounding/disowning jobs, and logging with `|& tee`. HN comments add better history search, vi-mode, creative pipeline commenting, and caveats around `Ctrl+W` in browsers.

---

## Comment pulse
- Prefix-based history via remapped arrows or `fzf` → narrows history to matching commands, making `up` search contextual instead of linear — counterpoint: many rely solely on `Ctrl+R`.
- Vi-mode/readline vi in shells → gives Vim users modal editing and `$EDITOR` integration for complex commands; Emacs-mode fans stick to default keybindings and `Ctrl+X Ctrl+E`.
- Tiny helper scripts and word-boundary tweaks → `#` as a passthrough `cat` to “comment out” pipeline stages; tuning `$WORDCHARS` and avoiding `Ctrl+W` tab-closures in browsers.

---

## LLM perspective
- View: These patterns are high‑leverage; mastering 5–10 yields disproportionate productivity gains in daily CLI work.
- Impact: Developers, SREs, and ops teams gain safer scripts, faster navigation, and fewer copy‑paste mistakes in complex commands.
- Watch next: Shell distributions could ship opinionated defaults: vi-mode options, fzf history search, sane word boundaries, and safer `set -euo pipefail` templates.
