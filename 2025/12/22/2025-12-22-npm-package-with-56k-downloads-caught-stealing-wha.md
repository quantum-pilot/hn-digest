# NPM Package with 56K Downloads Caught Stealing WhatsApp Messages

- Score: 154 | [HN](https://news.ycombinator.com/item?id=46359996) | Link: https://www.koi.ai/blog/npm-package-with-56k-downloads-malware-stealing-whatsapp-messages

### TL;DR
An npm package named `lotusbail` posed as a fork of the popular WhatsApp Web client library Baileys and racked up 56k downloads while secretly acting as full‑featured spyware. It transparently proxied WhatsApp Web traffic to work as advertised, but also captured auth tokens, every message, contacts, and media, then used custom RSA/AES and heavy obfuscation to exfiltrate data and install a persistent paired-device backdoor. The writeup frames this as a supply-chain pattern that static checks and reputation can’t reliably catch, sparking debate about package managers, platform lock‑downs, and developer responsibility.

### Comment pulse
- Lockdowns hurt users → Platforms respond by tightly siloing data; without official, granular APIs, developers resort to sketchy clients and users lose reliable backup/interop options.  
- Package ecosystems feel structurally risky → Late‑fetched deps, global tools, random Docker images and curl | sh create unaudited surfaces; engineers admit weak supply‑chain hygiene.  
- Who’s responsible? → Some expect npm/GitHub stewardship and fear lawsuits; others argue open‑source code is caveat emptor and auditing remains each downstream developer’s duty.  

### LLM perspective
- View: Functional, targeted malware in popular libraries is now normal; treating third‑party code as trusted by default is indefensible.  
- Impact: Teams should treat dependency selection as security‑critical: SBOMs, pinning, vendoring, and runtime anomaly detection become baseline, not “nice‑to‑have” extras.  
- Watch next: Watch for IDEs and CI systems integrating behavioral sandboxing of dependencies, plus stronger identity and signing requirements for package authors.
