# Quake Shareware, a CD-ROM just a little too full

- Score: 487 | [HN](https://news.ycombinator.com/item?id=49338328) | Link: https://fabiensanglard.net/quake_shareware_cd/index.html

### TL;DR

In 1996, id sold a $9.95 Quake shareware CD containing encrypted installers for its full catalogue, unlockable by phone payment. The 22MiB game left ample CD capacity, but TestDrive’s protection kept the challenge-to-serial generator entirely on disc: the phone code proved payment yet held no secret. GNOMON released QCRACK 39 days after launch, contributing to roughly 150,000 stranded discs. The disc also exposed plaintext metadata, artifacts, and an unlock-breaking capitalization bug. Comments recalled CD-ROM’s multimedia leap, easy cracking culture, soundtrack quirks, and later purchases by teenage pirates.

### Comment pulse

- Huge CD capacity enabled FMV and audio experiments → players remember the 1990s as unusually rapid, tangible technological change.
- Easy cracking may have expanded Quake’s audience → counterpoint: the distribution failure and warehouse inventory indicate it was not intentional.
- Protection commonly failed at local checks → reverse engineers patched branches or generated keys once validation logic was found.

### LLM perspective

- View: The design confused obfuscation with authorization; a local verifier cannot securely mint the same proof it accepts.
- Impact: Paying users faced bugs while pirates got easier access, undermining both revenue and customer trust.
- Watch next: Preserve mixed-mode discs correctly, including soundtrack pre-emphasis metadata, while documenting the scheme’s remaining archival details.
