# Oat – Ultra-lightweight, zero dependency, semantic HTML, CSS, JS UI library

- Score: 445 | [HN](https://news.ycombinator.com/item?id=47021980) | Link: https://oat.ink/

### TL;DR

Oat provides a class-light, zero-dependency UI kit using roughly 6 KB of compressed CSS and 2.2 KB of JavaScript. It styles native elements and ARIA attributes contextually, uses Web Components only for a few dynamic pieces, includes common controls plus grid and sidebar layouts, and supports keyboard navigation, CSS-variable theming, and dark mode without a build system. HN praised its instant pages and standards-first ergonomics, while noting that the catalog inconsistently mixes semantic tags, data attributes, ARIA, and occasional classes.

### Comment pulse

- ARIA-responsive styling encourages accessibility-first markup → developers must think about states instead of outsourcing them to a React component.
- Including a complete sidebar layout adds practical value → many small libraries demonstrate controls but omit application structure.
- Real adoption has begun → one project is replacing an unmaintained React interface with Oat.

### LLM perspective

- **View:** The library succeeds by constraining choices, but semantic consistency matters more than the absence of classes.
- **Impact:** Small apps gain fast defaults without Node tooling; complex teams retain responsibility for behavior, testing, and governance.
- **Watch next:** Accessibility audits, component consistency, extension growth, production migrations, and maintenance stability.
