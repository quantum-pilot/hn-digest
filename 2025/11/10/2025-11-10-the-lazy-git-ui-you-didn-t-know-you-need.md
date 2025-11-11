# The lazy Git UI you didn't know you need

- Score: 187 | [HN](https://news.ycombinator.com/item?id=45878578) | Link: https://www.bwplotka.dev/2025/lazygit/

- TL;DR
  - Bartek Płotka explains why lazygit, a keyboard-first TUI atop native git, replaced his CLI/GUI mix: consistent panes, vim-like keys, and context-rich, guided prompts make status, rebases, conflict resolution, patching by hunk/line, commit splitting, and cherry-picks faster and safer without new abstractions. He argues great devtools emphasize simplicity, discoverability, and interactivity, and notes AI fits auxiliary tasks, not version control decisions. HN compares alternatives—jj/jjui, SourceTree/Fork/Tower/Sublime Merge/JetBrains, GitHub Desktop—debating diff quality, editor integration, and onboarding.

- Comment pulse
  - jj replaces git for many → jjui enables graph editing; some still keep lazygit for best-perceived diffs — counterpoint: weak editor integration slows fine-grained committing.
  - Traditional GUIs excel → SourceTree, Fork, Tower, Sublime Merge, Git Extensions, JetBrains praised for polished UI, hunk/line staging, speed, stability, less auto-refresh interference.
  - GitHub Desktop reduces newbie errors → clear names, easy amend/cherry-pick; onboarding-friendly — counterpoint: weak merge/conflict tooling and missing graph frustrate power users.

- LLM perspective
  - View: Lazygit wins by guiding native git tasks, not hiding them; fewer surprises than opaque GUIs or DSL-style VCS replacements.
  - Impact: Teams see safer rebases, cleaner histories, faster patch splits; CLI purists gain discoverability, juniors reduce foot-guns.
  - Watch next: Head-to-head time-to-task studies versus jj/jjui and IDEs; tighter editor integrations; standardized hunk operations across tools.
