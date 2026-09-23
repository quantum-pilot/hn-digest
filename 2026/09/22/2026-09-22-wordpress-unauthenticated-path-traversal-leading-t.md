# WordPress: Unauthenticated path traversal leading to conditional RCE

- Score: 229 | [HN](https://news.ycombinator.com/item?id=49803959) | Link: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp

### TL;DR

WordPress disclosed CVE-2026-87902, a critical unauthenticated path-traversal flaw in page-template resolution affecting releases from 4.7 through 7.1.1. An attacker can include a readable local PHP file outside theme directories; remote code execution additionally requires a theme with a top-level `page-` directory and a usable server-side PHP target under specific configuration. Fixes were released as 7.1.2 and backported across maintained historical branches. HN discussion stresses rapid patching, safer path abstractions, and the operational appeal of static-site migrations.

### Comment pulse

- Popularity amplifies WordPress exposure → automated scanners continuously probe common PHP paths across its enormous installed base.
- Conditional exploitation still demands urgent patching → theme structure and server configuration gate RCE, but no authentication or interaction is required.
- Static sites reduce attack surface → migrations remove dynamic plugins and database complexity — counterpoint: comments and editorial workflows still need replacements.

### LLM perspective

- View: The root lesson is capability-safe file access; string-based global paths make traversal mistakes easy to repeat.
- Impact: Administrators across many legacy branches must patch promptly and audit themes plus PHP runtime settings.
- Watch next: Monitor exploitation evidence, automatic-update coverage, plugin interactions, regression tests, and unsupported installations.
