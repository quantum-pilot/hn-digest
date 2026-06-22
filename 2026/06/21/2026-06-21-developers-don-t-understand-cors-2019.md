# Developers don't understand CORS (2019)

- Score: 355 | [HN](https://news.ycombinator.com/item?id=48614844) | Link: https://fosterelli.co/developers-dont-understand-cors

## TL;DR
- The post argues that many developers, including Zoom’s engineers, misunderstand CORS. Zoom ran a privileged localhost server and dodged CORS by encoding responses in image dimensions, exposing webcams to any website.  
- The author says they should instead have exposed a localhost REST API locked to `https://zoom.us` via `Access-Control-Allow-Origin` and used CSP to prevent iframed auto-joins.  
- The HN thread explodes into debate over what CORS actually guarantees, preflight rules, and how confusing the threat model and spec really are.

---

## Comment pulse
- CORS doesn’t block sending most cross-origin requests, only reading responses; true protection still requires backend checks and understanding “simple” vs preflighted requests.  
- Many devs lack a clear threat model; CORS is browser-only, optional for non-browser clients, and ends up feeling like a nuisance rather than security—counterpoint: it still meaningfully limits drive‑by abuse.  
- Spec and browser behavior feel complex and inconsistent, so people cargo‑cult headers until “it works”; MDN’s CORS guide is repeatedly cited as the rare clear resource.

---

## LLM perspective
- View: CORS looks like security but is really a controlled relaxation of same-origin; tools should surface this distinction explicitly.  
- Impact: Misconfigs in boilerplates, proxies, and localhost services become latent vulnerabilities, especially when paired with powerful native integrations.  
- Watch next: opinionated defaults in frameworks, CORS linters, better browser console messaging, and more threat-model–centric documentation and training.
