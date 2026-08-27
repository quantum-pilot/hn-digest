# Checkout.com hacked, refuses ransom payment, donates to security labs

- Score: 525 | [HN](https://news.ycombinator.com/item?id=45912698) | Link: https://www.checkout.com/blog/protecting-our-merchants-standing-up-to-extortion

### TL;DR

Checkout.com says ShinyHunters accessed a legacy third-party cloud storage system that should have been decommissioned, exposing internal operational documents and merchant-onboarding material from 2020 or earlier. The company estimates fewer than 25% of current merchants were affected and says live payment processing, card numbers, and funds were untouched. It refused the ransom demand and promised an equivalent donation to cybersecurity research, without naming an amount. Commenters praised the disclosure’s directness but wanted a fuller root-cause analysis, remediation, and accountability.

### Comment pulse

- Some viewed the donation as a constructive refusal; others called it publicity without a disclosed ransom amount.
- Commenters questioned whether emphasizing a third party obscured Checkout.com’s responsibility for retaining the data.

### LLM perspective

- View: The clearest failure was lifecycle control: obsolete storage remained accessible after it should have disappeared.
- Impact: Even without payment data, onboarding and operational records can create meaningful merchant and organizational exposure.
- Watch next: Affected-data specifics, notification outcomes, remediation evidence, and whether Checkout.com publishes a substantive postmortem.
