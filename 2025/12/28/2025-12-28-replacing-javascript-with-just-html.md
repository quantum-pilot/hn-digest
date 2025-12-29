# Replacing JavaScript with Just HTML

- Score: 678 | [HN](https://news.ycombinator.com/item?id=46407337) | Link: https://www.htmhell.dev/adventcalendar/2025/27/

- TL;DR  
Modern HTML and CSS can now handle many UI patterns once implemented with JavaScript—accordions, autocomplete inputs, modals, and off‑canvas navigation—using elements like details/summary, datalist, and the popover API. The article argues this reduces JS payloads and complexity while improving performance and accessibility when browser support is adequate. HN readers celebrate underused platform features, especially details/summary, but criticize datalist’s weak UX and spotty mobile support, and note that industry hiring still heavily rewards framework skills over semantic HTML mastery.

- Comment pulse  
  - Native HTML components beat JS widgets → details/summary, popover, dialogs, etc. simplify ARIA and behavior, and even integrate with browser search and Markdown tools.  
  - datalist falls short for production UX → no fuzzy search, sublabels, styling control, reliable mobile behavior, or select-like constraints — counterpoint: OK as progressive enhancement.  
  - Industry incentives favor JS frameworks → interviews emphasize React hooks and CSS-in-JS, so developers underinvest in semantic HTML and newer built-in browser capabilities.

- LLM perspective  
  - View: Treat HTML/CSS features as first-class; reach for JS only when platform primitives truly can't express required behavior.  
  - Impact: Smaller bundles, fewer dependencies, and simpler accessibility for common widgets like accordions, menus, dialogs, and searchable lists.  
  - Watch next: standardize richer combobox primitives, improve mobile popover support, and publish benchmarks comparing native patterns against popular framework components.
