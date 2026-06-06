# The Website Specification

- Score: 428 | [HN](https://news.ycombinator.com/item?id=48343683) | Link: https://specification.website/

### TL;DR
A public “Website Specification” collects 128 concrete requirements for what a modern site should do: correct HTML structure, SEO metadata, accessibility, security headers, performance and caching, privacy, resilience, i18n, and standardized `/.well-known/` endpoints. Each rule cites underlying specs (WHATWG, W3C, IETF, WCAG, MDN), and the site doubles as a worked example. It also introduces “agent readiness” via llms.txt, per‑page Markdown, and an MCP server, which HN readers debate as either practical or hype-prone. Others want more UX‑level guidance and note implementation inconsistencies.

---

### Comment pulse
- Agent readiness is polarizing → critics expect abuse and divergence between human and agent views; supporters like markdown mirrors, crawl control, and AI-focused equivalents of robots.txt/SEO.  
- Practical UX gaps matter → commenters ask for form and login best practices (inputs, autofill, 2FA, focus) and lament today’s JS-heavy, non-native-feeling web.  
- Spec seen as curated index → some appreciate a single checklist sourced from standards; others call it derivative, AI-ish, and note the site itself misses its own “required” rules.

---

### LLM perspective
- View: Treat this as a living, opinionated checklist sitting atop standards, not as a replacement for the underlying specs.  
- Impact: Most useful for smaller teams, juniors, and auditors who need a shared baseline for “done” across HTML, SEO, a11y, and security.  
- Watch next: Adoption of llms.txt/MCP by major tools or browsers will decide whether “agent readiness” joins robots.txt and sitemaps as routine.
