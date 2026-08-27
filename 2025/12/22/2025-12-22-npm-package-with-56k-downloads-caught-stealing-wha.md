# NPM Package with 56K Downloads Caught Stealing WhatsApp Messages

- Score: 154 | [HN](https://news.ycombinator.com/item?id=46359996) | Link: https://www.koi.ai/blog/npm-package-with-56k-downloads-malware-stealing-whatsapp-messages

### TL;DR

Koi Security alleges that `lotusbail`, a functioning fork of the Baileys WhatsApp Web client with 56,000 downloads, secretly captured credentials, messages, contacts, and media. The package allegedly wrapped WebSockets, obscured its exfiltration server through multiple encoding and encryption layers, installed persistent account access through a hidden pairing code, and used 27 anti-debugging traps. Removing the package would not unlink the attacker’s device. HN treated this as another unreviewed-dependency failure, while noting the report comes from a security vendor and the package was malicious from inception, not compromised later.

### Comment pulse

- Trust failure → functional code, download counts, and convenient package installation encourage deployment without auditing behavior or provenance.
- Ecosystem scope → late-fetched dependencies amplify risk — counterpoint: vendoring or direct Git references would not sanitize intentionally malicious code.
- Access design → granular official APIs might reduce reverse-engineered clients, while complete lockdown sacrifices legitimate backup and interoperability.

### LLM perspective

- View: Working functionality is an effective malware cover because testing validates the advertised path, not hidden side effects.
- Impact: Affected users must remove the package and manually revoke linked WhatsApp devices to end persistent access.
- Watch next: Seek independent analysis, registry removal, incident reports, indicators of compromise, maintainer identity, and reproducible behavioral detections.
