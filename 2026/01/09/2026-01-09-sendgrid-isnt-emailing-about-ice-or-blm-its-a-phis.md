# SendGrid isn’t emailing about ICE or BLM – it’s a phishing attack

- Score: 169 | [HN](https://news.ycombinator.com/item?id=46555615) | Link: https://fredbenenson.com/blog/2026/01/09/sendgrid-isnt-emailing-you-about-ice-or-blm-its-a-phishing-attack/

### TL;DR

Attackers are compromising SendGrid customer accounts, then using SendGrid’s authenticated infrastructure and those customers’ reputations to phish other users. Politically charged claims about ICE, Black Lives Matter, LGBTQ+ branding, or language changes create urgency; fake opt-out controls lead to credential-stealing pages that can capture passwords and 2FA codes. The author recommends unique passwords, 2FA, sender-domain checks, account audits, and filtering impersonation mail. Commenters emphasize that valid SPF and DKIM authenticate infrastructure, not a displayed brand or trustworthy intent.

### Comment pulse

- Operational criticism → former customers describe poor SendGrid support and billing problems, suggesting platform governance—not email-scale economics—may enable abuse.
- Filtering proposals → compare display names against known domains or quarantine mismatches — counterpoint: brand-specific rules do not scale.
- Authentication limits → SPF, DKIM, and DMARC cannot stop lookalike senders; commenters prefer visible domains and phishing-resistant WebAuthn.

### LLM perspective

- View: Authenticated delivery can amplify deception when account security and sender identity cues fail together.
- Impact: SendGrid customers face credential theft, reputation damage, blocked delivery, and cleanup costs from compromised accounts.
- Watch next: Twilio’s WebAuthn support, mandatory MFA rollout, abuse-response times, and detection of cross-customer phishing campaigns.
