# Veracrypt project update

- Score: 1116 | [HN](https://news.ycombinator.com/item?id=47686549) | Link: https://sourceforge.net/p/veracrypt/discussion/general/thread/9620d7a4b3/

### TL;DR

VeraCrypt maintainer Mounir Idrassi says Microsoft terminated the long-used account that signs Windows drivers and the bootloader without warning, explanation, appeal, or reachable human support. Linux and macOS releases can continue, but Windows—most users’ platform—cannot receive updates, and the current 1.26.24 signature chain is nearing expiry. A Rufus developer reported an identical screen caused by failed automated business-domain validation and said human support resolved it; an internal contact offered routing help. HN became more alarmed when WireGuard’s maintainer disclosed a similar suspension and a 60-day appeal.

### Comment pulse

- Mandatory Windows Hardware Program re-verification reportedly began October 2025; partners missing it could be marked rejected and suspended.
- Some suspected hostility toward privacy tools — counterpoint: others favored a broad automated-validation failure, not a targeted anti-encryption campaign.
- Developers described signing approval as a de facto whitelist with opaque, expensive requirements and support loops disproportionately burdening independent publishers.

### LLM perspective

- **View:** Security infrastructure fails its purpose when revocation controls cannot distinguish malicious signers from maintainers needing urgent patch delivery.
- **Impact:** Windows users face delayed fixes; open-source publishers inherit a single-vendor operational dependency outside their control.
- **Watch next:** Account restoration, root-cause disclosure, certificate-expiry behavior, emergency signing paths, service guarantees, and appeal deadlines.
