# Electron-based apps cause system-wide lag on macOS 26 Tahoe

- Score: 235 | [HN](https://news.ycombinator.com/item?id=45376977) | Link: https://github.com/electron/electron/issues/48311

### TL;DR

An Electron issue reports severe system-wide stuttering on macOS 26 Tahoe when visible apps such as Discord and VS Code are open, despite low CPU and GPU use; minimizing them reportedly restores smoothness. Discussion complicates attribution: similar Tahoe problems affect non-Electron apps, and participants distinguish separate GPU and autofill issues. One investigation points to Electron overriding a private AppKit method for custom visual effects, with a temporary setting-based mitigation pending downstream patches. Commenters criticized both private-API dependence and Apple’s release testing.

### Comment pulse

- Visibility triggers the reported slowdown → open windows cause stutter while minimizing affected applications removes it.
- Root causes may be mixed → commenters warn that GPU load and autofill leaks are separate bugs.
- Private APIs create brittle coupling → Electron’s UI customization can fail when undocumented AppKit behavior changes.

### LLM perspective

- View: This looks like an ecosystem compatibility failure, not generic evidence that Electron always causes lag.
- Impact: Widely used productivity apps can degrade the entire desktop until framework patches propagate.
- Watch next: Confirm root-cause traces, upstream fixes, affected Electron versions, and safe removal of temporary workarounds.
