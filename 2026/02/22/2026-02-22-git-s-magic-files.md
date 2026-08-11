# Git's Magic Files

- Score: 104 | [HN](https://news.ycombinator.com/item?id=47111218) | Link: https://nesbitt.io/2026/02/05/git-magic-files.html

### TL;DR

The post catalogs committed files that alter Git or adjacent tooling: `.gitignore`, `.gitattributes`, `.lfsconfig`, `.gitmodules`, `.mailmap`, blame-ignore lists, commit templates, forge folders, and conventions such as `.gitkeep`. It explains scope, precedence, migration caveats, and what repository tools should honor; it also covers EditorConfig, runtime-version files, and Docker ignores. HN highlighted useful local controls such as `.git/info/exclude`, while flagging factual errors about ignored tracked files, GitHub mailmaps, and blame-ignore behavior—some of which the displayed article already appears to correct.

### Comment pulse

- Ignoring does not untrack files → committed paths remain visible, and forced additions can bypass ignore rules.
- Repository-local exclusions deserve emphasis → `.git/info/exclude` protects personal scratch files without changing shared configuration.
- Portability varies → several “magic” files require per-clone setup or forge support — counterpoint: optional configuration can reduce failures.

### LLM perspective

- **View:** Tool authors should distinguish Git-native semantics from conventions and hosting-platform extensions.
- **Impact:** Correct support improves repository walking, attribution, binary handling, and submodule awareness.
- **Watch next:** Version-specific behavior, correction history, and tests across GitHub, GitLab, Gitea, and Forgejo.
