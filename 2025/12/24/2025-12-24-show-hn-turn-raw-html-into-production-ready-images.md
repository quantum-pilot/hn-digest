# Show HN: Turn raw HTML into production-ready images for free

- Score: 132 | [HN](https://news.ycombinator.com/item?id=46371743) | Link: https://html2png.dev

### TL;DR

Html2png.dev offers a no-signup HTTP endpoint and editor for rendering raw HTML into PNG, JPEG, WebP, or PDF with configurable dimensions, scale, delay, zoom, and transparency. Generated assets are public and ephemeral; free use is capped at 50 requests per IP each hour. The site targets automated pipelines and LLM agents without MCP setup. HN questioned the “production-ready” claim because headless Chrome already screenshots pages, the demo PNG compressed substantially further, and robust rendering needs explicit readiness conditions rather than vague or fixed waiting.

### Comment pulse

- Convenience → hosted format, sizing, transparency, and CDN delivery bundle work beyond Chrome’s basic screenshot command.
- Production skepticism → unoptimized output and marketing language undermine reliability claims without measurable service guarantees.
- Rendering correctness → event- or condition-based waits handle dynamic pages better than arbitrary delays — counterpoint: observed requests appeared to delay timeout.

### LLM perspective

- View: The product’s value is managed rendering infrastructure, not the browser capability itself.
- Impact: Small teams and agents gain a simple endpoint but inherit public-output, rate-limit, privacy, and availability risks.
- Watch next: Publish retention rules, concurrency limits, readiness controls, output optimization, failure semantics, and service-level commitments.
