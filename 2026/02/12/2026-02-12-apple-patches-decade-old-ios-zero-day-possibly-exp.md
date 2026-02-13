# Apple patches decade-old iOS zero-day, possibly exploited by commercial spyware

- Score: 243 | [HN](https://news.ycombinator.com/item?id=46989107) | Link: https://www.theregister.com/2026/02/12/apple_ios_263/

### TL;DR
Apple’s iOS 26.3 update fixes CVE-2026-20700, a dyld bug present since iOS 1.0 that let attackers with a memory‑write foothold run arbitrary code. Chained with WebKit flaws, it enabled near zero‑click device takeover, likely used by commercial spyware vendors similar to Pegasus/Predator and aimed at high‑value targets. The case highlights how long-lived C/C++ code can harbor critical bugs, how commercial spyware has “democratized” nation‑state capabilities, and how users remain dependent on OS vendors for both patching and detection.

---

### Comment pulse
- Patches trail spyware vendors → NSO-style actors keep fresh exploit chains ready; annual iOS zero-clicks show determined adversaries outpace defensive patch cycles.  
- Apple pushes users to iOS 26 → leaving iOS 18 unpatched on capable devices feels like coercing adoption of disliked UI for security. — counterpoint: 18.7.5 exists.  
- “You’re not interesting” is obsolete → commercial spyware puts powerful exploits in many hands; huge legacy C/C++ bases and weak forensics make silent compromise realistic.

---

### LLM perspective
- View: Long-lived core components like dyld need systematic memory-safe refactors plus better exploit detection, not just one-off patches.  
- Impact: High-risk users should combine fast updates, Lockdown Mode, and independent mobile threat defense; orgs must assume occasional full-device compromise.  
- Watch next: Apple’s memory-safe C (BoundsSafety), increased Swift in low-level code, and regulatory pressure on commercial spyware/export of zero-click chains.
