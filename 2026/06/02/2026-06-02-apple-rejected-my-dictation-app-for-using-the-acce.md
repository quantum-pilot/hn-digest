# Apple rejected my dictation app for using the accessibility API

- Score: 286 | [HN](https://news.ycombinator.com/item?id=48369088) | Link: https://www.mitmllc.com/blog/apple-rejected-my-dictation-app/

### TL;DR
A developer with repetitive strain injury built WhisperPad, a Mac menu-bar dictation app that runs locally and auto-pastes text into any app via the macOS accessibility API. Apple had previously approved it, but rejected a paid update under guideline 2.4.5, arguing the accessibility API use wasn’t “accessibility.” He appealed and lost, then split the product: a constrained App Store version that only copies to clipboard, and a full-featured direct-download version, learning payments, licensing, and updates. HN debates Apple’s privacy stance, opaque rules, and platform lock-in.

---

### Comment pulse
- Accessibility API over-broad; Apple restricts it to limit cross-app spying, but this blocks benign tools and lacks fine-grained permissions — counterpoint: broad control is exactly what many disabled users need.  
- Common pattern: cut-down App Store build plus full “Pro” version sold directly; some suggest using App Store purchases as unlock keys, others warn this likely violates Apple’s rules.  
- iOS sandboxing makes powerful dictation tools nearly impossible; some users prize this security, others see anti-competitive lock-in and point to EU alt stores and open-source local dictation apps.

---

### LLM perspective
- View: The real fix is capability-based permissions for automation/accessibility: per-target, per-action grants instead of one huge, scary accessibility entitlement.  
- Impact: More indie assistive tools will bypass the App Store, shrinking visibility for people who’d benefit most while increasing user friction and trust concerns.  
- Watch next: Whether Apple introduces narrower automation APIs, and how EU alternative stores treat cross-app assistive tools versus Apple’s own walled-garden policies.
