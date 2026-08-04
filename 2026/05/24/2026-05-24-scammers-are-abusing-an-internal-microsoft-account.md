# Scammers are abusing an internal Microsoft account to send spam links

- Score: 262 | [HN](https://news.ycombinator.com/item?id=48253186) | Link: https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/

### TL;DR

Scammers have spent months exploiting an unclear Microsoft workflow to send phishing messages from msonlineservicesteam@microsoftonline.com, the genuine address used for two-factor codes and account alerts. Attackers appear able to register as customers and insert scam subjects and links into automated notifications. Spamhaus notified Microsoft; Microsoft says it is investigating, strengthening detection and blocking, and removing abusive accounts. HN commenters argued the deeper trust failure is sprawling corporate domains and third-party link tracking, which make legitimate mail look suspicious and teach users that checking sender domains is unreliable.

### Comment pulse

- Use one rooted namespace → official mail from subdomains such as internal.microsoft.com would be easier to authenticate than scattered vanity domains.
- Sender authenticity cannot establish message intent → legitimate notification and marketplace endpoints can become phishing relays without any domain spoofing.
- Interface design creates extra ambiguity → Outlook’s font can make an attacker’s rn-prefixed domain resemble an employer’s m-prefixed domain.

### LLM perspective

- **View:** This is an abuse-control failure: a trusted delivery channel accepted attacker-controlled content without adequate constraints.
- **Impact:** Email-origin reputation loses value, increasing successful phishing and false positives against Microsoft’s legitimate alerts.
- **Watch next:** Microsoft should disclose the abused feature, remediation date, affected volume, and safeguards limiting notification customization.
