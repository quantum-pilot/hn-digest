# Show HN: Minimalist editor that lives in browser, stores everything in the URL

- Score: 206 | [HN](https://news.ycombinator.com/item?id=46378554) | Link: https://github.com/antonmedv/textarea

### TL;DR

Textarea.my is a backend-free browser editor that deflate-compresses its document into the URL fragment, making notes shareable by copying one link. A Markdown heading can set the page title, and DevTools-injected article styles persist too. HN liked the pattern for quick, single-purpose tools and noted browser URL limits can accommodate surprisingly large documents. Discussion also exposed tradeoffs: URL bytes are not characters, shared links reveal their contents to recipients, Cloudflare analytics weakens the privacy pitch, and a native editor remains simpler for purely local notes.

### Comment pulse

- Disposable apps → fragment storage enables free, backendless tools tailored to one sharing workflow.
- Capacity → compression and generous browser limits support substantial text, but interoperability depends on octets and URI-safe encoding.
- Privacy → avoiding server-side document storage is attractive — counterpoint: embedded analytics and link sharing still expose metadata or content.

### LLM perspective

- View: The URL becomes both database and transport, trading durable storage for transparent portability and near-zero infrastructure.
- Impact: Users can share editable snapshots without accounts, while losing access control, collaboration, and conventional recovery.
- Watch next: Test cross-browser size limits, malformed fragments, Unicode handling, analytics removal, versioning, and accidental link leakage.
