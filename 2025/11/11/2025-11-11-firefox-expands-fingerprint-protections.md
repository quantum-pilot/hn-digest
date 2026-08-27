# Firefox expands fingerprint protections

- Score: 256 | [HN](https://news.ycombinator.com/item?id=45888891) | Link: https://blog.mozilla.org/en/firefox/fingerprinting-protections/

### TL;DR

Firefox 145 expands defenses against browser fingerprinting in Private Browsing and Enhanced Tracking Protection Strict mode. Beyond blocking known trackers, Firefox now limits additional signals including fonts, graphics behavior, processor-core counts, touchscreen capacity, and window chrome dimensions. Mozilla says its measurements show these changes nearly halve the share of users appearing unique. The rollout deliberately avoids stronger masking that would break legitimate features such as timezone-aware scheduling. Commenters welcomed the effort but noted Firefox's smaller population, custom layouts, and evolving fingerprinting services complicate anonymity.

### Comment pulse

- Users valued automatic defenses but reported that unusual canvas dimensions can remain highly identifying.
- Stronger isolation or randomization may resist tracking better, yet often breaks logins and everyday site behavior.

### LLM perspective

- View: Anti-fingerprinting is population engineering: consistency matters more than hiding every individual signal.
- Impact: Default-compatible protections can help more users than extreme settings that require constant site exceptions.
- Watch next: Default-mode rollout, breakage reports, independent uniqueness tests, and adaptation by fingerprinting vendors.
