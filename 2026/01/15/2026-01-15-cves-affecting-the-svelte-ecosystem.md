# CVEs affecting the Svelte ecosystem

- Score: 131 | [HN](https://news.ycombinator.com/item?id=46636387) | Link: https://svelte.dev/blog/cves-affecting-the-svelte-ecosystem

### TL;DR

Svelte published fixes for five vulnerabilities across devalue, Svelte, SvelteKit, and adapter-node, urging upgrades to devalue 5.6.2, Svelte 5.46.4, SvelteKit 2.49.5, and adapter-node 5.5.1. Three issues involve memory or CPU exhaustion around parsing and experimental remote functions; another combines prerendering DoS with conditional SSRF, and one enables XSS through hydratable with unsanitized keys. HN readers stressed that static builds are unaffected and most exposure requires experimental features, while warning that SSRF exceeds ordinary availability risk.

### Comment pulse

- Devalue attracted scrutiny because it parses user-controlled structures → form parsing is broadly difficult even in mature standard libraries.
- Most affected paths require remote functions or async mode → counterpoint: the prerendering issue can expose internal resources through SSRF.
- Static-only deployments avoid these server-side paths → commenters still recommended upgrading and wanted fixes linked directly to advisories.

### LLM perspective

- View: Exposure is configuration-dependent, but dependency chains make prompt patching safer than selective risk assessment.
- Impact: Teams using experimental SvelteKit features face the highest urgency; static sites have substantially lower blast radius.
- Watch next: Fix commits, regression tests, safer parser limits, and security review before experimental features graduate.
