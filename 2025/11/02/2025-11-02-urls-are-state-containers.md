# URLs are state containers

- Score: 311 | [HN](https://news.ycombinator.com/item?id=45789474) | Link: https://alfy.blog/2025/10/31/your-url-is-your-state.html

### TL;DR

The essay argues that URLs should be first-class application state: paths represent hierarchy, query parameters encode filters and configuration, and fragments select client-side locations or views. This makes state shareable, bookmarkable, refresh-safe, deep-linkable, and compatible with browser history. The author recommends excluding secrets, unfinished input, transient UI, and oversized structures, while choosing pushState or replaceState according to navigation semantics. Commenters broadly agreed but stressed that exposed state becomes a public, versioned protocol with leakage, migration, autocomplete, authentication, and long-term compatibility costs.

### Comment pulse

- URL-centered design can improve UX by forcing teams to decide which application context deserves persistence and sharing.
- Critics warned that permanent strings constrain refactors and leak internals; supporters proposed explicit decoding, migration, and versioning.

### LLM perspective

- View: URL state is best treated as a deliberately small public interface, not a dump of internal state.
- Impact: Users regain reliable refresh, sharing, bookmarking, and Back behavior while teams inherit compatibility obligations.
- Watch next: Version migrations, privacy reviews, canonical defaults, history semantics, URL limits, and cross-browser behavior.
