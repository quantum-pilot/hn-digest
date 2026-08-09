# Microsoft's 'unhackable' Xbox One has been hacked by 'Bliss'

- Score: 485 | [HN](https://news.ycombinator.com/item?id=47413876) | Link: https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level

### TL;DR

The captured article body is missing, but its headline and HN discussion describe Bliss, a voltage-glitch attack against the original 2013 “VCR” Xbox One that enables unsigned code. Commenters clarify that this is a double glitch: one skips MMU initialization, then another seizes the program counter during a memory copy to execute shellcode. Later hardware revisions remain unaffected because Microsoft enabled anti-glitch protections and separated security/reset functions. Readers attributed the console’s 13-year resistance both to strong architecture and weak hacking incentives, given PC game overlap and official developer mode.

### Comment pulse

- Some called the console effectively unhackable because it fell five-and-a-half years after its successor reached market.
- Original units remain common and inexpensive secondhand, so the narrow first-silicon scope still matters to hobbyists and preservationists.
- Precise voltage-rail control fascinated readers, though similar fault-injection techniques predate Bliss and also affected the Xbox 360.

### LLM perspective

- **View:** Hardware security is measured by attack cost and affected scope, not permanent impossibility.
- **Impact:** Owners gain a homebrew path; Microsoft learns which physical defenses survived only on revised silicon.
- **Watch next:** Reproducibility, equipment cost, persistence, payload tooling, and attacks against later revisions.
