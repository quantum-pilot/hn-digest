# Framework discloses data breach via Metabase 0-day

- Score: 141 | [HN](https://news.ycombinator.com/item?id=49206130) | Link: https://community.frame.work/t/framework-data-breach-discussion/83939

### TL;DR

Framework notified affected customers within hours after Metabase reported that attackers exploited an unknown vulnerability in Metabase Cloud 1.58 and later. The attacker reached Framework’s analytics instance, ran dozens of queries, briefly created an API key, and accessed customer records including names, email addresses, and billing addresses; Framework said payment data was not involved. Metabase blocked and patched the vulnerable endpoints, engaged forensics and law enforcement, and advised credential rotation. Framework is reviewing which columns its business-intelligence tools receive and says it will narrow access.

### Comment pulse

- Customers praised the unusually fast disclosure but disputed calling exposure of most available identifiers “limited.”
- Abandoned carts and old accounts were affected, intensifying criticism of retention and unnecessary third-party sharing.
- Some accepted analytics vendors as operationally normal — counterpoint: immutable metadata creates lasting phishing, scam, and physical-security risks.

### LLM perspective

- View: Rapid response mitigates trust damage but cannot compensate for excessive data propagation.
- Impact: Customers now face targeted phishing using accurate order, identity, and address context.
- Watch next: Forensic scope, credential rotation, retention changes, vendor audit results, and formal customer remediation.
