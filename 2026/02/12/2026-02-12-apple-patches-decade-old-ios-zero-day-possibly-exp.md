# Apple patches decade-old iOS zero-day, possibly exploited by commercial spyware

- Score: 243 | [HN](https://news.ycombinator.com/item?id=46989107) | Link: https://www.theregister.com/2026/02/12/apple_ios_263/

### TL;DR

Apple’s iOS 26.3 fixes CVE-2026-20700, a dyld flaw present since iOS 1.0 that lets an attacker who already has memory-write capability execute code. Google’s Threat Analysis Group found it; Apple says it was exploited against specific targets on pre-iOS 26 devices and may have formed part of a sophisticated chain. The article links it with WebKit bugs that could enable zero- or one-click compromise, while commercial-spyware involvement remains an expert comparison, not attribution. Commenters stressed patching, detection, platform trust, legacy memory safety, and attackers’ recurring replacement chains.

### Comment pulse

- Platform compromise defeats app-level defenses → developers can minimize data and permissions, but ultimately rely on the operating system’s security boundary.
- Targeted does not mean harmless → commercial exploit markets can spread advanced capabilities beyond their original state customers.
- Upgrade support caused confusion → commenters alleged iOS 18 exposure — counterpoint: another pointed to an iOS 18.7.5 release.

### LLM perspective

- View: The dyld bug is one link requiring prior memory write; chain composition matters more than its age alone.
- Impact: High-risk users face potential device takeover, while developers cannot fully compensate for a compromised linker and browser stack.
- Watch next: Apple’s detailed advisory, affected-version matrix, chain disclosure, forensic indicators, Lockdown Mode effectiveness, and commercial-spyware attribution evidence.
