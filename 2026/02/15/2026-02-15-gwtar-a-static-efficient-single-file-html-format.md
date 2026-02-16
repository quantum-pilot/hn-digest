# Gwtar: A static efficient single-file HTML format

- Score: 159 | [HN](https://news.ycombinator.com/item?id=47024506) | Link: https://gwern.net/gwtar

### TL;DR

Gwtar is a new archival format that packs a full web snapshot (HTML + all assets) into one `.html` file while still loading only what’s needed. It prefixes a small HTML/JS header, then appends a tarball of the original page and resources. The header calls `window.stop()` so the browser stops downloading after the header, then uses HTTP Range requests to pull individual assets from the tail tarball on demand. This solves the long‑standing “HTML trilemma” of being static, single‑file, and efficient, at the cost of weaker local-file support and dependence on JS and Range.

---

### Comment pulse

- Key trick is `window.stop()` → lets header halt further download and then Range‑fetch slices of the same file—counterpoint: brittle if browser behavior changes or JS is blocked.  
- Critics: lack of smooth local-file viewing undermines archival use → security restrictions block self-requests for local pages, forcing conversion back to multi-file form.  
- Alternatives debated → service-worker polyglots or SingleFileZ; but SingleFileZ still downloads the whole ZIP before rendering, so it’s “single” but not bandwidth-efficient.

---

### LLM perspective

- View: Gwtar is a clever, standards-compliant hack that makes browser + HTTP behave like a random-access archive reader.  
- Impact: Most useful for serious self-hosted archiving, large interactive articles, and reproducible-research bundles with embedded datasets.  
- Watch next: Real-world benchmarks on huge pages, more robust tooling (validators, hash checks), and whether archiving tools adopt Gwtar as an export target.
