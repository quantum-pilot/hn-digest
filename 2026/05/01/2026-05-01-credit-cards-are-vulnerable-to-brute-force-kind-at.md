# Credit cards are vulnerable to brute force kind attacks

- Score: 174 | [HN](https://news.ycombinator.com/item?id=47979839) | Link: https://metin.nextc.org/posts/Credit_Cards_Are_Vulnerable_To_Brute_Force_Kind_Attacks.html

### TL;DR

After an e-commerce account breach, the author reconstructs how attackers may have derived a stored virtual card from its visible first six and last four digits plus expiration date. Luhn validation reduces the unknown account-number space to roughly 100,000 candidates; distributed merchant-validation endpoints and detailed decline codes can identify the PAN, then test up to 999 CVVs. Six hours later, attackers used merchants without 3-D Secure to exhaust the reduced limit. The bank returned the money through chargeback, but PCI-compliant masking had not prevented enumeration.

### Comment pulse

- Some proposed account-updater or digital-wallet tokens as an alternative explanation because replacement cards can inherit merchant payment relationships.
- Processors prohibit card testing and penalize weak controls — counterpoint: low-rate attempts distributed across merchants, IPs, and changing PANs evade local detection.
- Liability varies among merchants and issuers; consumers still must inspect statements because settlement can occur with minimal authentication.

### LLM perspective

- Rate limits must aggregate across the payment network, not individual merchants alone.
- Decline responses should reveal no field-level correctness to untrusted clients.
- Virtual cards scoped per merchant reduce reuse after one account leaks identifying fragments.
