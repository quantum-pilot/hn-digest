# Honda Civics and the Evil Valet

- Score: 397 | [HN](https://news.ycombinator.com/item?id=48523080) | Link: https://juniperspring.org/posts/honda-evil-valet/

### TL;DR

A 2021 Honda Civic head unit accepts USB firmware packages signed with the publicly known AOSP test key; Honda’s extra version checks can be spoofed, and stock-like recovery verification then treats attacker-built packages as valid. With cabin access, power, and the front USB port, someone can gain persistent arbitrary code execution without conventional root. The author released ota-builder and reverse-engineering tools but cautions that untested versions may soft-brick. HN debated whether physical access makes this trivial or irrelevant, emphasizing stored contacts, locations, microphones, radios, and possible vehicle-bus reach.

### Comment pulse

- Physical access divides threat models → some consider cabin access decisive — counterpoint: modern encrypted devices show local compromise need not be cheap or automatic.
- Infotainment exceeds radio risk → implants can access historical personal data and potentially internal buses while leaving less evidence than an added tracker.
- Signing policy is insufficient → organizations sometimes sign firmware correctly but fail to verify it, or let update packages define verification logic.

### LLM perspective

- **View:** A public signing key converts authenticated update into authenticated attacker code; version checks are compatibility gates, not trust anchors.
- **Impact:** Owners cannot reliably detect implants; manufacturers inherit surveillance, privacy, and lateral vehicle-security exposure from an infotainment shortcut.
- **Watch next:** Confirm affected head-unit variants, key usage, CAN segmentation, rollback protection, forensic indicators, disclosure status, and Honda’s remediation path.
