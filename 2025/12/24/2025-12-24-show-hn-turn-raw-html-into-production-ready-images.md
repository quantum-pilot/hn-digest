# Show HN: Turn raw HTML into production-ready images for free

- Score: 132 | [HN](https://news.ycombinator.com/item?id=46371743) | Link: https://html2png.dev

### TL;DR
WebFetch / html2png is a free HTML-to-image/PDF API built on Cloudflare Workers. You POST raw HTML plus options (size, format, DPI, zoom, transparency) and get back a public, cached URL to the rendered asset. It’s pitched as “agent-native” so LLMs can generate visuals, OG images, PDFs, and UI mockups without MCP plugins or extra infra. HN commenters note you can already do this with headless Chrome/Playwright, debate the “production-ready” marketing, and discuss image optimization and waiting strategies.

---

### Comment pulse
- This overlaps with headless Chrome/Playwright CLI screenshotting → skeptics see it as a hosted wrapper. — counterpoint: managed edge + CDN is valuable operationally.
- “Production-ready” is seen as AI-era marketing jargon → some want concrete claims (scaling, CDN, reliability, compression), others just joke about “cloud-native, web-scale images.”
- PNGs aren’t optimized and delay is fixed → suggestions: optipng/webp/avif support and proper Playwright wait conditions like `networkidle` instead of static timeouts.

---

### LLM perspective
- View: Nice glue for text-only agents to emit visual artifacts without developers standing up headless-browser infrastructure.
- Impact: Most useful to SaaS dashboards, reporting tools, and code/diagram assistants needing one-off images or PDFs on demand.
- Watch next: Add smarter load-wait options, optional compression, and auth/privacy controls for non-public or higher-volume production workloads.
