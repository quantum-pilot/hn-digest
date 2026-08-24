# MS confirms it will give the FBI your Windows PC data encryption key if asked

- Score: 404 | [HN](https://news.ycombinator.com/item?id=46743154) | Link: https://www.windowscentral.com/microsoft/windows-11/microsoft-bitlocker-encryption-keys-give-fbi-legal-order-privacy-nightmare

### TL;DR

Microsoft told Forbes it supplies BitLocker recovery keys when presented with a valid legal order, after doing so for an FBI investigation in Guam. Windows 11’s Microsoft-account setup normally uploads the key for convenient recovery, creating a copy Microsoft can access; users can disable cloud backup or delete uploaded keys. The company receives roughly 20 FBI requests annually, most unfulfillable because no key was stored. The article contrasts this design with zero-knowledge key storage and argues convenience has created an avoidable law-enforcement and breach-access point.

### Comment pulse

- Legal compulsion is downstream → if Microsoft never held recoverable keys, it could truthfully say compliance was technically impossible.
- Default recovery helps ordinary lockouts → critics want an explicit setup choice — counterpoint: escrow creates insider, criminal, and cross-jurisdiction exposure.
- “Legal order” is broader than warrant → commenters question which process actually authorized the disclosure.

### LLM perspective

- View: Encryption design determines whether legal demands meet ciphertext or an accessible recovery secret.
- Impact: Default cloud escrow trades effortless recovery for exposure users may never knowingly accept.
- Watch next: Setup consent, zero-knowledge storage, deletion guarantees, request transparency, and enterprise policy defaults.
