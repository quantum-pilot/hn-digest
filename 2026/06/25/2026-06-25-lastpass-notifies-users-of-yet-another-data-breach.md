# LastPass notifies users of yet another data breach

- Score: 468 | [HN](https://news.ycombinator.com/item?id=48671468) | Link: https://9to5mac.com/2026/06/23/lastpass-notifies-users-of-yet-another-data-breach/

### TL;DR

LastPass notified customers that attackers breached market-research partner Klue and accessed names, phone numbers, emails, physical addresses, support cases, and sales data through integrations with Salesforce and Gong. Password vaults were not affected. LastPass revoked Klue access, rotated API tokens, contacted law enforcement, investigated scope, and warned that exposed context could enable targeted phishing. HN remained deeply distrustful given LastPass’s 2015 and 2022 incidents, questioned why identifiable data reached a research vendor, and favored local password managers; some stressed that this breach did not expose passwords.

### Comment pulse

- Vendor data minimization failed → commenters saw no reason Klue needed names, addresses, and support details instead of anonymized research data.
- Repeated incidents destroyed confidence → users recommended KeePassXC or Password Safe with locally controlled vaults and optional self-managed sync.
- Scope matters → critics treated any recurrence as disqualifying — counterpoint: vault encryption still served users because passwords remained inaccessible.

### LLM perspective

- **View:** The immediate risk is contextual phishing, while the governance failure is excessive customer-data propagation across SaaS vendors.
- **Impact:** Organizations must treat CRM and support metadata as sensitive authentication-adjacent material, not harmless business contact data.
- **Watch next:** Confirm affected-customer counts, token permissions, retention practices, Klue’s other impacted clients, ransom disclosures, and phishing campaigns.
