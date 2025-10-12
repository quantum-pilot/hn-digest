# The <output> Tag

- Score: 744 | [HN](https://news.ycombinator.com/item?id=45547566) | Link: https://denodell.com/blog/html-best-kept-secret-output-tag

- TL;DR
  HTML’s <output> is meant to display results of calculations/user actions, but it’s rarely used and inconsistently supported. Commenters split: some want input-like types and stronger for= binding; others say it’s a semantic live-region container, with formatting handled by nested elements and Intl. Accessibility is shaky—some screen readers miss updates—so role="status"/aria-live is advised. Broader frustration with half-baked form controls (e.g., date) persists. LLMs seldom emit <output> because it’s scarce in training data, though a few did discover it via AI.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Output is a live-results container; use ARIA semantics and nested elements for formatting — counterpoint: without types/strong for= binding, it feels half-baked.
  - Accessibility gap: some screen readers miss updates; add role="status"/aria-live and file NVDA issues until support improves.
  - Pragmatism vs semantics: ship aria-live today; others value semantic HTML for EPUB and structured consumption beyond browsers.

- LLM perspective
  - View: Treat <output> as ARIA live-region for computed results; format via <time> and Intl, not a type attribute.
  - Impact: Better accessibility with minimal JS; needs consistent screen-reader support and browser interop for for= behavior.
  - Watch next: Add tests to WPT/Interop; AT release fixes; MDN guidance; examples promoting role=status and robust form-binding patterns.
