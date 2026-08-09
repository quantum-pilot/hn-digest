# Using coding assistance tools to revive projects you never were going to finish

- Score: 148 | [HN](https://news.ycombinator.com/item?id=47902525) | Link: https://blog.matthewbrunelle.com/its-ok-to-use-coding-assistance-tools-to-revive-the-projects-you-never-were-going-to-finish/

### TL;DR

Matthew Brunelle used Claude Code with Opus 4.6 to rebuild an abandoned YouTube Music-to-OpenSubsonic shim in one evening. A supplied API specification, chosen stack, coding conventions, iterative planning, client logs, and regression tests helped cover the 80-endpoint long tail, including caching, SQLite metadata, and streamed-file cleanup. He argues assistants fit personal tools users want but would never finish, while separate stretch projects should preserve learning. Hacker News readers reported similar revivals in games and utilities, though some flagged fragile generated assets, code quality, and cases where existing automation already suffices.

### Comment pulse

- Clear specifications and fast feedback made assistance effective; repeated testing caught undocumented client expectations such as `.view` endpoint suffixes.
- Personal utilities tolerate rough internals when they finally solve a persistent need — counterpoint: built-in automation may eliminate the project entirely.
- Revived games and apps restored creative momentum, although generated engine files and increasingly complex projects still exceed agent reliability.

### LLM perspective

- **View:** Abandoned projects are unusually safe proving grounds because their baseline value is zero and the owner supplies domain judgment.
- **Impact:** Solo builders can convert neglected ideas into bespoke software without surrendering every learning-oriented project.
- **Watch next:** Maintenance after model changes, security omissions, dependency breakage, test depth, and whether revived tools remain used.
