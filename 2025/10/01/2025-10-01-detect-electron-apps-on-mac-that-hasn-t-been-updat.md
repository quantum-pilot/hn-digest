# Detect Electron apps on Mac that hasn't been updated to fix the system wide lag

- Score: 152 | [HN](https://news.ycombinator.com/item?id=45437112) | Link: https://gist.github.com/tkafka/e3eb63a5ec448e9be6701bfd1f1b1e58

### TL;DR

A shell script inventories macOS Electron applications that may still trigger system-wide lag on macOS Tahoe. The gist identifies patched Electron releases—36.9.2, 37.6.0, 38.2.0, 39.0.0, and later—and scans application bundles to infer embedded Electron versions or detect the implicated `_cornerMask` code. It also offers `CHROME_HEADLESS=1` as a temporary startup workaround, noting that it disables window shadows. The sample flagged applications including VS Code, Cursor, Signal, Slack, Claude, and Figma Beta at their then-installed versions.

### Comment pulse

- Users found numerous stale Electron runtimes and sometimes removed applications they no longer needed.
- Commenters noted some fixes require downloading a fresh installer rather than relying on an application’s auto-update.
- An alternative package identifies Electron builds through file fingerprints, while the gist author favored a simpler detector.

### LLM perspective

- View: Runtime inventory is valuable because application version numbers can conceal stale bundled frameworks.
- Impact: A quick local audit helps users isolate lag sources while vendors roll patched Electron releases forward.
- Watch next: Detection heuristics must track backports and apps whose installers update differently from their content.
