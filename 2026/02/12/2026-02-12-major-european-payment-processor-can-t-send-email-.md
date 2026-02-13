# Major European payment processor can't send email to Google Workspace users

- Score: 432 | [HN](https://news.ycombinator.com/item?id=46989217) | Link: https://atha.io/blog/2026-02-12-viva

TL;DR  
- A signup to major European processor Viva.com failed because Google Workspace bounced its verification emails: they omit the Message-ID header.  
- Message-ID is only a “SHOULD” in RFC 5322, yet mail software and anti-spam tools treat it as effectively mandatory, especially for automated mail.  
- Commenters see this as emblematic of weak engineering and developer experience in parts of European fintech and note that Gmail/Workspace now function as de‑facto standards bodies for email behavior.

Comment pulse  
- Message-ID is formally SHOULD, not MUST → In practice, production and automated emails must include it; missing IDs strongly correlate with spam and broken software.  
- Vendors must adapt to Google’s de‑facto rules → If Workspace rejects missing IDs, you add them— counterpoint: others note Google isn’t dominant for European email.  
- Story deepens distrust in fintech stacks → Commenters recount sloppy financial IT and email bugs; others appreciate strict filters after experiencing weaker spam protection elsewhere.

LLM perspective  
- View: This illustrates protocol drift: large providers harden rules beyond RFCs, effectively redefining “valid” email for the ecosystem.  
- Impact: Fintechs and other B2B SaaS must treat deliverability like uptime: monitor bounces, test against Gmail/Workspace/Outlook, and fix misconfigurations proactively.  
- Watch next: Useful benchmark: a public, updated matrix of email provider requirements, plus tooling that lint-checks outbound mail against those de‑facto standards.
