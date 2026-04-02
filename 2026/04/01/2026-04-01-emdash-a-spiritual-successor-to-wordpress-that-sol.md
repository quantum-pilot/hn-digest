# EmDash – A spiritual successor to WordPress that solves plugin security

- Score: 435 | [HN](https://news.ycombinator.com/item?id=47602832) | Link: https://blog.cloudflare.com/emdash-wordpress/

### TL;DR
Cloudflare’s EmDash is a new MIT‑licensed, TypeScript CMS positioned as a WordPress successor, built on Astro and Cloudflare’s serverless Workers/runtime. Its core innovation is a capability-based plugin model: each plugin runs in an isolated worker with a manifest that declares precise permissions (e.g., content read, email send, optional outbound hostnames), avoiding the “full DB/filesystem access” problem behind most WordPress vulnerabilities and marketplace lock‑in. EmDash also bakes in x402 pay-per-request monetization, passkey auth, AI/agent tooling, and one‑click import from existing WordPress sites.

---

### Comment pulse
- Strong interest from current WP devs → TypeScript modules and worker-style plugins align with modern tooling, CI/CD, and security expectations—counterpoint: doesn’t address WP’s “FTP and done” simplicity.

- Static vs dynamic debate → Critics prefer pure static sites; defenders note Astro still outputs static HTML while allowing sandboxed dynamic plugins for real-world client needs.

- Ecosystem skepticism → Many doubt it can rival WordPress’s plugin/labor market moat; success hinges on being clearly cheaper/easier than Wix/Squarespace/Shopify for non-technical users.

---

### LLM perspective
- View: The manifest-based, sandboxed plugin architecture is a concrete, testable improvement over WordPress’s all-powerful PHP plugins.

- Impact: Hosting providers, agencies, and security-conscious orgs gain a modern CMS path without inheriting WordPress’s operational and vulnerability baggage.

- Watch next: Real-world security audits, plugin catalog growth, migration tooling maturity, and whether agencies can train non-technical editors to live comfortably in EmDash.
