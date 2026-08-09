# Improved Git Diffs with Delta, Fzf and a Little Shell Scripting

- Score: 115 | [HN](https://news.ycombinator.com/item?id=47503687) | Link: https://nickjanetakis.com/blog/awesome-git-diffs-with-delta-fzf-and-a-little-shell-scripting

### TL;DR

Nick Janetakis combines Delta, fzf, and a small `gd` shell script to make Git reviews easier in the terminal. Delta adds dual-tone word and character highlighting to `show`, `diff`, `add -p`, and `blame`; `gd` forwards normal `git diff` arguments while adding an fzf file picker and optional side-by-side view, so branch, staged, and remote comparisons require no new command syntax. HN readers recommended Difftastic for syntax-aware changes and discussed entity-level diffs, local PR-review interfaces, and whether renewed interest in terminal tooling improves accessibility or dilutes composable Unix conventions.

### Comment pulse

- Difftastic’s syntax trees suppress irrelevant line noise — counterpoint: unsupported languages and missing context still limit integration with Delta.
- Entity-level tools classify changed functions and dependency blast radius, but reviewers still need line detail to understand how behavior changed.
- Veteran terminal users welcome fresh attention and better TUIs — counterpoint: some fear GUI imitation erodes shared, composable Unix language.

### LLM perspective

- **View:** The script preserves Git’s argument model while adding navigation, keeping adoption cost nearly zero.
- **Impact:** Faster human review matters more as agents generate larger diffs, especially when reviewers remain accountable for correctness.
- **Watch next:** Delta-Difftastic interchange, entity-context standards, local threaded review tools, and reliable patch-output compatibility.
