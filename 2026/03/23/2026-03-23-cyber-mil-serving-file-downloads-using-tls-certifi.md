# Cyber.mil serving file downloads using TLS certificate which expired 3 days ago

- Score: 153 | [HN](https://news.ycombinator.com/item?id=47490816) | Link: https://www.cyber.mil/stigs/downloads

- TL;DR  
  DoD’s cyber.mil site, which distributes security tools, is serving downloads over an expired IdenTrust TLS certificate while posting a vague “TSSL Certification renewal” notice and instructing users to bypass browser errors. Commenters argue this is a serious MITM risk and emblematic of poor PKI hygiene, even if it affects only unclassified public services. Others explain DoD’s convoluted internal PKI, CAC smartcards, and isolated networks, and broaden the discussion to how often enterprises and banks still mishandle certificate renewal.

- Comment pulse  
  - DoD’s PKI looks incompetent → expired cert, nonsensical “TSSL” messaging, and a memo-driven exception regime—counterpoint: internal CAs, CAC auth, and isolated networks genuinely complicate public TLS.  
  - Telling users to click through TLS errors is reckless → normalizes ignoring warnings and lets any MITM swap downloadable executables with malware using a bogus cert.  
  - Cert expiry both matters and is hard → limits damage from key leaks, but legacy services lack ACME; many enterprises still juggle brittle manual renewals.

- LLM perspective  
  - View: This episode shows misaligned policy, tooling, and user guidance turning a routine PKI task into a real security risk.  
  - Impact: Governments and large enterprises must modernize certificate management or keep generating incidents that erode public trust in their security posture.  
  - Watch next: Whether DoD standardizes ACME-style automation and how browsers further discourage or gate unsafe TLS error bypasses.
