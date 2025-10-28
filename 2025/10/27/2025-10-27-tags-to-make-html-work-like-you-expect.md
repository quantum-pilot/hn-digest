# Tags to make HTML work like you expect

- Score: 388 | [HN](https://news.ycombinator.com/item?id=45719140) | Link: https://blog.jim-nielsen.com/2025/dont-forget-these-html-tags/

- TL;DR
  - Blog lists four “incantations” for reliable HTML: <!doctype html> to avoid quirks-mode; <html lang> for accessibility/SEO; <meta charset="utf-8"> for correct text; <meta name="viewport"> for sane mobile scaling. A tongue‑in‑cheek nod to root+bundle.js aside, comments focus on real-world pitfalls: HN itself ships no DOCTYPE, prompting hacks to force standards mode; calls to add semantic landmarks (<main>/<nav>) for screen readers; debates over narrow content widths and tiny default fonts; and minifiers producing parser‑tolerated but authoring‑invalid HTML.

- Comment pulse
  - Quirks-mode hurts scripts; fix by injecting DOCTYPE (uBlock) or rewrite with document.write + reattach nodes — counterpoint: forcing standards may break legacy layouts.
  - Use <main>/<nav> semantics → screen readers skip chrome; some place nav last and visually reorder via CSS for better SR flow.
  - Narrow content columns aid readability; HN’s tiny default font frustrates users — counterpoint: fixed widths reflect old design, zoom is a user workaround.

- LLM perspective
  - View: Simple defaults still matter; shipping correct doctype, lang, charset, viewport prevents 80% of “mystery” bugs.
  - Impact: Accessibility, SEO, and mobile render quality improve without frameworks; fewer user scripts/hacks needed on hostile pages.
  - Watch next: Browser option for standards-only mode; better minifiers preserving authoring conformance; adoption of semantic landmarks like main/nav.
