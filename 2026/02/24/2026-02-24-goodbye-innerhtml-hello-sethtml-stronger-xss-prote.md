# Goodbye InnerHTML, Hello SetHTML: Stronger XSS Protection in Firefox 148

- Score: 325 | [HN](https://news.ycombinator.com/item?id=47136611) | Link: https://hacks.mozilla.org/2026/02/goodbye-innerhtml-hello-sethtml-stronger-xss-protection-in-firefox-148/

### TL;DR

Firefox 148 is the first browser to ship the standardized Sanitizer API. Element.setHTML inserts HTML through a browser-native sanitizer, removing script-capable elements and attributes under safe defaults; developers can customize allowed markup and combine it with Trusted Types to block unsafe insertion paths. Mozilla presents it as a low-friction replacement for risky innerHTML assignments. HN welcomed defense in depth but warned that XSS-safe does not mean harmless: permitted markup or CSS can still alter interfaces, custom policies create footguns, older browsers lack support, and plain text should still use textContent.

### Comment pulse

- Browser-native DOM sanitization reduces parser differentials → it can reason about elements during insertion instead of transforming strings beforehand.
- Mixed APIs remain hazardous → counterpoint: Trusted Types enforcement can centrally block ordinary strings from reaching unsafe sinks.
- Use the narrowest output primitive → textContent fits usernames; setHTML fits intentionally rich, tightly allowlisted content.

### LLM perspective

- **View:** Safer defaults lower XSS risk but cannot infer an application’s intended presentation semantics.
- **Impact:** Web teams can simplify common sanitization while retaining server-side escaping and content validation.
- **Watch next:** Cross-browser adoption, sanitizer bypasses, unsafe custom configurations, CSS abuse, and Trusted Types deployment.
