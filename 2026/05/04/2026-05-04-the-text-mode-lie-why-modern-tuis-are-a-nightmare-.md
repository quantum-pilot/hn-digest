# The text mode lie: why modern TUIs are a nightmare for accessibility

- Score: 284 | [HN](https://news.ycombinator.com/item?id=48002938) | Link: https://xogium.me/the-text-mode-lie-why-modern-tuis-are-a-nightmare-for-accessibility

### TL;DR

The author argues that terminal software is not automatically accessible: linear CLIs produce a chronological stream, while modern TUIs treat character cells as a reactive grid. Framework-driven redraws move the cursor through timers, spinners, and history, causing Speakup or NVDA to announce fragments, destabilize, or lag as conversations grow. Older tools remain usable when cursor noise is disabled, focus stays single-column, or VT100 scrolling regions update minimally. HN largely agreed that many TUIs emulate GUIs poorly, though defenders cited SSH portability, keyboard-first workflows, discoverability, and easier cross-platform distribution.

### Comment pulse

- A terminal grid is effectively a GUI canvas → screen readers need stable focus and semantic updates, not visually optimized cursor choreography.
- TUIs offer practical distribution advantages → they work over SSH, launch beside shell workflows, and avoid fragmented native-GUI packaging.
- Closing stale accessibility issues may reflect backlog semantics → counterpoint: corporate maintainers still leave affected users without a roadmap or usable product.

### LLM perspective

- **View:** Accessibility requires an explicit rendering contract; character output alone provides no semantic structure.
- **Impact:** Framework authors need reduced-motion, no-spinner, cursor-stable, transcript, and screen-reader modes as first-class capabilities.
- **Watch next:** Screen-reader regression tests, redraw-volume benchmarks, accessible-mode adoption in Gemini CLI, and documented terminal semantics.
