# Scripts I wrote that I use all the time

- Score: 414 | [HN](https://news.ycombinator.com/item?id=45670052) | Link: https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/

TL;DR
Engineer shares a grab bag of everyday shell helpers—clipboard wrappers, temp dirs, safe trash, static file server fallbacks, yt-dlp downloaders, JSON/quote tools, REPL launchers, timers/notifications, media utilities, and process controls—each with concrete examples and how often he uses them. Emphasis on simple wrappers over native tools, cross‑platform macOS/Linux, and composability. HN readers applaud the clarity and frequencies, but propose built‑ins (trash, jq, uuidgen, sed) and debate customization versus a vanilla shell. Others contribute small scripts, naming patterns, and history‑driven pruning.

Comment pulse
- Use native tools over wrappers → fewer deps, consistent behavior, often faster; e.g., trash, jq, uuidgen, sed — counterpoint: wrappers smooth cross‑OS quirks/ergonomics.
- Customization arc: heavy dotfiles early, vanilla later → simpler maintenance/portability; complex tasks move to Python/Go — counterpoint: selective tools (fzf, atuin) still pay off.
- Experimentation yields new workflows → making uncommon tasks cheap can reshape habits; share scripts (highlight, dehex), naming with leading comma, prune unused via history.

LLM perspective
- View: Bundle scripts into a portable toolbox with installer, unit tests, and fallbacks; reduce reliance on ambiguous system defaults.
- Impact: Faster day‑to‑day flows for individual devs; teams adopt shared, minimal helpers without forcing heavy dotfile frameworks.
- Watch next: Compare against built‑ins, measure maintenance cost, ensure cross‑OS parity; consider packaging via Homebrew/AUR and signed archives.
