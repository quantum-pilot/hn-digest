# HTML Lists

- Score: 276 | [HN](https://news.ycombinator.com/item?id=48161861) | Link: https://blog.frankmtaylor.com/2026/05/13/you-dont-know-html-lists/

### TL;DR
The article argues that most developers underuse HTML’s richer list ecosystem and default to `<ul>` or custom components. It classifies “lists” into five categories: form controls (`<select>/<option>/<optgroup>`, `<input>/<datalist>`), ordered lists (`<ol>` with `reversed`/`start`), description lists (`<dl>` for key–value data and even JSON debugging), command menus (`<menu>` for toolbars), and unordered lists (`<ul>` as the fallback when order is irrelevant). HN discussion focuses on flaky browser support for `datalist`, frustration with HTML/CSS quirks, and emerging semantic-aware tooling.

---

### Comment pulse
- `datalist` and `optgroup disabled` behave inconsistently on Safari and Firefox Android → many avoid it in production — counterpoint: simple autocomplete usage works fine for some.
- Native semantic HTML is powerful but cross-browser styling/behavior is brittle → devs retreat to React “div soup” they can control more predictably.
- Some seek linters that enforce semantic correctness → tools like the SuperHTML language server partially validate structure, nesting, and attribute values.

---

### LLM perspective
- View: Use the five-list taxonomy as a review checklist before inventing custom list-like UI.
- Impact: More semantic lists mean better accessibility, less ARIA boilerplate, and simpler markup around forms, metadata, and toolbars.
- Watch next: Browser convergence on `datalist` behavior and wider adoption of semantic HTML linters will determine how viable these patterns become.
