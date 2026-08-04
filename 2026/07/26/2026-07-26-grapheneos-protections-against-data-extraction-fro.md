# GrapheneOS protections against data extraction from locked devices

- Score: 372 | [HN](https://news.ycombinator.com/item?id=49055169) | Link: https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices

### TL;DR

GrapheneOS describes layered protection for locked Pixels: disk encryption, secure-element throttling limited to 20 guesses, firmware-update resistance to coerced backdoors, 128-character passwords, fingerprint-plus-PIN, hardened memory, and locked USB. Its default 18-hour auto-reboot clears memory and returns the main profile to Before First Unlock; secondary users and Private Space can independently return to that state. A duress credential wipes every profile but is optional and may carry legal or physical consequences. Commenters focus on border searches, safer backup-and-wipe workflows, decoy credentials, and confusion between privacy tools and criminal intent.

### Comment pulse

- Data protection does not depend on destruction → commenters stress BFU encryption and short auto-reboot timers, especially after a duress-wipe prosecution raised alarm.
- Travelers want reversible minimization → wipe-before-border plans need reliable self-hosted restore; GrapheneOS says encrypted per-profile backups exist but need a usability overhaul.
- Decoy unlocks appeal under coercion → users propose showing harmless data instead of visibly wiping — counterpoint: authorities may demand hidden stores or backups too.

### LLM perspective

- View: Layered controls reduce dependence on any safeguard; encryption, authentication, exploit resistance, USB policy, and state resets reinforce one another.
- Impact: Strong defaults protect ordinary seizures, while explicit duress actions shift risk from technical extraction toward legal and physical coercion.
- Watch next: Backup replacement, Motorola hardware support, separate BFU and AFU credentials, USB-PD hardening, decoy-mode threat models, and court outcomes.
