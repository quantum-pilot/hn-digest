# Scammers are abusing an internal Microsoft account to send spam links

- Score: 262 | [HN](https://news.ycombinator.com/item?id=48253186) | Link: https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/

- TL;DR
    - Scammers have found a way to send phishing emails from Microsoft’s trusted notification address msonlineservicesteam@microsoftonline.com, which normally delivers 2FA codes and account alerts. Spamhaus reports months of abuse, indicating Microsoft’s alert system lets customer-created accounts overly customize content. Microsoft says it’s now investigating and tightening filters and account removals. HN discussion broadens this to systemic issues: sprawling, confusing corporate email domains, shaky Microsoft security UX, and reluctance to adopt clear, centralized subdomain schemes for official communication.

- Comment pulse
    - Domain sprawl erodes trust → unclear which sender domains are legit; examples include Bluesky addresses, third-party tracking links, and banks before standardized caller ID rules.
    - Microsoft account security feels brittle → authenticator prompts appear without logs, passwordless flows can’t be disabled, and repeated failures can lock accounts and trigger resets.
    - Ambiguous domains aid phishers → 'm' vs 'rn' fonts and government/Booking domains confuse users — counterpoint: Booking scams often involve compromised hotels, not messaging abuse.

- LLM perspective
    - View: This illustrates that "trusted sender" models fail once internal notification channels become semi-self-service and lightly audited.
    - Impact: Enterprises should inventory and publish official email domains, consolidate onto subdomains, and enforce strict templates for automated notifications.
    - Watch next: Track whether Microsoft adds domain-level safeguards: DMARC/BIMI consistency, tighter API permissioning, and customer-visible lists of legitimate notification addresses.
