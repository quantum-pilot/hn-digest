# Just use a button

- Score: 232 | [HN](https://news.ycombinator.com/item?id=45774182) | Link: https://gomakethings.com/just-use-a-button/

- TL;DR
    - The piece argues against using divs as interactive controls. A button provides built‑in semantics, focusability, and keyboard activation; bolting on role, tabindex, and keydown handlers recreates fragile versions of what buttons already do. HN extends this to “use the right HTML element” generally: links for navigation, imgs for images. Nuance: in forms, buttons default to submit, so specify type="button" when appropriate. Many blame SPA habits and past styling inconsistencies for today’s div‑heavy, JavaScript‑first patterns.

- Comment pulse
    - Use anchors for navigation → preserves middle‑click, context menu, and a11y; onclick links break expectations — counterpoint: SPA routers sometimes complicate plain links.
    - In forms, set type="button" → avoids unintended submits; many devs misremember defaults for button versus input.
    - Prefer native elements broadly → past styling inconsistencies fueled custom UI, but semantics still deliver better UX with less code.

- LLM perspective
    - View: Favor semantic HTML; stop reimplementing control behavior with ARIA/tabindex/keydown.
    - Impact: Design systems and SPAs should default to button/a/img, document type="button", and ban faux controls.
    - Watch next: Add jsx‑a11y lint rules, axe tests; audit components; track native control styling improvements.
