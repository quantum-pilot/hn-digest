# Shell Tricks That Make Life Easier (and Save Your Sanity)

- Score: 516 | [HN](https://news.ycombinator.com/item?id=47525243) | Link: https://blog.hofstede.it/shell-tricks-that-actually-make-life-easier-and-save-your-sanity/

### TL;DR

The guide collects underused terminal shortcuts, separating broadly available habits from Bash/Zsh conveniences. Editing keys jump, cut, yank, and search command lines; `reset`, job control, directory stacks, truncation, and previous-argument reuse recover common situations. Shell-specific additions include history expansion, editor handoff, brace and process substitution, recursive globs, and combined output logging. For scripts it recommends stricter error and unset-variable handling, while warning that `set -e` has contextual traps. Its practical advice is to adopt one shortcut at a time.

### Comment pulse

- Prefix-aware up/down history search was called life-changing, with bindings shared for Zsh, Bash, and Readline; Fish provides it by default.
- Vim users favored shell vi-mode — counterpoint: others preferred default Emacs keys plus editor handoff for genuinely complex commands.
- `CTRL-W` boundaries vary by shell and configuration, and its browser meaning makes accidental tab closure a recurring hazard.

### LLM perspective

- **View:** Small editing and history habits compound more reliably than elaborate shell customization.
- **Impact:** Faster correction lowers friction, but portability claims can hide terminal, shell, and mode differences.
- **Watch next:** Shortcut discoverability, safer history expansion, cross-application conflicts, and whether modern shells improve defaults.
