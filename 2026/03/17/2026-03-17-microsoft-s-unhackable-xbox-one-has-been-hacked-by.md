# Microsoft's 'unhackable' Xbox One has been hacked by 'Bliss'

- Score: 485 | [HN](https://news.ycombinator.com/item?id=47413876) | Link: https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level

### TL;DR
A researcher, Markus “Doom” Gaasedelen, has finally broken the Xbox One’s long‑standing reputation for being “unhackable.” His Bliss exploit uses precisely timed voltage glitching on the CPU’s power rail to bypass early boot memory protections, then hijack execution during a memcpy, enabling arbitrary unsigned code at every privilege level, including the hypervisor and security processor. It’s a silicon boot ROM fault, so first‑gen 2013 units are permanently compromised, opening the door to full firmware/game decryption, preservation, emulation, and eventual modchips.

---

### Comment pulse
- Lack of incentive kept Xbox One untouched → games were already on PC, and Microsoft offered official dev mode sideloading for homebrew, reducing demand for risky hacks.  
- Bliss showcases modern fault injection → double crowbar glitch skips MMU setup then seizes memcpy control; part of a growing voltage‑glitch arsenal. — counterpoint: similar attacks on smartcards/SoCs have been studied for years.  
- “Unhackable” mostly held in practice → only the launch‑era 2013 “VCR” hardware is affected; later revisions added anti‑glitch defenses, yet those early units are now cheap and plentiful used.

---

### LLM perspective
- View: Hardware fault injection is escaping niche labs and becoming practical against consumer consoles, forcing designers to treat power rails as an active attack surface.  
- Impact: Game preservationists and modders gain deep access to Xbox One internals; console vendors must reevaluate long‑term security claims and lifecycle guarantees.  
- Watch next: Public Bliss tooling, follow‑on work targeting later Xbox One/Series silicon, and new anti‑glitch countermeasures in next‑gen “Project Helix” and competitors.
