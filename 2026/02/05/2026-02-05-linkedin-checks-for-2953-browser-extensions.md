# LinkedIn checks for 2953 browser extensions

- Score: 519 | [HN](https://news.ycombinator.com/item?id=46904361) | Link: https://github.com/mdp/linkedin-extension-fingerprinting

- TL;DR  
LinkedIn ships a script that, on every page view, quietly tests for 2,953 specific Chrome extensions by probing their web‑accessible resources, effectively building a fine-grained extension fingerprint. The GitHub repo reverse‑engineers LinkedIn’s list, resolves extension names, and shows many are removed or automation/scraping tools. HN discussion frames this as both anti‑scraping defense and invasive surveillance, notes Firefox’s architecture blocks this exact trick, and criticizes Chrome’s ad‑driven ecosystem for enabling such environmental fingerprinting.

- Comment pulse  
  - Firefox’s moz-extension random UUIDs stop sites from mapping specific extension IDs, so this particular scan fails—counterpoint: users remain fingerprintable through many other browser traits.  
  - List is dominated by LinkedIn scrapers and automation add-ons; some say it targets abuse, others note LinkedIn’s data brokerage and Chrome Web Store TOS violations.  
  - Many distrust Chrome as ad-company spyware and compare it to IE6; others concede it pioneered defenses like sandboxing; Brave is a popular alternative.

- LLM perspective  
  - View: Client-side extension scanning shows how anti-scraping tactics easily blur into cross-site tracking and unconsented behavioral profiling.  
  - Impact: Extension authors, growth hackers, recruiters, and ordinary jobseekers all inherit risk when their tool choices leak into platform risk models.  
  - Watch next: Expect browser vendors and regulators to scrutinize webAccessibleResources, mandate clearer consent, or treat extension enumeration as sensitive fingerprinting data.
