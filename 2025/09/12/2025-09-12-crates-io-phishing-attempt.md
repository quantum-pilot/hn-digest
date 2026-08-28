# Crates.io phishing attempt

- Score: 147 | [HN](https://news.ycombinator.com/item?id=45222772) | Link: https://fasterthanli.me/articles/crates-io-phishing-attempt

### TL;DR

Rust crate maintainers received phishing emails falsely claiming crates.io had been breached and directing them to rotate credentials through a counterfeit GitHub login page. The crates.io team acknowledged the campaign, and the report said no compromised packages had been identified as of its September 12 update. Commenters emphasized navigating independently to official sites, using domain-aware password managers, and treating urgent inbound requests skeptically. They also noted that legitimate organizations weaken these defenses when official messages use unfamiliar domains or embed unmarked user-controlled text.

### Comment pulse

- Readers disagreed over how convincing the message was, but stressed that fatigue can defeat even knowledgeable maintainers.
- A PayPal anecdote showed how attackers can place scam instructions inside genuinely signed platform email.

### LLM perspective

- View: The campaign targets repository trust through maintainers, making authentication design more important than individual vigilance.
- Impact: One successful credential theft could convert a narrow phish into a broad software-supply-chain incident.
- Watch next: Confirmed account compromise, mandatory phishing-resistant authentication, domain takedowns, and clearer official incident channels.
