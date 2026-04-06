# Someone at BrowserStack is leaking users' email addresses

- Score: 360 | [HN](https://news.ycombinator.com/item?id=47649117) | Link: https://shkspr.mobi/blog/2026/04/someone-at-browserstack-is-leaking-users-email-address/

- TL;DR  
  Terence Eden uses unique email aliases per service and caught BrowserStack leaking his address: a third‑party contacted that alias, citing Apollo.io. Apollo first claimed it had “derived” the email, then admitted BrowserStack contributed it to Apollo’s data‑sharing network. Eden infers BrowserStack (or a vendor/employee) is funneling user data into a sales database and then ignoring complaints. HN discussion notes this is standard practice in B2B CRMs, deeply at odds with users’ privacy expectations and likely regulatory intent.

- Comment pulse  
  - Widespread B2B data‑sharing → Tools like Apollo ingest customer lists, enrich them, and resell profiles to all clients; sharing is opt‑out, hidden—counterpoint: legality/consent is dubious.  
  - Why Eden’s address escaped → Most likely a BrowserStack sales upload to Apollo or CRM integration, not a hack; some argue it’s deliberate data selling.  
  - Unique emails as canaries → Commenters endorse per‑site aliases via custom domains/Fastmail/iCloud, while noting services de‑alias “+tags” and other vendors (e.g., BrightData) also mishandle data.

- LLM perspective  
  - View: This isn’t an isolated “leak” but structural: growth tooling turns every signup into a tradable lead without meaningful consent.  
  - Impact: Developers, admins, and decision‑makers using SaaS end up in shared prospect databases; privacy promises and DPA contracts become meaningless.  
  - Watch next: Regulators testing CRMs’ contributor networks against GDPR/CCPA, plus user‑friendly tools for aliasing, opt‑outs, and automated deletion/subject‑access requests.
