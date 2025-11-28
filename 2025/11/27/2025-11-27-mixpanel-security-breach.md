# Mixpanel Security Breach

- Score: 197 | [HN](https://news.ycombinator.com/item?id=46066522) | Link: https://mixpanel.com/blog/sms-security-incident/

## TL;DR
Mixpanel disclosed that on November 8, 2025 it detected a smishing campaign that led to unauthorized access to some customer accounts. They say they contained the incident by revoking user sessions, rotating credentials, resetting all employee passwords, engaging external forensics, and notifying affected customers, while asserting that others need not act. Hacker News commenters argue the statement omits crucial details (systems, data, scope, and timeline), compare it unfavorably to OpenAI’s more specific writeup of the same incident, and note OpenAI has now dropped Mixpanel.

## Comment pulse
- Disclosure lacks substance → No clarity on breached systems, data exposed, or scale; tone feels legalistic and defensive compared to OpenAI’s specific, candid incident report.  
- Timing and transparency questioned → Post came days after detection, on Thanksgiving eve, seen as minimizing attention—counterpoint: companies often wait for forensic confirmation before detailed disclosure.  
- User impact unclear → Closed-account holders still got notices, fueling doubts about data deletion, GDPR compliance, and whether “limited accounts” understates actual exposure.  

## LLM perspective
- View: Vendor breach communications should standardize around concrete fields: initial vector, affected data classes, time-to-detection, customer impact numbers.  
- Impact: Expect more large customers to scrutinize analytics vendors’ MFA, phishing training, and contractual breach-notification obligations, especially for employee-credential compromise.  
- Watch next: Whether regulators investigate timing, whether Mixpanel publishes follow-up specifics, and if competitors gain share on “security-first” positioning.
