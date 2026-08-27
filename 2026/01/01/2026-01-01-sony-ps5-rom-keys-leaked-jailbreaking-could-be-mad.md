# Sony PS5 ROM keys leaked – jailbreaking could be made easier with BootROM codes

- Score: 233 | [HN](https://news.ycombinator.com/item?id=46455053) | Link: https://www.tomshardware.com/video-games/playstation/playstation-5-rom-keys-leaked-jailbreaking-could-be-made-easier-with-bootrom-codes

### TL;DR

Alleged PS5 ROM key seeds could help researchers decrypt and analyze boot code embedded in existing consoles, giving future exploit work a useful foothold that software updates cannot simply erase. They do not, however, produce an immediate jailbreak: researchers still need device-specific fuses and NAND groups or a usable BootROM vulnerability, while other security layers remain. HN strongly corrected the article’s more dramatic framing, discussing hardware extraction, key rotation’s limited value, and the distinction between understanding the boot chain and achieving persistent custom firmware.

### Comment pulse

- The leak is useful but incomplete → encrypted or obfuscated fuses and NAND data remain difficult prerequisites.
- Spare embedded keys may not help → the same hardware or supply-chain compromise could expose every provisioned set.
- PS3 history remains contested → removing OtherOS followed, rather than prevented, an exploit path using that feature.

### LLM perspective

- View: Key material expands researchers’ visibility, but exploitability depends on additional secrets or implementation flaws.
- Impact: Existing consoles become enduring research targets; Sony can harden future revisions while preserving layered defenses.
- Watch next: Verify the seeds, document decryption progress, identify BootROM bugs, and distinguish model-specific hardware revisions.
