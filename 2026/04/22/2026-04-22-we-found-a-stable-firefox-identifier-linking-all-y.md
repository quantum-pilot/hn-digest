# We found a stable Firefox identifier linking all your private Tor identities

- Score: 346 | [HN](https://news.ycombinator.com/item?id=47866697) | Link: https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/

### TL;DR
FingerprintJS researchers found that Firefox-based browsers leaked a process-lifetime identifier through the ordering of `indexedDB.databases()` results. Because the order depended on global, deterministic internal data structures, unrelated sites could independently compute the same “permutation ID,” linking activity across domains, private windows, and even Tor Browser “New Identity” sessions until the browser process fully exited. With enough database names, the ID had high entropy. Mozilla fixed it in Firefox 150/ESR 140.10 by canonicalizing the ordering, illustrating how seemingly harmless APIs can become powerful tracking vectors.

---

### Comment pulse
- Fingerprinting company disclosed the bug → likely avoid using 0-days in products and prefer competitors and attackers losing this capability — counterpoint: secrecy could have given them an edge.  
- Tor/Firefox privacy users → must fully quit the browser to reset identity; Tor’s “New Identity” alone didn’t clear this process-global IndexedDB state.  
- Browser fingerprinting concern → many benign features (fonts, timezone, media support, window size) combine into unique IDs; overusing permissions would trash usability yet still miss subtle leaks.

---

### LLM perspective
- View: Treat every cross-origin or process-global implementation detail as potential identity state, not just explicit storage like cookies.  
- Impact: Tor, Firefox, and Gecko-derivative users should update; privacy tools can’t compensate for core browser-side leaks.  
- Watch next: Systematic audits of storage, caching, and isolation layers, plus standard patterns (sorting, privacy budgets) to neutralize similar side channels.
