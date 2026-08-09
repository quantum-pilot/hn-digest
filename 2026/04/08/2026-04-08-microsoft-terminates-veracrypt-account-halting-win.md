# Microsoft terminates VeraCrypt account, halting Windows updates

- Score: 447 | [HN](https://news.ycombinator.com/item?id=47690977) | Link: https://www.404media.co/microsoft-abruptly-terminates-veracrypt-account-halting-windows-updates/

### TL;DR

Microsoft terminated the account VeraCrypt uses for Windows distribution, leaving future signed updates uncertain and offering no public explanation in the accessible article. The incident illustrates how an open-source security project can depend on a platform owner’s identity, signing, and publishing infrastructure even when its code is independent. HN commenters reported similar verification failures and Partner Center lockouts affecting other developers, including Windscribe. Their concern was less one isolated account than opaque, unappealable gatekeeping in a software supply chain users are taught to trust.

### Comment pulse

- Affected developers described failed renewals with no human support → some moved to SignPath or costlier third-party certificates.
- Platform control drew the sharpest criticism → signing for user safety should not let one vendor silently decide which software can ship.
- The pattern may be broader → commenters cited multiple Windows driver developers losing Partner Center access without explanations.

### LLM perspective

- **View:** Code signing improves provenance only when issuer decisions are transparent, appealable, and replaceable.
- **Impact:** VeraCrypt users may lose timely Windows releases; maintainers face cost, delay, and reputation damage unrelated to code quality.
- **Watch next:** Account reinstatement, Microsoft’s explanation, alternative signing arrangements, affected-project counts, and independent governance proposals.
