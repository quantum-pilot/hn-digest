# HSBC blocks its app due to F-Droid-installed Bitwarden

- Score: 231 | [HN](https://news.ycombinator.com/item?id=46431453) | Link: https://mastodon.neilzone.co.uk/@neil/115807834298031971

### TL;DR

An HSBC customer reported that the bank’s Android app refused to run because Bitwarden had been installed through F-Droid, despite other F-Droid applications remaining accepted. He deleted HSBC’s app, retained Bitwarden, and planned to use the bank’s website with a requested physical security token. HN commenters debated whether Play Integrity, app-origin checks, or HSBC’s own package visibility policy caused the block. They contrasted banks that warn rooted-device users with those enforcing hard exclusions and questioned broad installed-app enumeration.

### Comment pulse

- Security policy removes user choice → several banks hard-block modified environments, while Monzo reportedly warns and permits continuation.
- Android package visibility enables screening → financial apps may receive broad installed-package access for security purposes.
- Web access is a crucial fallback → physical tokens and PWAs reduce dependence on proprietary mobile attestation.

### LLM perspective

- View: Blocking software provenance without explaining the threat converts risk management into opaque platform gatekeeping.
- Impact: Privacy-conscious customers must choose between banking convenience, alternative app stores, and separate devices.
- Watch next: Request HSBC’s exact detection criteria, false-positive process, supported stores, and non-app authentication commitments.
