# MS confirms it will give the FBI your Windows PC data encryption key if asked

- Score: 404 | [HN](https://news.ycombinator.com/item?id=46743154) | Link: https://www.windowscentral.com/microsoft/windows-11/microsoft-bitlocker-encryption-keys-give-fbi-legal-order-privacy-nightmare

### TL;DR
Microsoft confirmed it will hand BitLocker recovery keys to the FBI when presented with a valid legal order. Because Windows 11 strongly pushes (and often requires) a Microsoft account, many PCs automatically back up their disk-encryption keys to Microsoft’s cloud, where they are stored in a form Microsoft itself can read. Critics argue this turns BitLocker into de‑facto key escrow, unlike zero‑knowledge designs from some other vendors, expanding the attack and surveillance surface while users often remain unaware.

---

### Comment pulse
- Design choice, not inevitability → Microsoft didn’t need to store keys server-side; doing so creates a legal choke point for governments.  
- Legal framing matters → “valid legal order” can include more than warrants, raising jurisdiction, due‑process, and secrecy concerns. — counterpoint: compelling evidence is standard in criminal law.  
- Convenience vs freedom → Cloud recovery helps locked‑out users, but undermines safe private spaces for thought and speech, chilling behavior even of law‑abiding people.

---

### LLM perspective
- View: Treat BitLocker cloud backup as optional key escrow; serious users should assume escrowed disks are searchable by states and insiders.  
- Impact: Enterprises, activists, journalists, and regulated sectors will need stricter key-management policies or non-escrowed encryption stacks.  
- Watch next: Whether Microsoft adds zero‑knowledge key wrapping, clearer opt-outs in setup, and more granular transparency on key-access requests.
