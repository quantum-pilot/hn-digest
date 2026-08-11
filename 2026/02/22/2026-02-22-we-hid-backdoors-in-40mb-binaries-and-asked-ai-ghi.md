# We hid backdoors in ~40MB binaries and asked AI + Ghidra to find them

- Score: 201 | [HN](https://news.ycombinator.com/item?id=47111440) | Link: https://quesma.com/blog/introducing-binaryaudit/

### TL;DR

Quesma’s BinaryAudit benchmark gave AI agents stripped C and Rust executables containing simple, manually injected backdoors, plus clean controls, and access to Ghidra, Radare2, and binutils. Claude Opus 4.6 solved 49% of tasks, Gemini 3 Pro 44%, and Claude Opus 4.5 37%; models collectively reported nonexistent backdoors on 28% of negative tasks. Failures included aimless searching and rationalizing genuine shell execution as legitimate. Authors and commenters agree this is unsuitable for autonomous malware screening but potentially useful for human-guided first-pass reverse engineering.

### Comment pulse

- Critics expect basic import hiding and string encoding to collapse detection — counterpoint: authors position these entry-level tasks as a capability baseline.
- Practitioners reported value in file-format analysis, diagrams, attack-surface mapping, and repetitive searches when experts validate every finding.
- The open-source toolchain handled C better than Go, so benchmark results partly measure decompiler quality rather than model reasoning alone.
