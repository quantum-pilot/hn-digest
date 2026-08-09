# Writing my own text editor, and daily-driving it

- Score: 217 | [HN](https://news.ycombinator.com/item?id=47331034) | Link: https://blog.jsbarretto.com/post/text-editor

### TL;DR

After finding no existing editor that matched his workflow, the author spent two years building a personalized Rust TUI and began daily-driving it as soon as it could barely edit files. Forced use, logging every annoyance, and fixing blocking issues accelerated the project to roughly 10,000 lines, mostly in six months. It now offers fast fuzzy file discovery, a custom context-aware regex engine, demand-driven syntax highlighting, multithreaded project search, terminal panes, and damage-only rendering. Commenters echo that long-lived personal editors repay effort through fit, learning, productivity, and joy.

### Comment pulse

- Dogfooding creates a compounding roadmap → real friction supplies prioritized tasks, while each fix makes continued development easier.
- Simple ranking beat elaborate fuzzy metrics → prefixes, substrings, case, and recent access put desired files near the top after two keystrokes.
- Build versus borrow remained pragmatic → the author wrote regex for custom semantics but reused Alacritty’s mature terminal core.

### LLM perspective

- **View:** Personal software can rationally ignore generality when one committed user supplies continuous feedback.
- **Impact:** Engineers gain deeper systems knowledge but accept Unicode, portability, maintenance, and onboarding gaps.
- **Watch next:** Buffer scaling, grapheme support, crash recovery, plugin pressure, and whether hard-coded preferences remain sufficient.
