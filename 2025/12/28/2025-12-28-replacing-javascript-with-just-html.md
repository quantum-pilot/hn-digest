# Replacing JavaScript with Just HTML

- Score: 678 | [HN](https://news.ycombinator.com/item?id=46407337) | Link: https://www.htmhell.dev/adventcalendar/2025/27/

### TL;DR

Modern HTML can replace JavaScript for common interface patterns: `details` and `summary` provide accordions, `input` plus `datalist` offers filtered suggestions, and `popover` with `popovertarget` handles overlays and offscreen navigation. Native controls reduce downloaded code, runtime work, and manual ARIA state management, leaving JavaScript for behavior the platform cannot express. HN commenters welcomed forgotten platform capabilities but criticized the article for not embedding its demonstrations and emphasized that `datalist` remains weak on mobile, styling, accessibility, labels versus values, and typo tolerance.

### Comment pulse

- Native semantics reduce machinery → browsers manage interaction state and accessibility better than many hand-built component implementations.
- `datalist` is not production-complete → inconsistent mobile behavior and limited validation or presentation often force JavaScript fallbacks.
- Ecosystem habits lag the platform → component libraries and React-centered hiring reward framework knowledge over semantic HTML fluency.

### LLM perspective

- View: “Use the platform first” is a progressive-enhancement strategy, not an ideological ban on JavaScript.
- Impact: Simpler controls can improve load cost, maintenance, and accessibility when native behavior actually matches product requirements.
- Watch next: Cross-browser interop, mobile testing, styling hooks, and accessible combobox improvements will expand viable replacements.
