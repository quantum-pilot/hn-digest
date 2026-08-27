# Snitch – A friendlier ss/netstat

- Score: 290 | [HN](https://news.ycombinator.com/item?id=46361229) | Link: https://github.com/karol-broda/snitch

### TL;DR

Snitch is an MIT-licensed Go tool that presents Linux and macOS network connections through a live TUI, styled or plain tables, JSON, CSV, and streaming output. It filters by protocol, state, address family, PID, process, or port, resolves names, can watch or terminate processes, and reads Linux `/proc` data. HN readers welcome clearer defaults than `ss` or `lsof`, but note name confusion with Little Snitch, accessibility questions, and the practical advantage of `ss` already existing on servers.

### Comment pulse

- Better defaults aid diagnosis → process names and listening sockets matter more to many users than queue sizes shown by `ss`.
- Compatibility freezes old interfaces → text output doubles as an API, making improved defaults potentially breaking changes.
- Installation narrows the niche → Snitch suits workstations and homelabs, while ubiquitous `ss` remains preferable on managed fleets.

### LLM perspective

- View: Snitch adds discoverability and interaction atop familiar socket data rather than replacing foundational networking tools.
- Impact: Occasional operators can inspect connections faster, while automation retains structured and plain-output modes.
- Watch next: Test privilege behavior, macOS parity, screen-reader accessibility, performance, name-resolution delays, and packaging trust.
