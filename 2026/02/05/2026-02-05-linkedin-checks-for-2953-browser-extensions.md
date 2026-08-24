# LinkedIn checks for 2953 browser extensions

- Score: 519 | [HN](https://news.ycombinator.com/item?id=46904361) | Link: https://github.com/mdp/linkedin-extension-fingerprinting

### TL;DR

A public repository says LinkedIn’s page script probes for 2,953 Chrome extensions on every load by attempting to access extension-exposed resources. It publishes the extracted identifiers, a name-mapping script, and a CSV; roughly 78 percent matched the Chrome Web Store, while 22 percent required an archive fallback. Commenters inferred the list mainly targets LinkedIn scraping and automation tools but criticized undisclosed collection and broader browser fingerprinting. Firefox’s per-instance resource UUIDs appear to block this exact method, though not fingerprinting generally.

### Comment pulse

- Many listed extensions appear related to LinkedIn automation or scraping, suggesting abuse detection—counterpoint: commenters said protecting LinkedIn is not equivalent to protecting users.
- Chrome exposes predictable extension resource URLs; Firefox randomizes extension UUIDs, blocking this enumeration pattern while still permitting other fingerprinting signals.
- Developers reported rapidly accumulating console errors and high CPU in idle LinkedIn tabs, but the supplied discussion did not establish causation.

### LLM perspective

- View: Anti-abuse intent would not erase privacy risk; extension inventories can reveal tools, roles, interests, or uniquely identifying combinations.
- Impact: Chrome users may be silently classified; extension authors must treat web-accessible resources as fingerprint surfaces.
- Watch next: LinkedIn’s purpose, server-side reporting, retention, enforcement use, Chrome mitigations, Firefox bypasses, CPU cost, and regulatory scrutiny.
