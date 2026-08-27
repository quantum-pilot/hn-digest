# Why Nextcloud feels slow to use

- Score: 428 | [HN](https://news.ycombinator.com/item?id=45798681) | Link: https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/

### TL;DR

The author attributes Nextcloud’s sluggish feel partly to unusually large JavaScript payloads: roughly 15–20 MB uncompressed on a clean load, with individual Calendar, Files, Notes, notification, and shared bundles contributing heavily. Poor connections can turn common tasks into long waits, pushing the author toward focused alternatives such as Vikunja and Immich. Commenters argued that bundle size is only part of the diagnosis: Calendar can issue many serialized or uncached requests, while frontend update patterns, plugin boundaries, caching, and accumulated architecture may dominate latency.

### Comment pulse

- Users valued Nextcloud’s private, broad feature set but reported sync failures, upload problems, slow thumbnails, and recurring maintenance friction.
- Several favored multiple focused services with shared sign-on over one highly modular suite.

### LLM perspective

- View: The evidence supports frontend and request-path bloat, but not JavaScript size as the sole cause.
- Impact: Latency-sensitive and lower-powered clients bear the cost of architectural convenience most sharply.
- Watch next: Performance traces separating download, parse, execution, API waterfalls, rendering, and server time.
