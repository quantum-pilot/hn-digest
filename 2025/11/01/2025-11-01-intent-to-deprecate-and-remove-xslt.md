# Intent to Deprecate and Remove XSLT

- Score: 83 | [HN](https://news.ycombinator.com/item?id=45779261) | Link: https://groups.google.com/a/chromium.org/g/blink-dev/c/CxL4gYZeSJA/m/yNs4EsD5AQAJ

- TL;DR
  - Chrome plans to deprecate and remove in‑browser XSLT v1.0, citing libxslt maintenance gaps and memory‑safety risk versus ~0.05% usage. WHATWG advanced deprecation; Firefox/WebKit signaled support. Plan: warnings in M143, early pre‑stable disabling, removal in M155, with Origin Trial and Enterprise Policy until M164. A drop‑in polyfill/extension restores most breakages; XPath (document.evaluate) remains. HN debates precedent and Google’s influence versus security pragmatism; some note XSLT’s niche value for static sites without JS, others point to modern JS/CSS alternatives.

- Comment pulse
  - Baseline-feature removal sets a precedent → fear of Google steering the web and removing long-available capabilities — counterpoint: cross-engine consensus; security risks outweigh tiny usage.
  - XSLT enables static sites to compose HTML without JS or servers → simple menus/includes via XML transforms; few people actually build sites this way today.
  - Public sector should fund libxslt or a Rust rewrite → maintain safety without breakage; skeptics note complexity, ongoing cost, and better-supported JS alternatives.

- LLM perspective
  - View: Security-first deprecation of a niche, risky parser makes sense if mitigations (polyfill, trials, long runway) preserve real-world functionality.
  - Impact: Legacy XML-driven sites, gov portals, intranets, and WebView apps must migrate to JS libraries or server-side transforms.
  - Watch next: Canary breakage telemetry, OT/enterprise uptake, a maintained WASM/Rust XSLT engine, and formal deprecation policy for baseline features.
