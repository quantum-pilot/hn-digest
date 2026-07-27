# GrapheneOS protections against data extraction from locked devices

- Score: 372 | [HN](https://news.ycombinator.com/item?id=49055169) | Link: https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices

### TL;DR
GrapheneOS describes how it hardens Android on Pixel devices to resist data extraction from locked phones. Core defenses are hardware‑backed full‑disk encryption, a secure element that strictly rate‑limits unlock attempts and resists insider firmware tampering, OS exploit mitigations (e.g., MTE), and physical‑access protections like disabling USB data. It raises password limits to 128 characters and offers a fingerprint+PIN flow so users can rely on strong passphrases plus convenience. A duress PIN that wipes the device is emphasized as optional, risky, and not required for strong protection.

### Comment pulse
- Posted amid cases of a protester prosecuted after using duress wipe and a journalist protected by auto‑reboot → clarifies GrapheneOS works even without duress codes.  
- Many want simple full backups to self‑hosted storage to wipe phones before borders; others propose hidden partitions—counterpoint: could just expand what authorities insist on inspecting.  
- Thread debates decoy vs true duress passwords; GrapheneOS rejects fake‑wipe UIs as unrealistic and dangerous, while some users criticize the project’s public messaging tone.  

### LLM perspective
- View: Treating law‑enforcement scenarios as just another threat model keeps design grounded in technical reality instead of wishful narratives.  
- Impact: Strong defaults plus honest documentation help non‑experts—journalists, activists, travelers—make explicit trade‑offs instead of relying on folklore security advice.  
- Watch next: secure‑element‑level duress support, revamped backups, and broader hardware partners could shift GrapheneOS closer to mainstream high‑risk‑user platform.
