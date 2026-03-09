# Agent Safehouse – macOS-native sandboxing for local agents

- Score: 230 | [HN](https://news.ycombinator.com/item?id=47301085) | Link: https://agent-safehouse.dev/

### TL;DR
Agent Safehouse is a macOS-only, shell-script sandbox for local LLM/code agents that enforces a deny-by-default filesystem policy at the kernel level. It auto-detects your project root, grants read/write there, limited read access to toolchains, and blocks most of `$HOME` (SSH keys, other repos, personal files). It’s tuned for common agents and easy to auto-wrap via shell functions. HN discussion praises the practicality and minimalism, while noting gaps around configs, debugging tools, credentials, and broader, multi-dimensional agent safety.

---

### Comment pulse
- Tool is a thin, thoughtful wrapper over sandbox-exec policies; presets and Bash-only design are valued, but users still want overlay/COW-style isolation for configs.  
- Author emphasizes local, non-container agents and shares per-agent permission research; users like it but hit issues with home-dotfiles and limited process-control tools.  
- Many see sandboxing as the key blocker for serious agent use; filesystem sandboxes miss credentials, network, and costs—counterpoint: full safety may fundamentally conflict with capability.

---

### LLM perspective
- View: This hits a pragmatic sweet spot: OS-native, no daemons/VMs, yet materially lowers “oops rm -rf” risk for everyday agents.  
- Impact: Individual developers and small teams running “full-auto” agents locally gain a safer default without adopting containers or complex orchestration.  
- Watch next: Credential mediators, finer-grained process/network policies on macOS, and cross-platform equivalents that combine filesystem, secrets, and cost controls.
