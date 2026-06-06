# Distributing Mac software is increasing my cortisol levels

- Score: 175 | [HN](https://news.ycombinator.com/item?id=48075366) | Link: https://blog.kronis.dev/blog/apple-is-increasing-my-cortisol-levels

### TL;DR
A solo developer building a tiny Mac utility runs into macOS Gatekeeper: unsigned binaries are quarantined, and avoiding scary warnings effectively requires a $99/year Apple Developer account plus a clumsy ID-verification flow that worked only via iPhone. For a pay-what-you-want tool likely earning tens of dollars, this is economically absurd. The author generalizes to Windows, where code-signing and SmartScreen are even more extortionate, and argues the whole ecosystem resembles pre–Let’s Encrypt TLS: expensive, rent-seeking, and hostile to hobbyists.

---

### Comment pulse
- Gatekeeper is user-configurable → power users can disable it in seconds; average users won’t, and Apple’s “trust Apple or trust everyone” model lacks nuance — counterpoint: stricter defaults meaningfully improve safety.
- Indie devs feel squeezed → poor Apple backward compatibility, constant breakage, and mandatory fees; Windows is cheaper to enter but code-signing/EV certs and SmartScreen are an even bigger racket.
- Security advocates defend friction → paid, ID-verified certs deter some malware authors; critics note plenty of signed, notarized malware still reaches users, so costs mostly punish honest devs.

---

### LLM perspective
- View: Code-signing should be cheap, identity-focused infrastructure, not a recurring toll tied to specific hardware and app stores.
- Impact: Hobby and niche commercial tools quietly skip macOS/Windows, shrinking software diversity and pushing more usage into web and app-store silos.
- Watch next: Any “free CA for code” initiative, OS-level support for national eID signing, or store policies relaxing fees for low-revenue developers.
