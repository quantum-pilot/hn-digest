# Microsoft mishandling example.com

- Score: 223 | [HN](https://news.ycombinator.com/item?id=46731996) | Link: https://tinyapps.org/blog/microsoft-mishandling-example-com.html

### TL;DR
Microsoft’s Outlook Autodiscover service has, since early 2020, mapped `email@example.com` to Sumitomo Electric’s `sei.co.jp` mail servers via an internal configuration, not DNS. That means anyone using `example.com` as a dummy address in Outlook may have had test credentials sent toward a third party’s infrastructure. Hacker News discussion focuses on how Outlook routinely sends full email/password pairs to Microsoft for autodiscovery and sometimes proxies entire mailboxes, raising broader concerns about privacy, design flaws, and Microsoft’s treatment of reserved domains.

---

### Comment pulse
- Outlook sends full credentials for any account to Microsoft for autodiscovery, and often acts as a mailbox MITM → violates many admins’ security expectations — counterpoint: enables cross-device notifications and cloud “features.”
- Autodiscover’s design has long been a security risk → clients transmit passwords to various hosts, expanding attack surface well beyond the user’s actual mail provider.
- Mapping `example.com` to `sei.co.jp` likely stems from someone “claiming” the domain in Microsoft’s cloud without proper DNS verification → echoes older Microsoft guidance misusing `.local` despite later reservations.

---

### LLM perspective
- View: Using reserved domains in examples isn’t harmless when major clients special-case them; test data can become real traffic to unintended parties.
- Impact: Mail admins and security teams should inspect outbound connections and block or constrain Outlook’s cloud autodiscovery/proxy behavior where policy requires.
- Watch next: Whether Microsoft removes the rogue mapping, tightens domain-ownership checks, and exposes a transparent, local-only account setup path.
