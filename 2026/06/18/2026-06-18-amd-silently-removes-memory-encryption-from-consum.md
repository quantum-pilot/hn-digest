# AMD silently removes memory encryption from consumer Ryzen CPUs

- Score: 415 | [HN](https://news.ycombinator.com/item?id=48582320) | Link: https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change

### TL;DR

MSI testing found that AGESA 1.2.7.0 disables Transparent Secure Memory Encryption on consumer Ryzen CPUs even when BIOS settings enable it, while older firmware activated it and Pro chips remain unaffected. TSME firmware-encrypts all RAM against cold-boot, bus-snooping, and module-removal attacks. AMD says the feature belongs only to Pro products but has not explained whether this is deliberate segmentation or a regression. HN debated the narrow physical-threat model and lack of prior marketing, yet broadly objected to silently disabling capable hardware and leaving security status hard to detect.

### Comment pulse

- Consumer impact is disputed → most attackers with physical access have easier options — counterpoint: RAM encryption may also complicate RAMBleed and targeted bit flips.

- Unadvertised does not mean disposable → buyers may rely on working hardware behavior, and silent removal prevents informed risk and upgrade decisions.

- Firmware gating resembles artificial segmentation → commenters compared it with disabled GPU virtualization and paid vehicle features — counterpoint: uniform hardware can reduce base prices.

### LLM perspective

- **View:** The core failure is unverifiable security posture: a visible BIOS option can remain enabled while firmware silently withholds protection.

- **Impact:** High-risk laptop and confidential-work users must treat consumer Ryzen as lacking memory encryption unless independently verified.

- **Watch next:** AMD should publish affected SKUs, AGESA versions, intent, detection guidance, downgrade risks, and any restoration timeline.
