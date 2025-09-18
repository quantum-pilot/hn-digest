# macOS dotfiles should not go in –/Library/Application Support

- Score: 273 | [HN](https://news.ycombinator.com/item?id=45022383) | Link: https://becca.ooo/blog/macos-dotfiles/

- TL;DR
  - Author argues macOS CLI tools shouldn’t use ~/Library/Application Support; that directory targets GUI app bundles with managed settings. Instead, follow XDG and default to ~/.config to match cross‑Unix expectations and dotfile managers. Many libs auto-choose Library on macOS, causing inconsistency. HN splits: macOS‑first folks cite Apple’s Library/Preferences guidance and note bundled tools favor home‑dotfiles, not ~/.config; cross‑platform users prefer XDG for portability. Middle ground: GUI apps → Application Support; standalone CLIs → ~/.config.

- Comment pulse
  - macOS-native stance → Library/Preferences are the documented per-user locations; CLIs are “apps,” so follow Apple’s conventions — counterpoint: many CLI tools support XDG; users expect cross-Unix consistency.
  - Cross-platform view → Use XDG for CLIs; reserve Application Support for GUI bundles. Rationale: easier dotfile syncing across macOS/Linux/BSD; aligns with Git/Vim/Emacs behavior.
  - Library maintainers debate → dirs-rs defaults to Library; devs propose forks or using etcetera/xdg. Goal: sane per-platform defaults with opt-in for app-bundle semantics.

- LLM perspective
  - View: Default to XDG on macOS for CLIs; support Application Support/Preferences only when integrating with a signed app bundle.
  - Impact: Reduces user surprise, simplifies dotfile syncing, and avoids sandbox/bundle-ID assumptions inappropriate for standalone binaries.
  - Watch next: Track shifts in platformdirs/dirs-rs defaults, Apple doc clarifications, and major CLIs adding XDG-first with env overrides.
