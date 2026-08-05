# Thanks FedEx, This Is Why We Keep Getting Phished (2024)

- Score: 294 | [HN](https://news.ycombinator.com/item?id=49175192) | Link: https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/

### TL;DR

Troy Hunt received FedEx duty-payment texts containing nearly every classic phishing signal: odd capitalization, urgency, unexplained amounts, unfamiliar BPOINT URLs, inconsistent tracking details, and broken links. Direct verification through FedEx’s site, chatbot, and phone tree failed; only a later email containing his Prusa invoice proved the request genuine. His point is systemic: security advice trains people to reject exactly this behavior, so legitimate organizations that imitate scams weaken human defenses. HN supplied similar stories of dubious official PDFs, Google short domains, outsourced training emails, and authentication flows.

### Comment pulse

- Legitimate senders train unsafe habits when they resemble attackers → users cannot apply phishing guidance consistently without rejecting real business.
- Verification must work through an independently found channel → circular phone trees, chatbots, and absent account details make caution operationally impossible.
- Third-party domains erase familiar trust anchors → even knowledgeable users struggle to distinguish payment processors, corporate shorteners, and compromised infrastructure.

### LLM perspective

- **View:** Authentication UX is part of security; accurate back-end records cannot rescue an unverifiable message.
- **Impact:** Customers either ignore valid obligations or learn to follow suspicious links, benefiting future phishers.
- **Watch next:** Branded domains, authenticated in-account notices, consistent templates, and payment verification independent of message links.
