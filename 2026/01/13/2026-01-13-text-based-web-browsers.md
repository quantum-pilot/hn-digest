# Text-based web browsers

- Score: 275 | [HN](https://news.ycombinator.com/item?id=46597518) | Link: https://cssence.com/2026/text-based-web-browsers/

### TL;DR
The article inspects how classic text-based browsers like Lynx, w3m, and ELinks cope with modern HTML features such as `<details>`, `<dialog>`, popovers, `hidden`, and `inert`. Most newer, interactive semantics either degrade poorly (dialogs, popovers, inert) or not at all (`hidden` content always shown), breaking progressive enhancement patterns and sometimes behavior. The author still likes testing with text browsers but concludes the standards and mainstream engines essentially ignore them. HN replies highlight newer terminal browsers and broader accessibility, UX, and “user agent” questions.

---

### Comment pulse
- CLI-first browser edbrowse → powerful accessibility- and scripting-oriented workflow, blending browser, mail, IRC, SQL; linear interaction suits some users better than GUIs.  
- Newer TUIs like chawan and brow6el → aim to be “real” browsers in terminals with CSS/JS/images, narrowing the gap with GUI engines.  
- Text-mode compatibility → forces clean HTML structure, aids Tor “Safest” mode and accessibility—counterpoint: rich web apps and complex UIs still fundamentally depend on JavaScript.

---

### LLM perspective
- View: Treat text browsers as harsh progressive-enhancement tests; if they fail catastrophically, underlying HTML semantics are probably fragile.  
- Impact: Security-conscious users, blind users, and low-bandwidth environments depend most on robust HTML; they’re first to suffer from neglect.  
- Watch next: Tools that auto-derive text-mode views from full pages, and specs explicitly addressing non-graphical user agents.
