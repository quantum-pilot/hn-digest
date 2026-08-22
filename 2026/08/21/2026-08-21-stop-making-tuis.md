# Stop Making TUIs

- Score: 335 | [HN](https://news.ycombinator.com/item?id=49384210) | Link: https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/

### TL;DR

After generating SwiftUI tools with coding agents, the author argues that cheap native-interface creation weakens the case for new TUIs. Terminal interfaces impose constraints on scrolling, selection, drag-and-drop, windows, images, and accessibility; native widgets provide them by default. CLIs remain essential for composition and remote operation, while cross-platform consistency is the strongest TUI advantage. The claim is Mac-focused and concerns personal tools, not untested shipping. Commenters defended keyboard speed, density, portability, theming, and remote sessions; others noted that many celebrated shell workflows are CLIs, not TUIs.

### Comment pulse

- TUI advocates prized keyboard efficiency, information density, portability, theming, and SSH sessions; counterpoint: well-designed GUIs can also be keyboard-first.
- Accessibility split the thread: some treated it as one tradeoff, while affected users called it non-negotiable.
- A modern terminal protocol could fix legacy constraints, but critics asked whether that simply recreates a GUI framework.

### LLM perspective

- View: Agents make native prototyping newly viable, but one developer’s Mac experiments do not establish cross-platform production economics.
- Impact: Teams can expose CLI engines through richer local clients without sacrificing automation or remote execution.
- Watch next: Comparable Windows and Linux results, accessibility testing, maintenance costs, and keyboard-first native designs inspired by leading TUIs.
