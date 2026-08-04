# Removing React.js from the codebase and adapting Htmx for UI interactivity (2023)

- Score: 214 | [HN](https://news.ycombinator.com/item?id=49067301) | Link: https://misago-project.org/t/removing-reactjs-from-the-codebase-and-adapting-htmx-for-ui-interactivity/1267/

### TL;DR

Misago chose to unwind a hybrid architecture where Django rendered each forum page, embedded duplicate JSON, then React replaced the HTML and enabled interactions. That doubled templates, views, translations, APIs, customization work, and client cost. The plan moves incrementally to Django-rendered HTMX islands, tolerating full reloads where acceptable and retaining targeted JavaScript for richer controls. By July 2024, account settings and thread lists had migrated, shrinking `misago.js` from 615 KB to 530 KB. HN largely endorsed the forum fit while warning that response scope determines HTMX performance.

### Comment pulse

- Forums suit HTML-first design → their core is text, forms, filters, and pagination; WYSIWYG or highlighting can remain isolated client-side components.
- HTMX does not guarantee speed → returning oversized fragments made one filter page lag — counterpoint: precise targets and server-rendered partials avoid redundant markup.
- Client-heavy frameworks retain specific advantages → small JSON updates and offline-first behavior may outperform repeated server markup on highly interactive applications.

### LLM perspective

- **View:** The decisive architectural boundary is interaction locality: page-scale state favors clients, while isolated actions favor server-rendered fragments.
- **Impact:** Server work rises with interaction frequency, while clients shed state-management, hydration, and large bundle costs.
- **Watch next:** Compare interaction latency, transferred bytes, server load, accessibility, offline behavior, and maintenance effort after the migration completes.
