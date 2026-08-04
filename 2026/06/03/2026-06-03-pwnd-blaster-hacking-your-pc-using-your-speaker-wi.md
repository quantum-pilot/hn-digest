# Pwnd Blaster: Hacking your PC using your speaker without ever touching it

- Score: 633 | [HN](https://news.ycombinator.com/item?id=48382310) | Link: https://blog.nns.ee/2026/06/03/katana-badusb/

### TL;DR

A researcher chained two failures in Creative’s Katana V2X soundbar: its Bluetooth Low Energy interface accepts privileged CTP commands without pairing, and its firmware updater verifies only a replaceable checksum, not a signature. From roughly 15 meters away, they flashed custom firmware that made the USB-connected speaker enumerate as a keyboard and type commands into its host PC; its microphone could also enable covert listening. Creative rejected the report as a cybersecurity risk, prompting an unofficial Bluetooth-blocking patch. HN condemned both the design and response.

### Comment pulse

- Unauthenticated reflashing is a vulnerability → proximity and device ownership constrain likelihood, but arbitrary firmware on a trusted USB peripheral creates severe impact.
- Peripheral security is systemic → manufacturers often outsource firmware, lack disclosure channels, and neglect signing, patchability, or long-term software ownership.
- Vendor economics reward denial → a niche, short-range exploit may seem cheaper to ignore — counterpoint: lockout worms and targeted attacks expand liability.

### LLM perspective

- **View:** The decisive failure is transitive trust: wireless access inherited firmware authority, which inherited keyboard authority on the PC.
- **Impact:** Owners face PC compromise and eavesdropping without interacting with the attacker.
- **Watch next:** Signed firmware, mandatory BLE authentication, radio-disable controls, Creative advisories, and independent testing of related soundbars.
