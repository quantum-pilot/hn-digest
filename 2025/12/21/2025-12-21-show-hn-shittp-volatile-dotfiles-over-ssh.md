# Show HN: Shittp – Volatile Dotfiles over SSH

- Score: 113 | [HN](https://news.ycombinator.com/item?id=46344381) | Link: https://github.com/FOBshippingpoint/shittp

### TL;DR
Shittp is a small POSIX-shell wrapper around SSH that lets you carry your own dotfiles (.profile, .vimrc, .tmux.conf, etc.) into a remote session without leaving anything behind. It tars and base64‑encodes a configurable dotfiles directory, passes it as the SSH remote command, unpacks into a temporary directory on the remote, initializes an adjusted shell (aliases, config paths), then cleans up when you disconnect. HN discussion praises the idea but notes many equivalent one‑liners and alternative workflows already exist.

---

### Comment pulse
- Nice idea, but niche → Many users rarely SSH into machines where leaving dotfiles is a problem; tmux/screen plus persistent dotfiles are usually fine.  
- You can DIY with a line or two → mktemp + rsync or scp + trap achieve similar ephemeral homes with less tooling — counterpoint: shittp adds portability, options, and friendlier UX.  
- Heavier alternatives exist → Some bundle a full statically linked toolbox and rsync/activate it, or use sshrc-like tools; shittp is a lighter, config‑only variant.

---

### LLM perspective
- View: This is a focused, pragmatic improvement over ad‑hoc shell snippets for people who often SSH into “foreign” machines.
- Impact: Most useful for consultants, SREs, and developers frequently touching coworkers’ boxes or ephemeral CI/containers.
- Watch next: Benchmarks for large configs vs ARG_MAX, Windows/BusyBox quirks, and integrations with tools like sshrc or devbox.
