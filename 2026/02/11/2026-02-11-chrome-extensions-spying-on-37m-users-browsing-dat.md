# Chrome extensions spying on 37M users' browsing data

- Score: 227 | [HN](https://news.ycombinator.com/item?id=46973083) | Link: https://qcontinuum.substack.com/p/spying-chrome-extensions-287-extensions-495

## TL;DR
Researchers built an automated system that runs Chrome in Docker behind a MITM proxy and statistically correlates URL length with outbound traffic to detect history exfiltration. Scanning 240k+ extensions, they flagged 287 that leak browsing data—about 37.4M installs, ~1% of Chrome users. Many leaks are tied to data-broker ecosystems (Similarweb, Curly Doggo, Offidocs, “Big Star Labs”) and use deliberate obfuscation/encryption. HN discussion focuses on extension supply‑chain attacks, weak Chrome Store oversight, and mitigation via open source, manual audits, and traffic blocking.

## Comment pulse
- Legitimate extensions are bought, then modified to exfiltrate data → classic supply‑chain attack leveraging existing user bases and trust.
- Defense playbook: monitor extension updates/ownership, block extension network traffic (e.g., via per‑extension filters), self‑build from reviewed source when possible.
- “Only open‑source extensions” → better scrutiny signal, not a guarantee; distribution binaries may differ from public code — counterpoint: regulators and stores must shoulder more burden.

## LLM perspective
- View: Treat browser extensions as high‑risk apps with least‑privilege, periodic review, and network controls, not lightweight toys.
- Impact: Enterprises, schools, and power users should centralize extension policy, logging, and vetting; random installs become unacceptable.
- Watch next: Independent extension scanners, store‑level attestation of builds, and lawsuits/regs targeting undisclosed data‑broker collection via extensions.
