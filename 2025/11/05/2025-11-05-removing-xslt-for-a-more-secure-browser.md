# Removing XSLT for a more secure browser

- Score: 160 | [HN](https://news.ycombinator.com/item?id=45823059) | Link: https://developer.chrome.com/docs/web-platform/deprecating-xslt

TL;DR
Browsers are dropping XSLT to reduce attack surface, citing libxml2 vulnerabilities and limited usage. HN splits: proponents highlight XSLT’s unique role in making RSS/Atom and government XML human-readable and easily discoverable; others say deprecation is overdue, favoring simpler stacks and XML+CSS or server-rendered HTML. Debate flares over whether the referenced libxml2 issue is real and Google’s motives. Some JS-blocking users want a non-JS templating replacement. Critics note XSLT has exploitable parsers and minimal stewardship compared with JavaScript.
- Content unavailable; summarizing from title/comments.

Comment pulse
- XSLT crucial for readable RSS/Atom and government XML → styles feeds/sitemaps; aids discovery — counterpoint: low adoption; XML+CSS or server HTML suffice.
- Cutting XSLT shrinks attack surface → libxml2 vulns, thin maintenance; deprecating legacy APIs helps security — counterpoint: cited bug disputed; Chrome’s C++ footprint is vast.
- Some want non-JS templating → XSLT feels cleaner to JS-blockers — counterpoint: XSLT exploits exist; JS has stronger security processes; JS-blocking users are rare.

LLM perspective
- View: Removing XSLT is pragmatic; browser vendors should ship a minimal XML viewer and encourage server-side rendering for feeds.
- Impact: Publishers using XSLT must migrate; expect breakage in feed discovery UX unless browsers improve RSS handling.
- Watch next: Deprecation timelines, fallback behavior, XML+CSS support parity, proposals for native feed rendering or sanitized client-side templates.
