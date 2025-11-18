# Google is killing the open web, part 2

- Score: 327 | [HN](https://news.ycombinator.com/item?id=45954560) | Link: https://wok.oblomov.eu/tecnologia/google-killing-open-web-2/

- TL;DR
  - The author argues Chrome removing in‑browser XSLT (and offering a JS polyfill they won’t ship) is a political move to sideline XML/RSS and centralize control; urges “do not comply,” keep using XSLT, and file browser bugs. They broaden this to captured governance (WHATWG), loss of plugins, DRM/EME, and propose modular, plugin‑like browsers; Gemini is noted but tech isn’t the core problem. HN splits between “obsolete/unsafe, use JS/server‑side” and “breaks important standards‑based sites, signals Google‑led de facto standards and lock‑in.”

- Comment pulse
  - Dropping XSLT cuts attack surface; replacing C libs with Rust XML is safer → xml‑rs subset risks non‑compliant XML and silent breakage.
  - Use JS/polyfills or server‑side transforms; XSLT is niche → critical gov/academic sites depend on it; one‑year window is short — counterpoint: built‑in RSS is better.
  - Not about openness; real harms are AMP, MV3, AI summaries → others see governance capture: deprecations define de facto standards without user‑centric alternatives.

- LLM perspective
  - View: Polyfill‑only deprecation shifts costs to publishers, signaling product control over standards stewardship.
  - Impact: RSS/Atom UX, XML‑driven sites, archives, and civic portals face regressions or rewrites; indie maintainers absorb security and compatibility burdens.
  - Watch next: Chromium’s XML parser completeness tests, Firefox/WebKit timelines, and whether forks ship XSLT via extensions or revive plugin‑like architectures.
