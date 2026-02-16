# Oat – Ultra-lightweight, zero dependency, semantic HTML, CSS, JS UI library

- Score: 445 | [HN](https://news.ycombinator.com/item?id=47021980) | Link: https://oat.ink/

### TL;DR

Oat is a tiny (~8 KB gzipped) UI library built from plain semantic HTML, minimal CSS, and a bit of JavaScript, with zero dependencies and no build tooling. It styles native elements and ARIA roles directly, aims for accessibility-first, themeable design via CSS variables, and includes practical components like dialogs, tabs, and a layout sidebar. HN commenters like its speed, simplicity, and standards-based focus, while noting some inconsistency in its “classless” approach and being drawn to the author’s broader critique of JS framework bloat.

---

### Comment pulse

- Semantic-first, almost classless UI → encourages ARIA awareness and cleaner markup; sidebar/layout components are especially appreciated — counterpoint: semantics vs classes/attributes feel inconsistently applied.

- Performance and simplicity impress people → instant page loads remind users what non-SPA sites can feel like; some compare it favorably to heavyweight setups and even to DaisyUI.

- Seen as part of an anti-bloat trend → used in rclone’s new UI; pairs well with tools like Datastar; author’s blog post on JS ecosystem dysfunction resonates strongly.

---

### LLM perspective

- View: Oat fits teams wanting long-lived, low-maintenance UIs without React/Node lock-in, accepting a smaller component set and manual wiring.

- Impact: Most useful for dashboards, admin tools, and internal apps where semantic HTML and accessibility matter more than custom design systems.

- Watch next: Real-world adoption (like rclone), accessibility audits, and comparisons vs Tailwind/DaisyUI/HTMX+classless CSS in maintenance cost and performance.
