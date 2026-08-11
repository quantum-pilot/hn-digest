# Never buy a .online domain

- Score: 643 | [HN](https://news.ycombinator.com/item?id=47151233) | Link: https://www.0xsid.com/blog/online-tld-is-pain

### TL;DR

A developer recounts how a promotional `.online` domain bought through Namecheap disappeared after Google Safe Browsing flagged it and registry operator Radix applied a `serverHold`. Recovery became circular: Google Search Console required DNS proof of ownership, while the registry hold prevented DNS from resolving, and Radix wanted Google delisting first. After the story reached Hacker News, Google removed the warning and Radix restored the domain. The author now favors `.com`, early Search Console verification, and uptime monitoring, while criticizing the lack of notice or appeal path.

### Comment pulse

- Many blame Radix for converting Google’s warning into suspension; counterpoint: registries also face concentrated abuse on extremely cheap domains.
- Commenters saw an unaccountable verification loop, with Google requiring DNS proof while the registry hold prevented DNS from working.
- Others cautioned that one incident does not establish every `.online` domain is unsafe, even if new-TLD reputation risk is real.

### LLM perspective

- **View:** Automated trust systems need independent, reachable ownership and appeal channels.
- **Impact:** Coupled enforcement can turn a false positive into prolonged domain-level unavailability.
- **Watch next:** Whether registries add notice, temporary verification access, and human escalation.
