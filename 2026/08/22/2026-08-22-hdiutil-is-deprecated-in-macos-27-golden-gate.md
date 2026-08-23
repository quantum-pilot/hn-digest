# hdiutil is deprecated in macOS 27 Golden Gate

- Score: 179 | [HN](https://news.ycombinator.com/item?id=49402741) | Link: https://lapcatsoftware.com/articles/2026/8/7.html

### TL;DR

macOS 27’s beta documentation deprecates `hdiutil` in favor of `diskutil image`, whose renamed subcommands cover most disk-image operations but omit several automation and source-folder options. In one encrypted home-backup test, the replacement ran in 40–45 seconds versus 110–115 and produced a slightly smaller image. However, it failed opaquely on a root-owned file instead of requesting authentication, gave sparse diagnostics, and silently skipped Trash content. Commenters expect deprecation may mean stagnation rather than removal, citing Apple tools that remain available for years.

### Comment pulse

- Long-deprecated Apple tools often persist → `xip`, sandboxing interfaces, and old `launchctl` commands suggest scripts may keep working.
- Replacement gaps look intentional or underprioritized, not unaffordable → commenters debated maintenance choices rather than technical capability.
- Apple’s feedback process discourages volunteers → repeated, mismatched diagnostic requests leave bug status opaque.

### LLM perspective

- View: The replacement shows meaningful speed gains, but behavioral compatibility and diagnosability matter more than matching subcommand names.
- Impact: Backup tools and scripts need migration testing for permissions, exclusions, parseable progress, and every relied-upon legacy option.
- Watch next: Later macOS 27 betas, documented option parity, authentication behavior, stable machine-readable progress, and any removal timeline for `hdiutil`.
