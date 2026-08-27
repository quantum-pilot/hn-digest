# Xubuntu.org Might Be Compromised

- Score: 305 | [HN](https://news.ycombinator.com/item?id=45634367) | Link: https://old.reddit.com/r/Ubuntu/comments/1oa4549/xubuntuorg_might_be_compromised/

### TL;DR

A Reddit report said Xubuntu.org’s torrent download served a ZIP containing a suspicious Windows executable and oddly dated terms instead of a torrent file. Community analysis described the executable as malware that replaces copied cryptocurrency addresses, while warning it could have other behavior. The downloads page was disabled and a moderator attributed the incident to a hosting “slip-up,” language commenters considered inadequate. Discussion stressed that unaffected ISO checksums prove little unless signatures and reference values come through an independent trust path.

### Comment pulse

- The reported compromise targeted a narrow path → torrent users receiving and running the unexpected Windows executable faced the clearest risk.
- Same-site checksums are insufficient → attackers controlling downloads may also replace unsigned verification data.

### LLM perspective

- View: Distribution security depends on independently verifiable signatures, not merely publishing hashes beside artifacts.
- Impact: Affected users may need credential rotation, wallet migration, and system reinstallation given uncertain malware scope.
- Watch next: Seek Xubuntu’s incident report, hosting root cause, signed artifacts, exposure window, and confirmed remediation.
