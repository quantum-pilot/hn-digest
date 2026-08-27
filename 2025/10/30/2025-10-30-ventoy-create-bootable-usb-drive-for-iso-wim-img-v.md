# Ventoy: Create bootable USB drive for ISO/WIM/IMG/VHD(x)/EFI Files

- Score: 253 | [HN](https://news.ycombinator.com/item?id=45760340) | Link: https://github.com/ventoy/Ventoy

### TL;DR

Ventoy turns a USB drive into a multi-image boot menu: users copy ISO, WIM, IMG, VHD(X), or EFI files onto it instead of reformatting for every operating system. The project claims support for legacy BIOS, several UEFI architectures, MBR and GPT, Secure Boot, persistence, automated installation, and more than 1,200 tested ISOs. HN users praise replacing piles of dedicated flash drives, but report uneven compatibility, including some Linux and Windows images, and debate the security and reproducibility of bundled binary blobs.

### Comment pulse

- Multi-image copying is the central convenience → one fast drive can hold installers, rescue systems, diagnostics, and persistent environments.
- Compatibility is not universal → commenters report boot failures despite the project’s broad tested-image claims.
- Binary provenance remains contested → documented sources and hashes reassure some users, while others want reproducible from-source builds.

### LLM perspective

- View: Ventoy trades repeated flashing for a persistent boot layer, making that layer’s trustworthiness unusually important.
- Impact: Administrators save media and setup time but must test each image on target firmware beforehand.
- Watch next: Audit bundled blobs, reproducible builds, Secure Boot behavior, and compatibility across current Windows and Linux images.
