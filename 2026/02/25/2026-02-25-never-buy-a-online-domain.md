# Never buy a .online domain

- Score: 643 | [HN](https://news.ycombinator.com/item?id=47151233) | Link: https://www.0xsid.com/blog/online-tld-is-pain

- TL;DR  
  A developer registered a cheap .online domain (Radix registry) via Namecheap for a simple app landing page. Weeks later, browsers showed a red “unsafe site” warning, and the domain stopped resolving because Radix put it on serverHold after Google Safe Browsing blacklisted it. Removing the flag required Google Search Console DNS verification—impossible while the domain was suspended—creating a hard catch‑22. After the post hit Hacker News, someone at Google removed the listing and Radix restored the domain, prompting wider debate about sketchy gTLDs and Google’s de facto power over web presence.

- Comment pulse  
  - Registries auto-suspending domains based on Google Safe Browsing → hands effective censorship power to a private blacklist; makes affected TLDs risky for serious projects.  
  - Many Radix-operated gTLDs are cheap to register but pricey to renew → commenters treat that pattern, plus scam prevalence, as a red flag and sometimes block entire TLDs.  
  - Google’s dominance turns Search Console and Safe Browsing into gatekeepers → some see antitrust implications; others blame Radix for outsourcing policy to Google—counterpoint: Google only publishes a list.

- LLM perspective  
  - View: For anything important, favor long-established TLDs and registries with clear, independent abuse processes and documented appeal paths.  
  - Impact: Small developers and startups are most vulnerable; they lack leverage when registries and platforms form opaque, automated enforcement loops.  
  - Watch next: ICANN or regulators pressing for transparent registry suspension criteria, mandatory notification, and appeal channels decoupled from any single company’s blacklist.
