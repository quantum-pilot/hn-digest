# Oh My Zsh adds bloat

- Score: 301 | [HN](https://news.ycombinator.com/item?id=46562790) | Link: https://rushter.com/blog/zsh-shell/

### TL;DR
The author argues that Oh My Zsh (OMZ) adds noticeable startup latency (hundreds of milliseconds per tab) because it interprets lots of shell scripts and checks for updates, which hurts workflows that open many terminals. They show a minimal zsh setup plus a Starship prompt and fzf-based history search yielding ~0.07s startup versus ~0.38s with a typical OMZ + plugins combo and much lower first-prompt lag in zsh-bench. HN commenters split between valuing OMZ’s convenience and preferring lighter, faster setups or alternative shells.

---

### Comment pulse
- OMZ as turnkey productivity → instant, decent shell on any machine beats hand-tuning configs—counterpoint: maintain dotfiles or use Starship for similar convenience minus lag.  
- Performance debate → some measure OMZ as effectively instant; others report 200–600 ms lag and note heavy plugins and poor benchmarking methods skew results.  
- Alternatives and ergonomics → people advocate Zimfw, zsh4humans, fish + Starship; discussion also diverges on vi-mode vs readline keybindings for efficient command editing.

---

### LLM perspective
- View: OMZ is great as training wheels, but serious terminal-heavy users benefit from trimming plugins or rolling minimal configs.  
- Impact: Frequent tab openers, tmux users, and remote-shell workers gain most from sub-100 ms startup and consistent, portable setups.  
- Watch next: More “batteries-included but lean” shells/frameworks, standardized startup benchmarks, and distro defaults that favor fast prompts over feature-heavy bundles.
