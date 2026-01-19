# Consent-O-Matic

- Score: 178 | [HN](https://news.ycombinator.com/item?id=46666283) | Link: https://github.com/cavi-au/Consent-O-Matic

- TL;DR  
Consent-O-Matic is an open-source browser extension that auto-recognizes cookie consent banners and executes your predefined choices, including allowing functional cookies while disabling tracking across hundreds of Consent Management Platforms. Instead of simply hiding banners (which can break sites), it scripts clicks and toggles through dark-pattern UIs on your behalf. Hacker News discussion centers on how these banners mask a vast tracking ecosystem, the legal meaning of “no consent,” and tradeoffs versus banner-blocking or alternative auto-decline add-ons.

- Comment pulse  
  - Cookie banners obscure tracking → consent popups grant hundreds of ad-tech firms profiling rights, often framed as ‘fraud prevention’ so users can’t realistically opt out.  
  - uBlock’s cookie-notices list hides banners → if you never click accept, there’s no consent; but this can silently break site features and workflows.  
  - Tools like Consent-O-Matic or Cookie Auto Decline → auto-apply choices, keeping logins/carts working while removing prompts — counterpoint: coverage and reliability vary significantly across sites.

- LLM perspective  
  - View: Treats consent UIs as hostile APIs, using adversarial interoperability so users regain control without manual clicking.  
  - Impact: Heavy CMP users, publishers, and regulators get de facto evidence that current consent flows are unusable and routinely bypassed.  
  - Watch next: Independent audits measuring tracking after “reject all,” standardized machine-readable consent APIs, and browser-level controls replacing site-specific dark patterns.
