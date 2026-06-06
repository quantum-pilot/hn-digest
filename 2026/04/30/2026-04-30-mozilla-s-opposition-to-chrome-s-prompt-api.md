# Mozilla's opposition to Chrome's Prompt API

- Score: 575 | [HN](https://news.ycombinator.com/item?id=47959463) | Link: https://github.com/mozilla/standards-positions/issues/1213#issuecomment-4347988313

### TL;DR

Chrome’s Prompt API exposes a built‑in LLM through a generic browser API so sites can do things like summarization or text generation without calling external services. Mozilla has issued a negative standards position, arguing it will “calcify” the web around the quirks and terms of Google’s model, forcing other browsers to copy it or lose compatibility, and encouraging model-specific code paths. They instead want experimentation via extensions and locally chosen models. Chrome-side advocates accept many risks but favor shipping, measuring compat/legal harms, and iterating rather than delaying AI integration into the web.

---

### LLM perspective

- View: This is a clash between web‑as-neutral-runtime and web‑as-opinionated-AI-host; Prompt API pushes the latter hard and early.
- Impact: If Prompt-like APIs become common, prompt engineering becomes a cross‑browser compat problem, advantaging platforms with dominant distribution and marketing.
- Watch next: Evidence of sites breaking on non-Chromium models, browser vendors’ ToS changes, and how widely Edge/others adopt or diverge from Chrome’s design.
