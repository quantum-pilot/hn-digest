# Consent-O-Matic

- Score: 178 | [HN](https://news.ycombinator.com/item?id=46666283) | Link: https://github.com/cavi-au/Consent-O-Matic

### TL;DR

Consent-O-Matic is an open-source browser extension from Aarhus University that detects more than 200 consent-management platforms and answers their banners using preferences chosen once. Its rules locate banner elements, open settings, toggle consent categories, save choices, and can be extended as sites change. The extension reads pages and tab URLs, stores settings locally, and contacts the network only for rule updates or user reports. HN favored its granular automation over simply hiding banners, which can break logins, carts, and other functional cookies.

### Comment pulse

- Consent banners mask extensive profiling → commenters stressed that withholding consent matters more than removing visual annoyance.
- Blanket blocking can break sites → granular rules preserve functional cookies while rejecting analytics, advertising, and other purposes.
- Automation remains brittle → alternatives may cover more sites, but hidden banners can leave users diagnosing mysterious failures.

### LLM perspective

- View: Automating the actual consent workflow preserves intent better than cosmetic banner removal.
- Impact: Users regain time and consistency; maintainers inherit a continuous compatibility race against changing CMP markup.
- Watch next: Track rule coverage, failure reports, browser-permission changes, and audits confirming rejected processing actually stops.
