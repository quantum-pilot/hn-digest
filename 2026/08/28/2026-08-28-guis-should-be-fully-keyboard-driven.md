# GUIs should be fully keyboard-driven

- Score: 758 | [HN](https://news.ycombinator.com/item?id=49479837) | Link: https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html

### TL;DR

The author rejects keyboard control as an inherent advantage of terminal interfaces: graphical applications can expose every action through predictable focus movement and shortcuts while retaining pointer input for tasks that need it. GNOME’s guidance explicitly requires equivalent keyboard access, and the author reports implementing broad shortcuts in a first GUI application. Commenters connect this to disability access and power-user efficiency, arguing that native frameworks once supplied sensible tab order and menus by default, whereas many modern applications omit or break those conventions.

### Comment pulse

- Accessibility testing with screen readers and no mouse benefits disabled users while often improving workflows for everyone.
- Some reject mandatory keyboard learning — counterpoint: full keyboard access should remain optional alongside mouse interaction.
- Discoverability requires visible menu shortcuts, logical tab order, remapping, documentation, and platform conventions rather than hidden key combinations.

### LLM perspective

- View: Keyboard completeness is an accessibility baseline and efficiency option, not a demand that every user abandon pointing devices.
- Impact: Better focus management helps disabled users, repetitive commercial workflows, testing automation, and temporary hardware failures.
- Watch next: Add no-mouse test days, inspect accessibility trees, verify tab order, and track regressions across framework upgrades.
