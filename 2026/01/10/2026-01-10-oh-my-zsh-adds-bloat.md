# Oh My Zsh adds bloat

- Score: 301 | [HN](https://news.ycombinator.com/item?id=46562790) | Link: https://rushter.com/blog/zsh-shell/

### TL;DR

The author attributes a 0.38-second Zsh startup to Oh My Zsh and replaces it with built-in history/completion settings, Starship, fzf, and Vim bindings, reporting 0.07 seconds afterward. The recommendation is to begin with a minimal configuration and add only required features, especially for workflows that constantly create tmux panes or terminal tabs. HN discussion split over whether convenience outweighs latency, suggested Fish, Zim, dotfiles, or zsh4humans, and challenged the benchmark’s shell mode, repository context, and diagnostic rigor.

### Comment pulse

- Ready-made value → OMZ gives consistent behavior on fresh hosts — counterpoint: synchronized dotfiles or lighter frameworks can do likewise.
- Fish advocates → Strong defaults and completions reduce configuration work, though non-POSIX behavior limits some scripting patterns.
- Measurement concerns → Login versus interactive mode, Git-aware plugins, and profiling method can materially change startup results.

### LLM perspective

- View: Plugin selection and initialization paths matter more than framework labels; profile the workload users actually feel.
- Impact: High-churn terminal users benefit most from trimming latency, while occasional users may favor turnkey consistency.
- Watch next: Repeatable first-prompt and first-command benchmarks across identical plugins, repositories, and hardware.
