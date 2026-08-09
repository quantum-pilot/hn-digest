# A domain can now say it is for sale, in DNS

- Score: 328 | [HN](https://news.ycombinator.com/item?id=49221668) | Link: https://specification.website/spec/foundations/for-sale-dns/

- TL;DR  
  RFC 10023 defines a standard `_for-sale` TXT record in DNS so a domain can quietly advertise it’s for sale without parking or disrupting services. A single TXT at `_for-sale.example.com`, starting `v=FORSALE1;` plus one tag (price, URI, text, or proprietary code), targets brokers and automated checkers, not end users. Rules mandate short TTLs, leaf-only placement, and DNSSEC signing. Discussion centers on trademarks, squatting economics, registry “Georgism,” and the enduring value of good domains.

- Comment pulse  
  - Publicly listing domains for sale may weaken positions in trademark/UDRP disputes; anecdotes of big brands pressuring owners—counterpoint: earlier registration dates and trademark classes still matter.  
  - Georgist-style self-assessed annual taxes on declared domain value proposed to deter squatting; others note registry premium pricing already behaves similarly and can empower capital-rich actors.  
  - Absence of `_for-sale` records doesn’t imply “not for sale,” but still adds useful signal; commenters note domain trade remains huge despite apps and confusing TLDs.

- LLM perspective  
  - View: Encodes commercial intent in DNS, letting machines discover sale status without polluting UX or relying on fragile WHOIS data.  
  - Impact: Domain marketplaces, registrars, and large portfolio holders can streamline discovery, valuations, and outreach, potentially reducing spammy purchase emails.  
  - Watch next: Adoption by big registrars, integration into brokerage APIs, and whether forged records or DNSSEC failures cause fraud.
