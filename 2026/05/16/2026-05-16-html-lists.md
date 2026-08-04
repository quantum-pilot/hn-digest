# HTML Lists

- Score: 276 | [HN](https://news.ycombinator.com/item?id=48161861) | Link: https://blog.frankmtaylor.com/2026/05/13/you-dont-know-html-lists/

### TL;DR

The article presents five semantic list patterns and a decision rule: use select/option or input/datalist for form choices, ol when reordering changes meaning, dl for term–value relationships, menu for action controls, and ul as the remaining default. It highlights lesser-known features including optgroup, hr inside select, datalist on non-text inputs, ol start and reversed, and dl wrappers for metadata. HN appreciated the depth but found native controls inconsistent: datalist and disabled optgroups fail or degrade across Safari, Firefox Android, and keyboard combinations, weakening their appeal versus custom components.

### Comment pulse

- Native semantics reduce ARIA and custom code → built-in controls convey roles automatically — counterpoint: implementation gaps can make behavior device-dependent.

- Datalist remains narrowly useful → autocomplete works for some users, but incomplete suggestion browsing, weak styling hooks, and compatibility failures block richer comboboxes.

- Abstraction versus fundamentals stays unresolved → semantic HTML can replace React components, while framework supporters prioritize predictable cross-browser behavior over mastering evolving specifications.

### LLM perspective

- **View:** Semantic element choice encodes meaning for accessibility and tooling, but semantics deliver value only when browser implementations are trustworthy.

- **Impact:** Teams need progressive enhancement: native markup first, explicit support matrices, and custom fallbacks only for requirements browsers cannot meet.

- **Watch next:** Test datalist discovery, optgroup disabling, keyboards, screen readers, range labels, and lint enforcement across supported browser-device pairs.
