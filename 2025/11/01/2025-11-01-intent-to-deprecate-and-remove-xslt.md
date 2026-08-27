# Intent to Deprecate and Remove XSLT

- Score: 83 | [HN](https://news.ycombinator.com/item?id=45779261) | Link: https://groups.google.com/a/chromium.org/g/blink-dev/c/CxL4gYZeSJA/m/yNs4EsD5AQAJ

### TL;DR

Chromium proposes deprecating browser XSLT because its aging libxslt implementation creates a security burden while client-side usage is low. The tentative schedule starts warnings in late 2025, disables XSLT for most stable users in November 2026, and ends origin-trial and enterprise-policy exceptions in August 2027. Chromium acknowledges above-threshold `XSLTProcessor` usage and developer opposition, offering a polyfill, extension, outreach, and early pre-stable experiments. XPath and `document.evaluate()` are explicitly outside the removal. The plan is approved for experimentation, not yet completed.

### Comment pulse

- Critics called removal of a standardized, broadly available feature a troubling compatibility precedent.
- Others accepted the maintenance and security rationale; users also described static-site composition uses that JavaScript-free alternatives may not match.

### LLM perspective

- View: Security can justify removal, but baseline web features require unusually strong compatibility evidence and migration support.
- Impact: Even rare usage can represent durable documents and workflows whose owners no longer actively maintain them.
- Watch next: Scrutinize pre-stable breakage data, polyfill limitations, outreach coverage, and whether the proposed dates change.
