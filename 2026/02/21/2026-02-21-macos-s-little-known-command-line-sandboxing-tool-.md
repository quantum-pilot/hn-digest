# macOS's Little-Known Command-Line Sandboxing Tool (2025)

- Score: 185 | [HN](https://news.ycombinator.com/item?id=47101200) | Link: https://igorstechnoclub.com/sandbox-exec/

### TL;DR

macOS includes sandbox-exec, a command-line front end to Seatbelt that runs a process under a Scheme-like sandbox profile. Profiles can deny everything then allow required files, execution, and network operations, or permit most behavior while blocking selected resources. The article demonstrates restricted shells, system profiles, aliases, and violation logs, while warning that complex GUI applications require trial and error. Commenters emphasized that Apple has deprecated the tool for nearly a decade, although Codex, Claude Code, Swift tooling, and community wrappers still rely on it.

### Comment pulse

- Deprecation raised longevity concerns — counterpoint: cron illustrates that deprecated macOS tools can remain operational for decades.
- Developers valued explicit profiles for coding agents, especially when they want stricter boundaries than consent-based escape mechanisms.
- Policy debugging remains technical because user-space SBPL compilation feeds kernel enforcement and blocked operations must be traced through logs.
