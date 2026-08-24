# That's not how email works

- Score: 218 | [HN](https://news.ycombinator.com/item?id=46799304) | Link: https://danq.me/2026/01/28/hsbc-dont-understand-email/

### TL;DR

After HSBC mailed a warning that emails were being returned undelivered, the author found the bank held the correct address and its messages were arriving. He infers HSBC treated blocked tracking-pixel requests as failed delivery, confusing an unreliable open metric with email transport status. The emails also embedded tracking images over unencrypted HTTP, potentially exposing the bank domain and enabling network tampering. He urges HSBC to use real delivery or explicit confirmation mechanisms, secure any remote content, and stop framing privacy-protected reading as an invalid address.

### Comment pulse

- Another bank customer reported being switched to paper statements unless remote images loaded, suggesting the misuse is not isolated.
- Banking engineers blamed legacy systems and incentives that reward inflated open rates over accurate clicks or honest uncertainty.
- Unencrypted pixels alarmed readers — counterpoint: HTTPS may still reveal the bank hostname, though it would protect content integrity.

### LLM perspective

- View: A probabilistic engagement signal appears to have escaped its purpose and become a customer-record decision.
- Impact: Conflating image loads with delivery penalizes privacy settings, creates needless support work, and can corrupt compliance evidence.
- Watch next: HSBC’s tracking transport, letter wording, validation method, opt-out controls, and whether regulators distinguish delivery from opens.
