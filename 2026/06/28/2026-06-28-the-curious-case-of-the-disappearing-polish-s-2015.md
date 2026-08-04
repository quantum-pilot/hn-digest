# The curious case of the disappearing Polish S (2015)

- Score: 200 | [HN](https://news.ycombinator.com/item?id=48706814) | Link: https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/

### TL;DR

Medium’s editor once swallowed Polish Ś because four histories collided: Poland’s imported American keyboards popularized an Alt-based programmer layout; Windows represents Right Alt/AltGr as Ctrl+Alt; users developed a reflexive Ctrl+S save habit; and Medium intercepted any Ctrl+S event to suppress the browser dialog. Thus AltGr+S looked like Ctrl+Alt+S and `preventDefault()` erased the character. The fix excluded events carrying Alt. HN praised the cultural debugging story but noted the handler still overmatches Command+Alt+S and argued shortcut APIs should support exact modifier combinations. Similar Copilot conflicts show the internationalization trap persists.

### Comment pulse

- Shortcut matching should be exact → manual modifier checks invite extra-key collisions; a normalized combination property could make intent explicit.
- More interception can worsen accessibility → richer keyboard hooks simplify shortcuts — counterpoint: developers already override fundamental behavior without testing international layouts.
- The bug class remains current → Copilot reportedly captures AltGr+C used for Polish Ć and Hungarian ampersands, interrupting typing even during exams.

### LLM perspective

- **View:** Keyboard events encode platform history, not universal intent; shortcut code must treat layouts and input methods as first-class.
- **Impact:** International users lose characters or trigger commands; teams face bugs invisible to English-only keyboards and test suites.
- **Watch next:** Test AltGr, Option, dead keys, IMEs, normalization, shortcuts, and exact modifier sets across Windows, macOS, Linux, and browsers.
