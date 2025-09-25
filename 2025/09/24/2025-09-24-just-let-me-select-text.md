# Just let me select text

- Score: 701 | [HN](https://news.ycombinator.com/item?id=45360475) | Link: https://aartaka.me/select-text.html

- TL;DR
    - The essay argues that disabling text selection turns interfaces into opaque media: users can’t translate, cite, or reference UI text—hurting comprehension and accessibility. Claimed justifications (anti-scraping, draggable UIs, “professional” look) don’t hold; bots ignore selection locks and it blocks bug reporting and international use. HN largely agrees: people rely on selecting to read, copy, and translate; OS-level OCR is a workaround but absurd when the text is already there. The ask: stop disabling selection; design around accidental highlights instead.

- Comment pulse
    - Selecting while reading aids focus and referencing → blocking selection and share popups degrade UX and accessibility.
    - OS OCR makes any app’s text selectable (Android app switcher, iOS Live Text) → ironic ML fix for data apps already have.
    - Disable selection on buttons/tabs to avoid accidental highlights → users need to translate/copy labels and IDs; design better targets — counterpoint: accidental highlights distract.

- LLM perspective
    - View: Selection is a baseline affordance; solve conflicts with CSS and event handling rather than disabling.
    - Impact: Restores translation, quoting, and bug reporting; reduces reliance on screenshots/OCR; improves a11y compliance.
    - Watch next: Platform overrides for selection locks; product policies enabling live caption copy; UX guidelines for clickable text without blocking selection.
