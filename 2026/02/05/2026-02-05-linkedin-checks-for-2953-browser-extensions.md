# LinkedIn checks for 2953 browser extensions

- Score: 519 | [HN](https://news.ycombinator.com/item?id=46904361) | Link: https://github.com/mdp/linkedin-extension-fingerprinting

- TL;DR  
  LinkedIn injects a script on every page load that silently probes for 2,953 specific Chrome extensions by checking for web‑accessible resources, effectively building a detailed extension fingerprint for each visitor. The GitHub repo reverse‑engineers LinkedIn’s list and offers scripts to map IDs to store entries, revealing most are automation/scraping tools. HN discussion centers on privacy implications, LinkedIn’s anti‑scraping motives, Chrome’s fingerprint‑friendly design, and why Firefox’s randomized extension URLs block this particular tracking technique.

- Comment pulse  
  - Firefox resists this by assigning random moz-extension UUIDs, so sites can’t enumerate installed add-ons—counterpoint: overall browser fingerprinting still easily tracks most users.  
  - Many think LinkedIn targets scraping/automation extensions to protect its data; critics note the crude name-based list and possible Chrome Web Store scraping to compile it.  
  - Commenters blast Chrome as ad-driven spyware and new IE6; defenders cite sandboxing/site isolation, while others switch to Brave or Firefox to regain privacy.

- LLM perspective  
  - View: Extension enumeration via web-accessible resources is a general pattern; any browser exposing stable IDs invites similar fingerprinting.  
  - Impact: LinkedIn’s behavior normalizes invasive client-side recon; expect more enterprise sites to quietly profile toolchains, plugins, even devtools usage.  
  - Watch next: Browser vendors could restrict extension resource probing or add permissions; regulators may revisit consent rules around extension-based fingerprinting.
